#encoding=utf-8

import redis
import MySQLdb
import time
import datetime
import sys
import hashlib

from LOG import _ERROR, _INFO
from calCost_train import durCal

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

#s:20140809 12:24:12
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


def push_train_data(source_db_name,source_sql_table_name,dest_db_name,train_info_sql_table,train_ticket_info_sql_table):
	conn = MySQLdb.connect(host='127.0.0.1', user='', charset='utf8',passwd='', db=source_db_name)
	cursor = conn.cursor()

	sql = "select train_no,train_type,train_corp,dept_city,dept_id,dest_city,dest_id,dept_day,dept_time,dest_time,dur,price,tax,currency,seat_type,real_class,source,return_rule,stopid,stoptime,daydiff,stop,update_time from " + source_sql_table_name + " ;"
	
	#print 'sql: ' + sql
	
	_INFO('push train data',['get train data from database...'])
	
	try:
		n = cursor.execute(sql)
		datas = cursor.fetchall()
	
	except Exception, e:
		_INFO('push train data',['Error','execute sql error!'])
		sys.exit(1)

	cursor.close()
	conn.close()
	
	_INFO('push train data',['get train data from sql database done!'])

	_INFO('push train data',['get available data...'])
	train_data = {}
	train_key_set = set()

	for data in datas:
		#print data
		dept_id = data[4].encode('utf-8').strip()
		dest_id = data[6].encode('utf-8').strip()
		dept_day = data[7].encode('utf-8').strip().replace('-','')
		source = data[16].encode('utf-8').strip()
		update_time = str(data[22]).strip()

		train_key = 'train_' + dept_id + '_' + dest_id + '_' + dept_day + '_' + source

		#print 'train_key: ' + train_key
		
		cur_span = -10000
		if train_key not in train_key_set:
			train_data[train_key] = []
			train_data[train_key].append(update_time)
			train_key_set.add(train_key)
			cur_span = 0

		if cur_span != 0:
			cur_up_dt = str2datetime(update_time)

			ori_update_time = train_data[train_key][0]
			ori_up_dt = str2datetime(ori_update_time)

			if type(cur_up_dt).__name__ != 'datetime' or type(ori_up_dt).__name__ != 'datetime':
				print 'filter\tupdate_time_error_' + source
				#_INFO('push_train_data',['Error','cur_update='+update_time,'ori_update_time='+ori_update_time])
				continue

			cur_span = (cur_up_dt - ori_up_dt).seconds

		if cur_span < -10:
			print 'Filter by low span! key=' + train_key + " update_time=" + update_time + " ori_update_time=" + ori_update_time
			continue

		elif cur_span > 10:
			print "Filter by newest key!"
			train_data[train_key] = []
			train_data[train_key].append(update_time)
			train_data[train_key].append(data)

		else:
			train_data[train_key].append(data)
			if cur_span > 0:
				train_data[train_key][0] = update_time

	_INFO('push train data',['get available data done!'])

	conn = MySQLdb.connect(host='127.0.0.1', user='', charset='utf8',passwd='', db=dest_db_name)
	cursor = conn.cursor()
	
	train_redis = {}
	train_ticket_redis = {}

	for train_key in train_data:
		if len(train_data[train_key]) <= 1:
			continue

		update_time = train_data[train_key][0]

		#print 'up_time: ' + update_time

		for idx in range(1,len(train_data[train_key])):
			data = train_data[train_key][idx]
			
			#!!!!!may change here
			if len(data) != 23:
				print 'filter\tdata_size_error'
				#_INFO('push train data',['data len error! data = '+str(data)])
				continue
			
			ticket_no = data[0].encode('utf-8').strip()
			train_count = ticket_no.count('_') + 1
			
			train_type = data[1].encode('utf-8').strip()
			if 'NULL' == train_type:
				train_type = '_'.join(['NULL' for i in range(train_count)])

			train_corp = data[2].encode('utf-8').strip()
			dept_city = data[3].encode('utf-8').strip()
			dept_id = data[4].encode('utf-8').strip()
			dest_city = data[5].encode('utf-8').strip()
			dest_id = data[6].encode('utf-8').strip()
			dept_day = data[7].encode('utf-8').strip().replace('-','')
			dept_time = data[8].encode('utf-8').strip().replace('-','')
			dest_time = data[9].encode('utf-8').strip().replace('-','')
			dur = str(data[10]).strip()
			source = data[16].encode('utf-8').strip()
			
			price = data[11]
			if abs(price + 10) < 0.1:
				pattern = 'train_' + dept_id + '_' + dest_id + '_' + dept_day + '_*'
				rds = redis.Redis(host='127.0.0.1', port=6379, db=0)
				deleKey = rds.keys(pattern)
				for key in deleKey:
					rds.delete(key)

			elif price < 0:
				print 'filter\tprice_error_' + source
				#_INFO('push train data',['Warning','price is err! data = ' + str(data)])
				continue

			tax = data[12]
			currency = data[13].encode('utf-8').strip()
			seat_type = data[14].encode('utf-8').strip()
			real_class = data[15].encode('utf-8').strip()

			if 'NULL' == real_class:
				real_class = '_'.join(['NULL' for i in range(train_count)])

			return_rule = data[17].encode('utf-8').strip().replace("'",'"')
			stop_id = data[18].encode('utf-8').strip()
			stop_time = data[19].encode('utf-8').strip().replace('-','')
			daydiff = data[20].encode('utf-8').strip()
			stop = data[21]
			up_time = str(data[22]).strip()

			if 'NULL' in stop_id:
				print 'filter\tstop_id_error_' + source
				continue

			if 'NULL' in stop_time:
				print 'filter\tstop_time_error_' + source
				continue
			
			if not (ticket_no.count('_') == train_type.count('_') == train_corp.count('_') \
					== stop_id.count('|') == stop_time.count('|') == seat_type.count('_') \
					== real_class.count('_') == daydiff.count('_')):
				print 'filter\tdata_count_error_' + source
				#_INFO('push train data',['Error','data count is not same! data=' +  str(data)])
				continue
			
			train_redis_key = 'train_' + dept_id + '_' + dest_id + '_' + dept_day + '_' + source

			if train_redis_key not in train_redis:
				train_redis[train_redis_key] = []
				train_redis[train_redis_key].append(update_time)
			
			md5Str = seat_type + '$' + real_class + '$' + ticket_no + '$' + dept_id + '$' + dest_id
			train_ticket_md5 = 'trainTicket#' + getStrMd5(md5Str)

			train_redis_value = str(price) + '\t' + str(tax) + '\t' + currency + '\t' + train_ticket_md5
			

			ticket_stop_id_vec = stop_id.strip().split('|')
			ticket_stop_id = ''
			error = False

			for index in range(0,len(ticket_stop_id_vec)-1):
				tmpList = ticket_stop_id_vec[index].strip().split('_')

				if len(tmpList) != 2:
					print 'filter\tstop_id_error_' + source
					#_INFO('push train data',['stop_id error! data = ' + str(data)])
					error = True
					break
				
				if ticket_stop_id == '':
					ticket_stop_id = tmpList[1]
				else:
					ticket_stop_id += '_' + tmpList[1]

			if error:
				continue

			#train_ticket info for latest one day
			train_ticket_info_value = seat_type + '\t' + real_class + '\t' + ticket_no + '\t' + ticket_stop_id + '\t' + dept_id + '\t' + dest_id + '\t' + update_time + '\t' + return_rule + '\t' + str(stop)
			

			try:
				selectsql = "select * from " + train_ticket_info_sql_table + " where train_ticket_md5 = '" + train_ticket_md5 + "';"
				q = cursor.execute(selectsql)
				resultData = cursor.fetchall()

				if len(resultData) == 0:
					train_ticket_sql = "replace into " + train_ticket_info_sql_table + " (train_ticket_md5, seat_type,real_class,ticket_no,stop_id,dept_id,dest_id,update_time,return_rule,stop) values ('"  + train_ticket_md5 + "','" + seat_type + "','" + real_class + "','" + ticket_no + "','" + ticket_stop_id + "','" + dept_id + "','" + dest_id + "','" + update_time + "','" + return_rule + "','" + str(stop) + "');"

					
					try:
						#print 'train_ticket_sql: ' +  train_ticket_sql
						cursor.execute(train_ticket_sql)
						#print 'train_ticket_key: ' + train_ticket_md5
						#pri:nt 'train_ticket_value: ' +  train_ticket_info_value
						train_ticket_redis[train_ticket_md5] = train_ticket_info_value
						
					except Exception,e:
						_ERROR('excute sql fail',['Error','sql_len='+str(len(train_ticket_sql)),'sql='+train_ticket_sql])
						continue
				#update update_time
				else:
					try:
						upsql = "update " + train_ticket_info_sql_table + " set update_time='" + update_time + "' where train_ticket_md5 = '" + train_ticket_md5 + "';"
						cursor.execute(upsql)
						_INFO('update train ticket update_time',['train_ticket_md5=' + train_ticket_md5])
					except Exception, e:
						_ERROR('update update_time fail',['error code=' + str(e)])
						continue


			except Exception ,e:
				_INFO('push train data',['Error in sql! sql=' + selectsql])
				_INFO('push train data',['Error code: ' + str(e)])
				continue

			train_no_vec = ticket_no.strip().split('_')
			train_type_vec = train_type.strip().split('_')
			train_corp_vec = train_corp.strip().split('_')
			stop_id_vec = stop_id.strip().split('|')
			stop_time_vec = stop_time.strip().split('|')
			daydiff_vec = daydiff.strip().split('_')

			trainInfo_sql = "replace into " + train_info_sql_table + " (train_info_key,train_no,train_type,train_corp,dept_id,dest_id,dept_time,dest_time,cost,daydiff) values "

			values = ''
			info_error = False

			for i in range(0,len(train_no_vec)):
				trainNo = train_no_vec[i]
				trainType = train_type_vec[i]
				trainCorp = train_corp_vec[i]
				stopId = stop_id_vec[i]

				stopId_list = stopId.strip().split('_')
				if len(stopId_list) != 2:
					print 'filter\tstop_id_error_' + source
					info_error = True
					break
					
				deptId = stopId_list[0]
				destId = stopId_list[1]

				stopTime = stop_time_vec[i]
					
				stopTime_list = stopTime.strip().split('_')
				if 2 != len(stopTime_list):
					print 'filter\tstop_time_error_' + source
					info_error = True
					break

				deptTime = stopTime_list[0].strip()
				destTime = stopTime_list[1].strip()

				deptTime_list = deptTime.strip().split(' ')
				if len(deptTime_list) != 2:
					print 'filter\tstop_time_error_' + source
					info_error = True
					break

				deptDay = deptTime_list[0]
				deptTime = deptTime.replace(' ','_')
				destTime = destTime.replace(' ','_')
				
				dayDiff = daydiff_vec[i]


				train_info_key = trainNo + '_' + deptId + '_' + destId + '_' + deptDay

				getsql = "select * from " + train_info_sql_table + " where train_info_key='" + train_info_key + "';"
				cursor.execute(getsql)

				tmpData = cursor.fetchall()
				
				if len(tmpData) > 0:
					oldCost = tmpData[0][0]
				
				if len(tmpData) == 0 or oldCost < 0:
					cost = durCal(deptTime,destTime,deptId,destId)

					tmpValue = "('" + train_info_key + "','" + trainNo + "','" + trainType + "','" + trainCorp \
							+ "','" + deptId + "','" + destId + "','" + deptTime + "','" + destTime + "','" \
							+ str(cost) + "','" + dayDiff + "') "

					if values == '':
						values = tmpValue
					else:
						values += " , " + tmpValue
			
			if not info_error and values != '':
				try:
					trainInfo_sql += values + ";"
					#print  'trainInfo_sql: ' + trainInfo_sql
					cursor.execute(trainInfo_sql)

				except Exception, e:
					_ERROR('exceute tran info sql fail',['SQL fail sql_len=' +  str(trainInfo_sql)])
					_ERROR('exceute tran info sql fail',[str(e)])
					continue

			if not info_error and train_redis_value not in train_redis[train_redis_key]:
				train_redis[train_redis_key].append(train_redis_value)

	conn.commit()
	cursor.close()
	conn.close()

	return train_redis,train_ticket_redis


