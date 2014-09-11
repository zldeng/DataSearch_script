rsync -r 10.131.136.190::nobody/flight_new.sql ./

tmpdb=test
mysql -u root --default-character-set=utf8 $tmpdb < flight_new.sql 
