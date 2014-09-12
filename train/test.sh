src_db=test
src_table=train_new

dest_db=onlinedb
flight_info_table=train_info
flight_ticket_info_table=train_ticket_info

python push_train.2.py $src_db $src_table $dest_db $flight_info_table $flight_ticket_info_table


