src_db=test
src_table=room

testLog=test.log
testErr=test.err

python  push_hotel.2.py $src_db $src_table 1>$testLog 2>$testErr
