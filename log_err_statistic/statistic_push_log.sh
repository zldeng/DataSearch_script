lastday=`date -d "1 day ago" +"%Y%m%d"`
#lastday="20140910"

flight_log_file=/search/redis/flight/push_log/push_flight_std.$lastday
flight_tmp=flight_push.log
flight_result=flight_push_statistic.txt


flight_table_name=flight_log

if [ -f $flight_log_file ]
then
	cp $flight_log_file $flight_tmp

	grep "filter	" $flight_tmp | awk -F"\t" '{print $2}' | awk -F"\t" '{c[$0]++}END{for(i in c){print i"\t"c[i]}}' > $flight_result
	python push_data_to_sql.py $flight_table_name $flight_result $lastday

	rm -f $flight_tmp
fi

train_log_file=/search/redis/train/push_log/push_train_std.$lastday
train_tmp=train_push.log
train_result=train_push_statistic.txt

train_table_name=train_log

if [ -f $train_log_file ]
then
	cp $train_log_file $train_tmp

	grep "filter	" $train_tmp | awk -F"\t" '{print $2}' | awk -F"\t" '{c[$0]++}END{for(i in c){print i"\t"c[i]}}' > $train_result
	
	python push_data_to_sql.py $train_table_name $train_result $lastday
	rm -f $train_tmp

fi

hotel_log_file=/search/redis/hotel/push_log/push_hotel_std.$lastday
hotel_tmp=hotel_push.log
hotel_result=hotel_push_statistic.txt

hotel_table_name=hotel_log
if [ -f $hotel_log_file ]
then
	cp $hotel_log_file $hotel_tmp

	grep "filter	" $hotel_tmp | awk -F"\t" '{print $2}' | awk -F"\t" '{c[$0]++}END{for(i in c){print i"\t"c[i]}}' > $hotel_result
	
	python push_data_to_sql.py $hotel_table_name $hotel_result $lastday
	rm -f $hotel_tmp

fi



