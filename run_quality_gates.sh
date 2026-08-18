#!/bin/bash
#
# @brief   gen_message_queue
# @version 1.1.7
# @date    Sun Aug 09 07:48:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_message_queue
python3 gates/gates/isp_checker.py gen_message_queue
python3 gates/gates/limits_checker.py gen_message_queue
python3 gates/gates/srp_checker.py gen_message_queue

echo "Done"
