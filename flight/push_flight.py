#encoding=utf-8

import redis
import MySQLdb
import time
import datetime
import sys
import hashlib

from LOG import _ERROR, _INFO
from fuseFlightDatat import fuse_flight_data
from calCost_flight import durCal


def loadForexInfo():
	forex_rate_dic = {}
	conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db='onlinedb')
	cursor = conn.cursor()

	sql = 'select currency_code, rate from exchange;'
	n = cursor.execute(sql)
	datas = cursor.fetchall()

	for data in datas:
		forex = data[0].encode('utf-8').strip()
		rate = data[1]

		forex_rate_dic[forex] = rate

	_INFO('load forex info',['forex_size = ' + str(len(forex_rate_dic))])	
	cursor.close()
	conn.close()

	return forex_rate_dic

def getStrMd5(srcStr):
	myMd5 = hashlib.md5()
	myMd5.update(srcStr)
	strMd5 = myMd5.hexdigest()

	return strMd5

#s:2014-08-09 12:24:12
def str2datetime(s):
	l = s.split(' ')
	if len(l) != 2:
		return None

	item1 = l[0].split('-')
	item2 = l[1].split(':')

	if len(item1) != 3 or len(item2) != 3:
		return None

	dt = datetime.datetime(int(item1[0]), int(item1[1]), int(item1[2]), int(item2[0]), int(item2[1]), int(item2[2]))
	return dt


