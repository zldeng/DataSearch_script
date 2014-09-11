#!/bin/sh 

CUR_DIR=`pwd`
SQL_DATA_NAME="room"
RIGHT_NOW=`date +%Y%m%d_%H%M%S`

log_dir=push_log
cur_day=`date +%Y%m%d`
last_day=`date -d yesterday +%Y%m%d`

cd $log_dir
for oldFile in `ls | grep  -E -v "$cur_day|$last_day|err"`
do
	rm -f $oldFile
done

cd ..

logFile=$log_dir/push_hotel_std.$cur_day
errFile=$log_dir/push_hotel_err

SQL_FILE=${SQL_DATA_NAME}${RIGHT_NOW}".sql"
rsync -r 10.131.136.190::nobody/room.sql $SQL_FILE

database="hotel_"`date +%Y%m%d%H%M%S`
mysql -e "create database $database;"

mysql -u root --default-character-set=utf8 $database  < $SQL_FILE

python push_hotel.py $database $SQL_DATA_NAME 1>>$logFile 2>$errFile


mysql -e "drop database $database;"

mv $SQL_FILE ${CUR_DIR}/sql_bak/


