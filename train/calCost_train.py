import sys
import datetime
import time

from timezone import get_time_zone


#def durCal(dept_time, dest_time, time_zone_A, time_zone_B):
#time:20140903_12:20:30
def durCal(deptTimeStr, destTimeStr, dept_iata_code, dest_iata_code):
	deptList = deptTimeStr.strip().split('_')
	destList = destTimeStr.strip().split('_')

	if len(deptList[0]) != 8 or len(destList[0]) != 8:
		return -1

	dept_time = ''.join(deptList[0][0:4]) + '-' + deptList[0][4] + deptList[0][5] \
			+ '-' + deptList[0][6] + deptList[0][7] + 'T' + deptList[1]
	
	dest_time = ''.join(destList[0][0:4]) + '-' + destList[0][4] + destList[0][5] \
			+ '-' + destList[0][6] + destList[0][7] + 'T' + destList[1]

	dept_zone = get_time_zone('station',dept_iata_code,dept_time)
	dest_zone = get_time_zone('station',dest_iata_code,dest_time)

	if dept_zone < 0 or dest_zone < 0:
		return -1
	#print 'dept_time:' + dept_time
	#print 'dest_time:' + dest_time
	#print 'dept_zo: ' + str(dept_zone)
	#print 'dest_zo: ' + str(dest_zone)
	
	try:
		dept_time_str = datetime.datetime.strptime(dept_time, '%Y-%m-%dT%H:%M:%S')
		dest_time_str = datetime.datetime.strptime(dest_time, '%Y-%m-%dT%H:%M:%S')
		dept_time_temp = int(time.mktime(dept_time_str.timetuple()))
		dest_time_temp = int(time.mktime(dest_time_str.timetuple()))
		
		dur = dest_time_temp - dept_time_temp
		dur = dur - (dest_zone - dept_zone) * 3600
		
	except Exception, e:
		#traceback.print_exc(str(e))
		print str(e)
		return -1

	return dur

if __name__ == '__main__':
	print durCal('20141016_13:00:00','20141016_13:40:00','CDG','DUB')
