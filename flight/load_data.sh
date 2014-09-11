for sqlfile in `ls ./data`
do
	echo $sqlfile
	sh  load.sh $sqlfile
done