Usage = 'python xx.py tmp_db_name tmp_table_name train_info_table train_ticket_infotable'
if __name__ == '__main__':
	if len(sys.argv) != 6:
		print Usage
		sys.exit(-1)
	
	#forex_rate_dic = loadForexInfo()

	tmp_db_name = sys.argv[1]
	tmp_table_name = sys.argv[2]
	dest_db_name = sys.argv[3]
	train_info_sql_table = sys.argv[4]
	train_ticket_info_sql_table = sys.argv[5]

	try:
		cache = redis.Redis(host='127.0.0.1', port=6379, db=0)
		pipeline = cache.pipeline()
	
	except Exception , e:
		_ERROR('Init Redis', ['Failed, error = ' + str(e.code)])
		sys.exit(-1)

	train_redis,train_ticket_redis = push_train_data(tmp_db_name,tmp_table_name,dest_db_name,train_info_sql_table,train_ticket_info_sql_table)
	
	_INFO('train_num', ['train_num = ' + str(len(train_redis))])
	_INFO('train_ticket_num',['train_ticket_num = ' + str(len(train_ticket_redis))])

	_INFO('push train data',['begin push train data to redis...'])

	num = 0
	data_len = 0

	for train_key in train_redis:
		if len(train_redis[train_key]) <= 1:
			continue

		train_value = '\n'.join(train_redis[train_key])
		data_len += len(train_value)

		try:
			cache.set(train_key,train_value)
			print 'update train info\t' + train_key
			num += 1

		except Exception ,e:
			_ERROR('Redis Caching Error', ['key = ' + train_key, 'value.length = ' + str(len(train_value))])
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
		_INFO('finished put train data to redis', ['Cached ' + str(num) + 'th data', 'datalen = ' + str(data_len)])
	
	except Exception, e:
		_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
		pass

	_INFO('push train data',['push train info data to redis done!'])
	
	sys.exit(1)

	_INFO('push train data',['begin push train ticket data to redis...'])

	num = 0
	data_len = 0

	for train_ticket_key in train_ticket_redis:
		train_ticket_value = train_ticket_redis[train_ticket_key]

		#print 'key:' + train_ticket_key
		#print 'value: ' + train_ticket_value

		try:
			cache.set(train_ticket_key,train_ticket_value)
			print 'update train ticket info\t' + train_ticket_key
			num += 1
			data_len += len(train_ticket_value)

		except Exception ,e :
			_ERROR('Redis Caching Error', ['key = ' + train_ticket_key, 'value.length = ' + str(len(train_ticket_value))])
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
		_INFO('finished push train ticket data', ['Cached ' + str(num) + 'th data', 'datalen = ' + str(data_len)])

	except Exception , e:
		_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
		pass
	
	sys.stdout.flush()

	_INFO('Redis', ['Finished Caching'])

