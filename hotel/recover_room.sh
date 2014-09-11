#!/bin/sh 
# author:lurong85, date: 20140430
# check if exists flight.sql, import, check, push to redis
# bakup flight.sql, and rm Permmision file

for file in `ls data_bak/*.sql`
do
    mysql -uroot -pxiaoaojianghu --default-character-set=utf8 hotel_recover  < $file
#    python push_hotel.py hotel_recover room 1>recover_std 2>recover_err
#    python truncate_table.py hotel_recover room
done  

