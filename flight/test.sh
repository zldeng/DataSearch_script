src_db=test
src_table=flight_new

dest_db=onlinedb
flight_info_table=traffic_flight_info
flight_ticket_info_table=traffic_flight_ticket_info

python push_flight.2.py $src_db $src_table $dest_db $flight_info_table $flight_ticket_info_table


