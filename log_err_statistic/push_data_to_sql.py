import sys
import MySQLdb

if len(sys.argv) != 4:
	print 'Usag:python xx.py table_name[in] result_file[in] day[in]'
	sys.exit(1)

conn = MySQLdb.connect(host='127.0.0.1', user='root', charset='utf8',passwd='', db='log_statistic')
cursor = conn.cursor()

table_name = sys.argv[1].strip()

count = {}

inFile = file(sys.argv[2].strip())
for line in inFile:
	lineList = line.strip().split('\t')

	if len(lineList) != 2:
		continue

	item = lineList[0].strip()
	num = lineList[1].strip()

	count[item] = num

day = sys.argv[3].strip()

value = " values ('" + day

sql = "replace into " + table_name + " (date "

for key in count:
	sql += "," + key
	value += "','" + count[key]

sql += ") "
value += "') ;"

sql += value

cursor.execute(sql)

cursor.close()
conn.close()

