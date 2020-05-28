#!/bin/bash

pwd
python -u one.py > log_test.log  2>&1 &
python -u two.py > log_test.log  2>&1 &
python -u three.py > log_test.log  2>&1 &

#python one.py &
#python two.py &
#python three.py &

