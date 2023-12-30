#!/bin/bash
#
# @brief   gen_message_queue
# @version v1.0.1
# @date    Sat Aug 1 07:52:38 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf fresh_new/ full_simple_new/ latest_pro/ simple_read/ simple_write/
python3 -m coverage run -m --source=../gen_message_queue unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
