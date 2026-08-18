#!/bin/bash
#
# @brief   gen_message_queue
# @version 1.1.7
# @date    Sun Aug 09 07:48:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_message_queue
pylint gen_message_queue > gen_message_queue.report
echo "Done"
