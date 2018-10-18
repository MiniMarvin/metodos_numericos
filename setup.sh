#!/bin/bash
ret=`python -c 'import sys; print("%i" % (sys.hexversion>0x03000000))'`
if [ $ret -eq 0 ]; then
    echo "we require python version >3"

    ## Try with python 3
    res=`python3 -c 'import sys; print("%i" % (sys.hexversion>0x03000000))'`
    if [ $res -eq 0 ]; then
    	echo "we require python3 version to work otherwise"
	else
		echo "python3 version ok"
	fi 
else 
    echo "python version is > 3"
    pip install -r requirements.txt
fi
