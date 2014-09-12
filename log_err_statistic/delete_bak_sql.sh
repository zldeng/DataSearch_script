last2day=`date -d "2 day ago" +"%Y%m%d"`
#last2day="20140910"

flight_bak_dir=/search/redis/flight/sql_bak

cd $flight_bak_dir

for file in `ls $flight_bak_dir | grep $last2day`
do
	rm -f $file
done

train_bak_dir=/search/redis/train/sql_bak

cd $train_bak_dir
for file in `ls $train_bak_dir | grep $last2day`
do
	rm -f $file
done


hotel_bak_dir=/search/redis/hotel/sql_bak

cd $hotel_bak_dir
for file in ` ls $hotel_bak_dir | grep $last2day`
do
	rm -f $file
done

