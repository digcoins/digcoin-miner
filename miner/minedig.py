#!/usr/bin/python3

"""
Copyright (C) 2019 Dig Coin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import threading
from sys import exit, argv
from time import sleep

from cleos import Cleos_Handler
import cleos as cl

# ***WARNING***
# Increasing this limit too much has the potential to use up all your
# resources in an instant. Modify at your own discretion.
MAX_NUM_THREADS = 4

def load_config(path):
    fp = open(path, 'r')

    try:
        return json.loads(fp.read())['config']
    except:
        raise
    finally:
        fp.close()

"""
Each thread will attempt approx. one mine operation per block.

Note: This is a naive implementation that does not attempt to syncronize
threads/mine attempts.
"""
def miner_thread(cleos_handler):
    while True:
        cl.send_mine_action(cleos_handler)
        sleep(0.5)

def main(config_path):
    config = load_config(config_path)['cleos']
    C = Cleos_Handler(config)

    num_threads = config['num_threads']

    if num_threads > MAX_NUM_THREADS or num_threads <= 0:
        print("num_threads must be a positive integer no greater than %d" % MAX_NUM_THREADS)
        exit(2)

    for _ in range(num_threads):
        thread = threading.Thread(target=miner_thread, args=(C,))
        thread.start()
        sleep(0.5)

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./minedig.py [config_path]")
        exit(1)

    main(argv[1])
