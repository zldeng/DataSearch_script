today=`date +%Y%m%d`
logFile=delete.log.$today
errFile=delete.err.$today
python delete_keys.py 1>$logFile 2>$errFile