def push_flight_data(source_db_name,source_sql_table_name,dest_db_name,flight_info_sql_table,flight_ticket_info_sql_table):
	flight_day_info_fuse_dic = fuse_flight_data(source_db_name,source_sql_table_name)	
	
	try:
		rds = redis.Redis(host='127.0.0.1', port=6379, db=0)

		conn = MySQLdb.connect(host='127.0.0.1', user='', charset='utf8',passwd='', db=source_db_name)
		cursor = conn.cursor()
	
	except Exception, e:
		_INFO('push flight data',['redis or mysql connection error'])
		_INFO('push flight data',['error code = ' + str(e)])
		return None,None


	sql = "select flight_no,plane_type,flight_corp,dept_id,dest_id,dept_day,dept_time,dest_time,dur,rest,price,tax,surcharge,currency,seat_type,real_class,stop_id,stop_time,daydiff,source,return_rule,stop,updatetime from " + source_sql_table_name + " ;"
	
	#print 'sql: ' + sql
	
	_INFO('push flight data',['get flight data from database...'])
	
	try:
		n = cursor.execute(sql)
		datas = cursor.fetchall()
	
	except Exception, e:
		_INFO('push flight data',['Error','execute sql error!','sql = ' + str(sql)])
		sys.exit(1)

	cursor.close()
	conn.close()
	
	_INFO('push flight data',['get flight data from sql database done!'])

	_INFO('push flight data',['get available data...'])
	flight_data = {}
	flight_key_set = set()
	
	fusedNum = 0
	for data in datas:
		#print data
		dept_id = data[3].encode('utf-8').strip()
		dest_id = data[4].encode('utf-8').strip()
		dept_day = data[5].encode('utf-8').strip().replace('-','')
		source = data[19].encode('utf-8').strip().split('::')[-1]
		update_time = str(data[22]).strip()

		flight_key = 'flight_' + dept_id + '_' + dest_id + '_' + dept_day + '_' + source

		#print 'flight_key: ' + flight_key
		
		cur_span = -10000
		if flight_key not in flight_key_set:
			flight_data[flight_key] = []
			flight_data[flight_key].append(update_time)
			flight_key_set.add(flight_key)
			cur_span = 0

		if cur_span != 0:
			cur_up_dt = str2datetime(update_time)

			ori_update_time = flight_data[flight_key][0]
			ori_up_dt = str2datetime(ori_update_time)

			if type(cur_up_dt).__name__ != 'datetime' or type(ori_up_dt).__name__ != 'datetime':
				print 'filter\tupdate_time_error_' + source + "\tcur_up_dt=" + update_time+"\tori_up_dt=" + ori_update_time
				continue

			cur_span = (cur_up_dt - ori_up_dt).seconds

		if cur_span < -10:
			print 'Filter by low span! key=' + flight_key + " update_time=" + update_time + " ori_update_time=" + ori_update_time
			continue

		elif cur_span > 10:
			print "Filter by newest key!"
			flight_data[flight_key] = []
			flight_data[flight_key].append(update_time)
			flight_data[flight_key].append(data)

		else:
			flight_data[flight_key].append(data)
			if cur_span > 0:
				flight_data[flight_key][0] = update_time

	_INFO('push flight data',['get available data done!'])

	conn = MySQLdb.connect(host='127.0.0.1', user='', charset='utf8',passwd='', db=dest_db_name)
	cursor = conn.cursor()
	cursor.execute("SET NAMES 'utf8'")	
	flight_redis = {}
	flight_ticket_redis = {}

	for flight_key in flight_data:
		if len(flight_data[flight_key]) <= 1:
			continue

		update_time = flight_data[flight_key][0]

		#print 'up_time: ' + update_time

		for idx in range(1,len(flight_data[flight_key])):
			data = flight_data[flight_key][idx]
			
			#!!!!!may change here
			if len(data) != 23:
				print 'filter\tdata_size_error\tdata_len=' + str(len(data))
				continue
			
			ticket_no = data[0].encode('utf-8').strip()
			flight_count = ticket_no.count('_') + 1
			
			source = data[19].encode('utf-8').strip().split('::')[-1]
			
			plane_type = data[1].encode('utf-8').strip()
			flight_corp = data[2].encode('utf-8').strip()
			dept_id = data[3].encode('utf-8').strip()
			dest_id = data[4].encode('utf-8').strip()
			
			ori_dept_day = data[5].encode('utf-8').strip()
			dept_day = data[5].encode('utf-8').strip().replace('-','')
			dept_time = data[6].encode('utf-8').strip().replace('-','').replace('T',' ')
			dest_time = data[7].encode('utf-8').strip().replace('-','').replace('T',' ')
			dur = str(data[8]).strip()
			rest = data[9]
			price = data[10]
			if abs(price + 10) < 0.1:
				pattern = "flight_" + dept_id + "_" + dest_id + "_" + dept_day + "*"
				delKeys = rds.keys(pattern)

				for key in delKeys:
					rds.delete(key)
				
				continue
			elif price < 0:
				print 'filter\tprice_error_' + source
				continue

			tax = data[11]
			surcharge = data[12]
			currency = data[13].encode('utf-8').strip()
			seat_type = data[14].encode('utf-8').strip()
			real_class = data[15].encode('utf-8').strip()

			if 'NULL' == real_class:
				real_class = '_'.join(['NULL' for i in range(flight_count)])
			
			stop_id = data[16].encode('utf-8').strip()
			stop_time = data[17].encode('utf-8').strip().replace('-','').replace('T',' ')
			daydiff = data[18].encode('utf-8').strip()
			
			#using fused data
			flight_day_info_fuse_key = ticket_no + '\t' + dept_id + '\t' + dest_id + '\t' + dept_day

			if flight_day_info_fuse_key in flight_day_info_fuse_dic:
				fusedNum += 1
				stop_id = flight_day_info_fuse_dic[flight_day_info_fuse_key]['stop_id']
				stop_time = flight_day_info_fuse_dic[flight_day_info_fuse_key]['stop_time'].strip().replace('-','').replace('T',' ')
				plane_type = flight_day_info_fuse_dic[flight_day_info_fuse_key]['plane_type']
				flight_corp = flight_day_info_fuse_dic[flight_day_info_fuse_key]['flight_corp']
				daydiff = flight_day_info_fuse_dic[flight_day_info_fuse_key]['daydiff']
			#using fused data done!

			return_rule = data[20].encode('utf-8').strip().replace("'",'"')
			stop = data[21]
			up_time = str(data[22]).strip()

			if not (ticket_no.count('_') == plane_type.count('_') == flight_corp.count('_') \
					== stop_id.count('|') == stop_time.count('|') == seat_type.count('_') \
					== real_class.count('_') == daydiff.count('_')):
				#print 'ticket_no: ' + ticket_no 
				#print 'plane_type: ' + plane_type
				#print 'flight_corp: ' + flight_corp
				#print 'stop_id: ' + stop_id
				#print 'stop_time: ' + stop_time
				#print 'seat_type: ' + seat_type
				#print 'real_class: ' + real_class 
				#print 'daydiff: ' + daydiff
				#
				print 'filter\tdata_count_error_' + source
				continue
			
			flight_redis_key = 'flight_' + dept_id + '_' + dest_id + '_' + dept_day + '_' + source

			if flight_redis_key not in flight_redis:
				flight_redis[flight_redis_key] = []
				flight_redis[flight_redis_key].append(update_time)
			
			md5Str = seat_type + '$' + real_class + '$' + ticket_no + '$' + dept_id + '$' + dest_id
			flight_ticket_md5 = 'flightTicket#' + getStrMd5(md5Str)

			flight_redis_value = str(price) + '\t' + str(tax) + '\t' + str(surcharge) + '\t' + currency + '\t' + flight_ticket_md5
			
			if flight_redis_value not in flight_redis[flight_redis_key]:
				flight_redis[flight_redis_key].append(flight_redis_value)

			ticket_stop_id_vec = stop_id.strip().split('|')
			ticket_stop_id = 'NULL'
			error = False
			for index in range(0,len(ticket_stop_id_vec)-1):
				tmpList = ticket_stop_id_vec[index].strip().split('_')
				if len(tmpList) != 2:
					#_INFO('push flight data',['Warning','stop_id error! data = ' + str(data)])
					error = True
					break
				
				if ticket_stop_id == 'NULL':
					ticket_stop_id = tmpList[1]
				else:
					ticket_stop_id += '_' + tmpList[1]

			if error:
				print 'filter\tstop_id_error_' + source
				continue
			
			try:
				selectsql = "select * from " + flight_ticket_info_sql_table +" where flight_ticket_md5 ='" + flight_ticket_md5 + "';"
				q = cursor.execute(selectsql)
				resultDatas = cursor.fetchall()

				if len(resultDatas) == 0:
					#flight_ticket info for latest one day
					flight_ticket_info_value = seat_type + '\t' + real_class + '\t' + ticket_no + '\t' + ticket_stop_id + '\t' + dept_id + '\t' + dest_id + '\t' + update_time + '\t' + str(stop) + '\t' + return_rule + '\t' + str(rest)
					
					flight_ticket_sql = "replace into " + flight_ticket_info_sql_table + " (flight_ticket_md5, seat_type,real_class,ticket_no,stop_id,dept_id,dest_id,update_time,stop,return_rule,rest) values ('"  + flight_ticket_md5 + "','" + seat_type + "','" + real_class + "','" + ticket_no + "','" + ticket_stop_id + "','" + dept_id + "','" + dest_id + "','" + update_time + "','" + str(stop) + "','" + return_rule + "','" + str(rest) + "');"

					
					try:
						#print 'flight_ticket_sql: ' +  flight_ticket_sql
						cursor.execute(flight_ticket_sql)
						
						#print 'flight_ticket_key: ' + flight_ticket_md5
						#print 'flight_ticket_value: ' +  flight_ticket_info_value
						flight_ticket_redis[flight_ticket_md5] = flight_ticket_info_value
						
					except Exception,e:
						_ERROR('excute sql fail',['Error','sql_len='+str(len(flight_ticket_sql)),'sql='+flight_ticket_sql])
						_ERROR('excute sql fail!',['error code: ' + str(e)])
						continue
			except Exception ,e:
				_INFO('push flight data',['Error',['execute sql error! sql = ' + selectsql]])
				_INFO('push flight data',['Error',['error: ' + str(e)]])
				continue

			flight_no_vec = ticket_no.strip().split('_')
			plane_type_vec = plane_type.strip().split('_')
			flight_corp_vec = flight_corp.strip().split('_')
			stop_id_vec = stop_id.strip().split('|')
			stop_time_vec = stop_time.strip().split('|')
			daydiff_vec = daydiff.strip().split('_')

			flightInfo_sql = "replace into " + flight_info_sql_table + " (flight_info_key,flight_no,plane_type,flight_corp,dept_id,dest_id,dept_time,dest_time,cost,daydiff) values "

			values = ''

			for i in range(0,len(flight_no_vec)):
				flightNo = flight_no_vec[i]
				planeType = plane_type_vec[i]
				flightCorp = flight_corp_vec[i]
				
				stopId = stop_id_vec[i]
				
				stopId_list = stopId.strip().split('_')
				if len(stopId_list) != 2:
					print 'filter\tstop_id_error_source_' + source
					continue
					
				deptId = stopId_list[0].strip()
				destId = stopId_list[1].strip()

				stopTime = stop_time_vec[i]
					
				stopTime_list = stopTime.strip().split('_')
				if 2 != len(stopTime_list):
					print 'filter\tstop_time_error_' + source
					continue

				deptTime = stopTime_list[0].strip()
				destTime = stopTime_list[1].strip()

				deptTime_list = deptTime.strip().split(' ')
				if len(deptTime_list) != 2:
					print 'filter\tstop_time_error_' + source
					continue

				deptDay = deptTime_list[0]
				deptTime = deptTime.replace(' ','_')
				destTime = destTime.replace(' ','_')

				dayDiff = daydiff_vec[i]


				flight_info_key = flightNo + '_' + deptId + '_' + destId + '_' + deptDay

				getsql = "select * from " + flight_info_sql_table + " where flight_info_key='" + flight_info_key + "';"
				p = cursor.execute(getsql)
				tmpData = cursor.fetchall()

				if len(tmpData) == 0:
					cost = durCal(deptTime,destTime,deptId,destId)
					tmpValue = "('" + flight_info_key + "','" + flightNo + "','" + planeType + "','" + flightCorp \
							+ "','" + deptId + "','" + destId + "','" + deptTime + "','" + destTime + "','" \
							+ str(cost) + "','" + dayDiff + "') "

					if values == '':
						values = tmpValue
					else:
						values += " , " + tmpValue
			
			if values != '':
				try:
					flightInfo_sql += values + ";"
					#print  'flightInfo_sql: ' + flightInfo_sql
					cursor.execute(flightInfo_sql)

				except Exception, e:
					_ERROR('exceute tran info sql fail',['SQL fail sql_len=' +  str(flightInfo_sql)])
					_ERROR('exceute tran info sql fail',[str(e)])
					continue


	conn.commit()
	cursor.close()
	conn.close()
	print 'fusedNum:' + str(fusedNum)
	return flight_redis,flight_ticket_redis


