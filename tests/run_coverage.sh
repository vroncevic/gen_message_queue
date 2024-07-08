#!/bin/bash
#
# @brief   gen_message_queue
# @version v1.0.1
# @date    Sat Aug 1 07:52:38 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_message_queue_coverage.xml gen_message_queue_coverage.json .coverage
rm -rf fresh_new/ full_simple_new/ latest_pro/ simple_read/ simple_write/
ats_coverage_run.py -n gen_message_queue -p ../README.md
rm -rf fresh_new/ full_simple_new/ latest_pro/ simple_read/ simple_write/
python3 -m coverage run -m --source=../gen_message_queue unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_message_queue_coverage.xml 
python3 -m coverage json -o gen_message_queue_coverage.json
python3 -m coverage report --format=markdown -m
