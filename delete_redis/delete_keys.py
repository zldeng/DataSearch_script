#--coding:utf-8--
#author:lurong85, date:20140430
#desc:

import redis
import datetime
import os
import sys


if __name__ == '__main__':
	dt = datetime.date.today().strftime('%Y%m%d')
	
	#conventional_dt_begin = (datetime.date.today() + datetime.timedelta(days=11)).strftime('%Y%m%d')
	#conventional_dt_end = (datetime.date.today() + datetime.timedelta(days=30)).strftime('%Y%m%d')
	#conventional_up_dt = (datetime.date.today() - datetime.timedelta(days=5)).strftime('%Y%m%d')

	#perennial_1_dt_begin = (datetime.date.today() + datetime.timedelta(days=6)).strftime('%Y%m%d')
	#perennial_1_dt_end = (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y%m%d')

	#perennial_2_dt_begin = (datetime.date.today() + datetime.timedelta(days=31)).strftime('%Y%m%d')

	#perennial_up_dt = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%Y%m%d')
	
	up_dt_threshold = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%Y%m%d')

	print dt

	r = redis.Redis(host='127.0.0.1', port=6379, db=0)
	p = r.pipeline()
	c = 0

	for key in r.keys():
		c+=1
		if c % 1000 == 0:
			c = 0
		items = key.split('_')
		
		#hotel
		if len(items)==4 : 
			dept_day=items[2].strip()
		#train,flight
		elif len(items)==5 :
			dept_day=items[3].strip()
		else:
			continue

		if dept_day < dt:
			print 'delete. dept_day out\t' + key
			r.delete(key)
			continue

		val=r.get(key)
		val_dt=val.split("\n")[0]
		update_dt=val_dt.replace("-","")[0:8]
		
		if update_dt < up_dt_threshold:
			print 'delete. update_day out\t' + key + '\tup_time:' + update_dt
			r.delete(key)
	
	p.execute()
