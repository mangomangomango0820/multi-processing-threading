# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/1/10 11:05 PM
# File      : Multithreading_While.py
# Tool      : PyCharm

import datetime, time
import threading

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s: %(levelname)s  %(message)s',
    datefmt='%Y-%m-%d %A %H:%M:%S',
    filename='logging.log',
    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
log = logging.getLogger(__name__)


def worker(name, sleep=2):
    logging.info(f"Worker '{name}': {sleep} s.")
    time.sleep(sleep)
    logging.info(f"Worker '{name}': done.")

def boss(name, sleep=4):
    logging.info(f"Boss '{name}': {sleep} s.")
    time.sleep(sleep)
    logging.info(f"Boss '{name}': done.")

def threadStatus(con, thread):
    info = [thread.is_alive(), thread._started.is_set(), thread._is_stopped]

    dict = {
        'initial': [False, False, False],
        'start': [True, True, False],
        'stop': [False, True, True]
    }

    if con in dict.keys():
        if not info == dict[con]:
            logging.error(f"{thread.name}: {info}")
        else:
            logging.info(f"{thread.name}: ident {thread._ident}, is_alive() {thread.is_alive()}, "
                 f"_started.is_set() {thread._started.is_set()}, _is_stopped {thread._is_stopped}")
    else:
        logging.info(f"{con} not in list {dict.keys()}")


if __name__ == '__main__':
    runTime = 120                                                   # total loop time
    looptime = 20                                                   # single loop time
    loopCounts = 20                                                 # total loop counts

    loop = 0
    start = time.time()
    while (loop < loopCounts) and (time.time()-start < runTime):    # if loop is larger than loop counts or duration
        logging.info(f"****** loop {loop} ******")                  # is larger than 'runTime', break and exit the loop
        START = time.time()
        i = 0
        while time.time()-START < looptime:
            logging.info(f">>> Sub loop {i} <<<")
            threadWorker = threading.Thread(target=worker, kwargs={'name': 'Hanna', 'sleep': 1}, name='WORKER')
            threadStatus(con='initial', thread=threadWorker)

            threadWorker.start()
            threadStatus(con='start', thread=threadWorker)

            boss(name='BOSS', sleep=4)

            threadWorker.join()
            threadStatus(con='stop', thread=threadWorker)

            i += 1
        else:
            logging.info("Post Loop")
            loop += 1
    else:
        logging.info("> End.")