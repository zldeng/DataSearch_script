#!/bin/sh

start_time=`date +%s`

cur_dir=`pwd`
sql_data_name="flight_new"
right_now=`date +%Y%m%d_%H%M%S`
bak_dir=sql_bak
log_dir=push_log
cur_day=`date +%Y%m%d`
last_day=`date -d yesterday +%Y%m%d`

cd $log_dir
for old_file in `ls | grep -v -E "$cur_day|$last_day|err"`
do
	rm -f $old_file
done
cd ..

log_file=$log_dir/push_flight_std.$cur_day
err_file=$log_dir/push_flight_err

echo "get sql data..." >> $log_file
sql_file=$sql_data_name$right_now".sql"
rsync -r 10.131.136.190::nobody/flight_new.sql ./$sql_file


echo "create database..." >> $log_file
database="flight_"`date +%Y%m%d%H%M%S`

mysql -e "create database $database;"

flight_info_table_name=traffic_flight_info
flight_ticket_info_table_name=traffic_flight_ticket_info

dest_db_name=onlinedb

echo "push data into sql and redis..." >> $log_file
if [ -f "$sql_file" ]
then
	mysql -u root --default-character-set=utf8 $database < $sql_file
	
	python push_flight.py $database $sql_data_name $dest_db_name  $flight_info_table_name $flight_ticket_info_table_name 1>>$log_file 2>>$err_file

fi

echo "put data done" >> $log_file
echo "drop database..." >> $log_file
mysql -e "drop database $database;"

echo "bak sql file" >> $log_file
mv $sql_file $bak_dir/
#echo "remobe sql file"
#rm -f $sql_file

end_time=`date +%s`
cost_time=$[ $end_time - $start_time ]
echo "Update data Done! cost "$cost_time" s" >> $log_file
echo "" >> $log_file
echo "" >> $log_file
