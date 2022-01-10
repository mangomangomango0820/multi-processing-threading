# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/1/11 12:08 AM
# File      : Multiprocessing_While.py
# Tool      : PyCharm

import datetime, time
from multiprocessing import Process

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

def ProcessAliveOrNot(pro):
    if not pro.is_alive():
        logging.info(f"{pro} Not Alive.")
    else:
        logging.info(f"{pro} Alive")


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
            logging.info(f"****** Sub loop {i} ******")
            Subpro = Process(target=worker, kwargs={'name': 'Hanna', 'sleep': 4}, name='WORKER')
            ProcessAliveOrNot(pro=Subpro)

            Subpro.start()
            ProcessAliveOrNot(pro=Subpro)

            boss(name='BOSS', sleep=2)

            Subpro.join()
            ProcessAliveOrNot(pro=Subpro)

            i += 1
        else:
            logging.info("Post Loop")
            loop += 1
    else:
        logging.info("> End.")