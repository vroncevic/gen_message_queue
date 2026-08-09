#!/usr/bin/env bash

python3 main.py create --name "my_message_queue" --type "posix" --output "./demo/posix"
python3 main.py create --name "my_message_queue" --type "sysv" --output "./demo/sysv"
