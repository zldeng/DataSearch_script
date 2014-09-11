#--coding:utf-8--

import redis
import MySQLdb
import time
import datetime
import sys
import json
#sys.path.append('/home/workspace/lurong/pylib')
from LOG import _ERROR, _INFO
from roomTypeNormalize import normalizeRoomType 


def index_format(v):
	if type(v) is int or type(v) is float or type(v) is long:
		return str(v)
	if type(v) is str or type(v) is unicode:
		return v.replace("\t","").replace("\n","")

def loadForexInfo():
	forex_rate_dict = {}
	
	conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db='onlinedb')
	cursor = conn.cursor()
	sql = 'select currency_code, rate from exchange;'
	n = cursor.execute(sql)
	datas = cursor.fetchall()
	cursor.close()
	conn.close()

	for data in datas:
		forex = data[0].encode('utf-8').strip()
		rate = data[1]
		forex_rate_dict[forex] = rate
      
	_INFO('loadForexInfo', ['forex_rate_dict.size = ' + str(len(forex_rate_dict))])
	return forex_rate_dict

def loadOpenedHotelSource():
	openedSource = set()
	conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db='onlinedb')
	cursor = conn.cursor()
	sql = " select name from source where status='Open' and  type='hotel';"
	n = cursor.execute(sql)
	datas = cursor.fetchall()
	cursor.close()
	conn.close()

	for data in datas:
		source = data[0].encode('utf-8').strip()
		openedSource.add(source)

	_INFO('loadOpenedHotelSource',['opened source size:' + str(len(openedSource))])
	return openedSource
   
def loadCandidateHotel():
	hotelSet = set()
	conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db='onlinedb')
	cursor = conn.cursor()
	sql = " select H.uid from hotel H, city C where H.city_mid=C.id and C.status='Open' "

	n = cursor.execute(sql)
	datas = cursor.fetchall()

	for data in datas:
		hid = data[0].encode('utf-8').strip()
		hotelSet.add(hid)

	_INFO('load candidate hotel',['available hotel size = ' + str(len(hotelSet))])
	return hotelSet

def loadHidUidInfo():
	sid_uid_dict = {}
	conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db='onlinedb')
	cursor = conn.cursor()
	sql = "select source, sid, uid from hotel_unid where status='Open';"
	n = cursor.execute(sql)
	datas = cursor.fetchall()
	cursor.close()
	conn.close()

	for data in datas:
		source = data[0].encode('utf-8').strip()
		sid = data[1].encode('utf-8').strip()
		uid = data[2].encode('utf-8').strip()

		sid_uid_dict[source + '_' + sid] = uid

	_INFO('loadHidUidInfo', ['sid_uid_dict.size = ' + str(len(sid_uid_dict))])
	return sid_uid_dict


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


