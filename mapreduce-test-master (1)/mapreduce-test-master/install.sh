#!/bin/sh
cat slaves | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        ssh root@$line -n "rm -rf /mapreduce-test/ && mkdir /mapreduce-test/"
        echo "Copy data to $line"
        scp  /mapreduce-test/setup.py root@$line:/mapreduce-test/ && scp /mapreduce-test/master root@$line:/mapreduce-test/ && scp /mapreduce-test/slaves root@$line:/mapreduce-test/
        echo "Setup $line"
        ssh root@$line -n "cd /mapreduce-test/ && python3 setup.py && ntpdate time.nist.gov"
        echo "Finished config node $line"
    fi
done