Usage = 'python xx.py tmp_db_name tmp_table_name flight_info_table flight_ticket_infotable'
if __name__ == '__main__':
	if len(sys.argv) != 6:
		print Usage
		sys.exit(-1)
	
	#forex_rate_dic = loadForexInfo()

	tmp_db_name = sys.argv[1]
	tmp_table_name = sys.argv[2]
	dest_db_name = sys.argv[3]
	flight_info_sql_table = sys.argv[4]
	flight_ticket_info_sql_table = sys.argv[5]

	try:
		cache = redis.Redis(host='127.0.0.1', port=6379, db=0)
		pipeline = cache.pipeline()
	
	except Exception , e:
		_ERROR('Init Redis', ['Failed, error = ' + str(e.code)])
		sys.exit(-1)

	flight_redis,flight_ticket_redis = push_flight_data(tmp_db_name,tmp_table_name,dest_db_name,flight_info_sql_table,flight_ticket_info_sql_table)

	_INFO('flight_num', ['flight_num = ' + str(len(flight_redis))])
	_INFO('flight_ticket_num',['flight_ticket_num = ' + str(len(flight_ticket_redis))])
	

	_INFO('push flight data',['begin push flight data to redis...'])

	num = 0
	data_len = 0

	for flight_key in flight_redis:
		if len(flight_redis[flight_key]) <= 1:
			continue

		flight_value = '\n'.join(flight_redis[flight_key])
		data_len += len(flight_value)

		try:
			cache.set(flight_key,flight_value)
			print 'update flight info\t' + flight_key
			num += 1

		except Exception ,e:
			_ERROR('Redis Caching Error', ['key = ' + flight_key, 'value.length = ' + str(len(flight_value))])
			_ERROR('Redis Caching Error', ['error code: ' + str(e)])
			continue


		if num % 30 == 0:
			try:
				pipeline.execute()
				_INFO('Redis', ['Cached' + str(num) + 'th data', 'datalen = ' + str(data_len)])
				data_len = 0

			except Exception, e:
				_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
				continue

	try:
		pipeline.execute()
		_INFO('finished put flight data to redis', ['Cached ' + str(num) + 'th data', 'datalen = ' + str(data_len)])
	
	except Exception, e:
		_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
		pass

	_INFO('push flight data',['push flight info data to redis done!'])
	
	sys.exit(1)

	_INFO('push flight data',['begin push flight ticket data to redis...'])

	num = 0
	data_len = 0

	for flight_ticket_key in flight_ticket_redis:
		flight_ticket_value = flight_ticket_redis[flight_ticket_key]

		#print 'key:' + flight_ticket_key
		#print 'value: ' + flight_ticket_value

		try:
			cache.set(flight_ticket_key,flight_ticket_value)
			print 'update flight ticket info\t' + flight_ticket_key
			num += 1
			data_len += len(flight_ticket_value)

		except Exception ,e :
			_ERROR('Redis Caching Error', ['key = ' + flight_ticket_key, 'value.length = ' + str(len(flight_ticket_value))])
			_ERROR('Redis Caching Error', ['error code: ' + str(e)])
			continue

		if num % 30 == 0:
			try:
				pipeline.execute()
				_INFO('Redis', ['Cached' + str(num) + 'th data', 'datalen = ' + str(data_len)])
				data_len = 0

			except Exception ,e:
				_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
				continue

	try:
		pipeline.execute()
		_INFO('finished push flight ticket data', ['Cached ' + str(num) + 'th data', 'datalen = ' + str(data_len)])

	except Exception , e:
		_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
		pass
	
	sys.stdout.flush()

	_INFO('Redis', ['Finished Caching'])