#def getNewestPrice(cname_cid_dict, forex_rate_dict, sid_udi_dict, db_name, table_name, city, sc,opened_source_set):
def getNewestPrice(candHotelSet, forex_rate_dict, sid_udi_dict, db_name, table_name, city, sc,opened_source_set):
	_INFO('getNewestPrice', ['Begin'])
	
	try:
		rds = redis.Redis(host='127.0.0.1', port=6379, db=0)
		conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db=db_name)
		cursor = conn.cursor()
	
	except Exception,e :
		_INFO('getNewestPrice',['redis or mysql connection fail!'])
		_INFO('getNewestPrice',['error code = ' + str(e)])
		return None

	sql = 'select hotel_name, city, source, source_hotelid, source_roomid, real_source, room_type, occupancy, \
			bed_type, size, floor, check_in, check_out, price, tax, currency, is_extrabed, is_extrabed_free, \
			has_breakfast, is_breakfast_free, is_cancel_free, room_desc, update_time from ' + table_name

    
	if (len(city) > 0 and city != 'NULL') and (len(sc) > 0 and sc != 'NULL'):
		sql += ' where city = "' + city  +'" and source = "' + sc + '" ;'
	elif (len(city) > 0 and city != 'NULL') and (len(sc) <= 0 or sc == 'NULL'):
		sql += ' where city = "' + city  +'";'
	elif (len(city) <= 0 or city == 'NULL') and (len(sc) > 0 and sc != 'NULL'):
		sql += ' where source = "' + sc + '" ;'
	else:
		sql += ';'


	n = cursor.execute(sql)
	datas = cursor.fetchall()

	cursor.close()
	conn.close()

	key_roominfo_dict = {}
	key_set = set([])

	if len(datas) == 0:
		_INFO('getNewestPrice', ['city = ' + city + ', sc = ' + sc + ', no result'])
		return {}


	sid_set = set(sid_udi_dict.keys())

	c = 0
	for data in datas:
		c += 1
		if c == 1 or c % 10000 == 0:
			_INFO('getNewestPrice', ['c = ' + str(c)])

		info = {}

		source = data[2].encode('utf-8').strip()	#source
		real_source = data[5].encode('utf-8').strip()        #real_source
		
		hid = real_source + '_' + data[3].encode('utf-8').strip()
		if hid not in sid_set:
			print "filter\tnot_in_sid_set_" + source + "\thsid=" + hid
			continue
		
		uid = sid_uid_dict[hid]
		if uid not in candHotelSet:
			print 'filter\tnot_in_candHotelSet_' + source + "\thid=" + uid
			continue

		info['rid'] = data[4].encode('utf-8').strip()       #source_roomid


		if (real_source not in opened_source_set):
			print 'filter\tnot_in_openedSourc_' + source + '\treal_source=' + real_source
			continue
		
		info['rs'] = real_source

		ori_rt = data[6].encode('utf-8').strip()

		info['ori_rt'] = ori_rt
		try:
			normalized_rt = normalizeRoomType(ori_rt)
		except Exception ,e:
			_ERROR('normalize room type',['Error normalize roomType=' + ori_rt])
			normalized_rt = ori_rt
			pass

		info['rt'] = normalized_rt        #room_type 

		info['occu'] = data[7]                              #occupancy
		info['bt'] = data[8].encode('utf-8').strip()        #bed_type
		info['size'] = data[9]                              #size
		info['floor'] = data[10]                            #floor
		
		# check_in
		check_in = data[11].encode('utf-8').strip()
		check_in_vec = check_in.split('-')
		if len(check_in_vec) != 3:
			print "filter\tcheck_in_not_format_" + source + "\tcheck_in="+check_in
			continue
		try:
			check_in_dt = datetime.date(int(check_in_vec[0]), int(check_in_vec[1]), int(check_in_vec[2]))
		except Exception, e:
			print "filter\tcheck_in_not_forma_" + source + "\tcheck_in=" + check_in
			continue

		info['ci'] = check_in_vec[0] + check_in_vec[1] + check_in_vec[2]

		# check_out
		check_out = data[12].encode('utf-8').strip()
		check_out_vec = check_out.split('-')
		
		if len(check_out_vec) != 3:
			print "filter\tcheck_out_not_format_" + source + "\tcheck_out=" + check_out
			continue
		try:
			check_out_dt = datetime.date(int(check_out_vec[0]), int(check_out_vec[1]), int(check_out_vec[2]))
		
		except Exception, e:
			print "filter\tcheck_out_not_format_" + source + "\tcheck_out=" + check_out
			continue
		
		info['co'] = check_out_vec[0] + check_out_vec[1] + check_out_vec[2]

		# dur
		dur = (check_out_dt - check_in_dt).days
		#dur = 1

		price = data[13]
		if abs(price + 10) < 0.1:
			patterm = uid + "_" + "*" + "_" + info['ci'] + "_*"

			deleKey = rds.keys(patterm)
			for key in deleKey:
				rds.delete(key)
			continue

		elif price < 0:
			print "filter\tprice_error_" + source + "\tprice="+str(price)
			continue

		tax = data[14]
		crcy = data[15].encode('utf-8').strip()
		if crcy not in forex_rate_dict.keys():
			print "filter\tcrcy_not_in_forex_rate_dict_" + source + "\tcurrency=" + crcy
			continue
		if tax > 0:
			price += tax

		info['price'] = int(price * forex_rate_dict[crcy])              #price
		
		info['i_e'] = data[16].encode('utf-8').strip()          #is_extrabed
		
		if info['i_e'] == 'NULL':
			info['i_e'] = 'No'

		info['i_e_f'] = data[17].encode('utf-8').strip()     #is_extrabed_free
		if info['i_e_f'] == 'NULL':
			info['i_e_f'] = 'No'

		info['h_b'] = data[18].encode('utf-8').strip()        #has_breakfast
		if info['h_b'] == 'NULL':
			info['h_b'] = 'No'

		info['i_b_f'] = data[19].encode('utf-8').strip()        #is_break_free
		if info['i_b_f'] == 'NULL':
			info['i_b_f'] = 'No'

		info['i_c_f'] = data[20].encode('utf-8').strip()        #is_cancl_free
		if info['i_c_f'] == 'NULL':
			info['i_c_f'] = 'No'

		room_desc = data[21].encode('utf-8').strip()
		info['rd'] = room_desc                                   #room_desc

		if room_desc.find('含早餐') != -1:
			info['h_b'] = 'Yes'
			info['i_b_f'] = 'Yes'

		ut = str(data[22])                                              #update_time

		key = uid + '_' + str(dur) + '_' + info['ci'] + '_' + source

		info_list=[]
		info_list.append(info['rid'])
		info_list.append(info["rs"])
		info_list.append(info["rt"])
		info_list.append(info["occu"])
		info_list.append(info["bt"])
		info_list.append(info["size"])
		info_list.append(info["floor"])
		info_list.append(info["ci"])
		info_list.append(info["co"])
		info_list.append(info["price"])
		info_list.append(info["i_e"])
		info_list.append(info["i_e_f"])
		info_list.append(info["h_b"])
		info_list.append(info["i_b_f"])
		info_list.append(info["i_c_f"])
		info_list.append(info["rd"])
		info_list.append(info["ori_rt"])
		info_str="\t".join([ str(index_format(x)) for x in info_list])

		#sys.exit(-1)
		cur_span = -100000
		# new key
		if key not in key_set:
			key_set.add(key)
			key_roominfo_dict[key] = []
			key_roominfo_dict[key].append(ut)
			cur_span = 0


		# an old key
		if cur_span != 0:
			cur_ut_dt = str2datetime(ut)
			orig_ut_dt = str2datetime(key_roominfo_dict[key][0])
			if type(cur_ut_dt).__name__ != 'datetime' or type(orig_ut_dt).__name__ != 'datetime':
				_INFO('getNewestPrice', ['Warning', 'cur_ut = ' + ut, 'orig_ut_dt = ' + key_roominfo_dict[key]['ut']])
				continue
			
			cur_span = (cur_ut_dt - orig_ut_dt).seconds

		if cur_span < -10:
			print "filter by span\001"+key+"\001"+ut+"\001"+key_roominfo_dict[key][0]+"\001drop_info:"+info_str
			continue
		
		elif cur_span > 10: # update
			sys.stdout.write("filter all_by_span\t%s\tspan=%d,curt=%s,orit=%s,ori_size=%d\n"%(key,cur_span,ut,key_roominfo_dict[key][0],len(key_roominfo_dict[key])))
			key_roominfo_dict[key] = []
			key_roominfo_dict[key].append(ut)
			key_roominfo_dict[key].append(info_str)

		else:               # insert
			key_roominfo_dict[key].append(info_str)
			if cur_span > 0:
				key_roominfo_dict[key][0] = ut

	_INFO('getNewestPrice', ['key_roominfo_dict.size = ' + str(len(key_roominfo_dict)), 'total = ' + str(c)])
	
	return key_roominfo_dict

