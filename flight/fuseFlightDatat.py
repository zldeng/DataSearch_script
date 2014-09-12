#encodeing=utf-8

import sys
import redis
import MySQLdb

from LOG import _ERROR, _INFO


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_contain_ch(str):
    for ch in str:
        if is_chinese(ch) : return True
    return False

def fuse_flight_data(db_name,table_name):
	conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db=db_name)
	cursor = conn.cursor()
	
	flight_info = {}
	flight_day_info = {}
	
	src_table = table_name
	sql = "select flight_no,plane_type,flight_corp,dept_id,dest_id,dept_time,dest_time,daydiff,seat_type,real_class,stop_id,source,dept_day,stop_time from " + src_table + " ;";
	
	try:
		cursor.execute(sql)
		datas = cursor.fetchall()
	
	except Exception, e:
		_INFO('fuse flight data',['execute sql error! sql = ' + sql])
		_INFO('fuse flight data',['Error! ' + str(e)])
		
		return flight_info, flight_day_info
	
	cursor.close()
	conn.close()

	
	for data in datas:
		flight_no = data[0].encode('utf-8').strip()
		flight_count = flight_no.count('_') + 1

		plane_type = data[1].encode('utf-8').strip()
		flight_corp = data[2].encode('utf-8').strip()
		dept_id = data[3].encode('utf-8').strip()
		dest_id = data[4].encode('utf-8').strip()
		dept_time = data[5].encode('utf-8').strip()
		dest_time = data[6].encode('utf-8').strip()
		daydiff = data[7].encode('utf-8').strip()
		seat_type = data[8].encode('utf-8').strip()
		real_class = data[9].encode('utf-8').strip()
		if 'NULL' == real_class:
			real_class = '_'.join(['NULL' for i in range(0,flight_count)])
		
		stop_id = data[10].encode('utf-8').strip()
		source = data[11].encode('utf-8').strip()
		dept_day = data[12].encode('utf-8').strip().replace('-','')
		stop_time = data[13].encode('utf-8').strip()
	
		if not (flight_no.count('_') == plane_type.count('_') == flight_corp.count('_') \
				== daydiff.count('_') == seat_type.count('_') == real_class.count('_') \
				== stop_id.count('|') == stop_time.count('|')) :
			#print 'flight_no: ' + flight_no
			#print 'plane_type: ' + plane_type
			#print 'flight_corp: ' + flight_corp
			#print 'daydiff: ' + daydiff
			#print 'seat_type: ' + seat_type
			#print 'real_class: ' + real_class
			#print 'stop_id: ' + stop_id
			#print 'stop_time: ' + stop_time
			#print 'data: ' + str(data)
			#INFO('fuse flight data',['data count error!','data = ' + str(data)])
			continue
		
		flight_day_key = flight_no + '\t' + dept_id + '\t' + dest_id + '\t' + dept_day
	
		if flight_day_key not in flight_day_info:
			flight_day_info[flight_day_key] = {}
			
			flight_day_info[flight_day_key]['stop_id'] = stop_id
			flight_day_info[flight_day_key]['stop_time'] = stop_time
			flight_day_info[flight_day_key]['plane_type'] = plane_type
			flight_day_info[flight_day_key]['flight_corp'] = flight_corp
			flight_day_info[flight_day_key]['daydiff'] = daydiff
	
		else:
			if 'NULL' in flight_day_info[flight_day_key]['stop_id'] and \
					'NULL' not in stop_id:
						flight_day_info[flight_day_key]['stop_id'] = stop_id
			
			if 'NULL' in flight_day_info[flight_day_key]['stop_time'] and \
					'NULL' not in stop_time:
						flight_day_info[flight_day_key]['stop_time'] = stop_time
	
			if 'NULL' in flight_day_info[flight_day_key]['daydiff'] and \
					'NULL' not in daydiff:
						flight_day_info[flight_day_key]['daydiff'] = daydiff
	
			if ('NULL' in flight_day_info[flight_day_key]['plane_type'] \
					and 'NULL' not in plane_type) \
					or (not is_chinese(flight_day_info[flight_day_key]['plane_type'].decode('utf-8')) \
					and is_chinese(plane_type.decode('utf-8'))):
						flight_day_info[flight_day_key]['plane_type'] = plane_type
	
			if ('NULL' in flight_day_info[flight_day_key]['flight_corp'] \
					and 'NULL' not in flight_corp) \
					or (not is_chinese(flight_day_info[flight_day_key]['flight_corp'].decode('utf-8')) \
					and is_chinese(flight_corp.decode('utf-8'))):
						flight_day_info[flight_day_key]['flight_corp'] = flight_corp
	return flight_day_info


if __name__ == '__main__':
	flight_info,flight_ticket_info = fuse_flight_data('test','flight_new')

	print 'flight_info size: ' + str(len(flight_info))
	print 'flight_ticket_info size: ' + str(len(flight_ticket_info))

