import sys
import MySQLdb

if len(sys.argv) != 4:
	print 'Usag:python xx.py table_name[in] result_file[in] day[in]'
	sys.exit(1)

conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db='log_statistic')
cursor = conn.cursor()

table_name = sys.argv[1].strip()

source_count = {}

inFile = file(sys.argv[2].strip())
for line in inFile:
	lineList = line.strip().split('\t')

	if len(lineList) != 2:
		continue

	item = lineList[0].strip()
	
	itermList = item.strip().split('_')

	if len(itermList) < 2:
		continue

	error = '_'.join(itermList[0:-1])
	source = itermList[-1]

	num = lineList[1].strip()
	
	if source not in source_count:
		source_count[source] = {}

	source_count[source][error] = num



day = sys.argv[3].strip()

for sourceKey in source_count:
	sql = "replace into " + table_name + " (date, source"
	value = "('" + day + "','" + sourceKey

	for errorKey in source_count[sourceKey]:
		sql += "," + errorKey

		value += "','" + source_count[sourceKey][errorKey]

	
	sql += ") values "
	value += "')"

	sql += value + ";"

	cursor.execute(sql)

cursor.close()
conn.close()