Usage = 'python xxx.py db_name table_name already_processed_city.txt'
if __name__ == '__main__':
	if len(sys.argv) != 3 and len(sys.argv) != 4:
		print Usage
		sys.exit(-1)

	db_name = sys.argv[1]
	table_name = sys.argv[2]

	if len(sys.argv) == 4:
		already_porcessed_city_file = sys.argv[3]
	else:
		already_porcessed_city_file = ''

	try:
		cache = redis.Redis(host='127.0.0.1', port=6379, db=0)
		pipeline = cache.pipeline()
	except Exception, e:
		_ERROR('Init Redis', ['Failed, error = ' + str(e.code)])
		sys.exit(-1)

	forex_rate_dict = loadForexInfo()
	#cname_cid_dict = loadCityInfo()
	sid_uid_dict = loadHidUidInfo()
	candHotelSet = loadCandidateHotel()
	openedSourceSet = loadOpenedHotelSource()

	source = ''
	city = ''
	#key_roominfo_dict = getNewestPrice(cname_cid_dict, forex_rate_dict, sid_uid_dict, db_name, table_name, city, source,openedSourceSet)
	key_roominfo_dict = getNewestPrice(candHotelSet, forex_rate_dict, sid_uid_dict, db_name, table_name, city, source,openedSourceSet)
	_INFO('hotel_num', ['key_roominfo_dict.size = ' + str(len(key_roominfo_dict))])

	c = 0
	data_len = 0

       
	for key in key_roominfo_dict.keys():
		value = "\n".join(key_roominfo_dict[key])
		data_len += len(value)

      
		try:
			cache.set(key,value)
			print "update\t"+key
			c += 1
		
		except Exception, e:
			_ERROR('Redis Caching Error', ['key = ' + key, 'value.length = ' + str(len(value))])
			_ERROR('Redis Caching Error', ['error code: ' + str(e)])
			continue

    
		if c % 30 == 0:
			try:
				pipeline.execute()
				_INFO('Redis', ['Cached' + str(c) + 'th data', 'datalen = ' + str(data_len)])
				data_len = 0
			
			except Exception, e:
				_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
				continue

	try:
		pipeline.execute()
		_INFO('finished', ['Cached ' + str(c) + 'th data', 'datalen = ' + str(data_len)])
	except Exception, e:
		_ERROR('Redis Pipeline execute', ['error code: ' + str(e)])
		pass

         
	sys.stdout.flush()

	#cache.save()
	_INFO('Redis', ['Finished Caching'])
