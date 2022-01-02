# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/1/2 6:02 PM
# File      : Pool&Queue.py
# Tool      : PyCharm
'''
A basic example using the knowledge points of pool and queue
'''

from multiprocessing import current_process, Manager, Pool, pool
import datetime, time, psutil, os


def func1(name, q):
    '''

    :param q: put msg into q
    :return: child process pid, pid counter, name
    '''
    # child process pid, name, is alive or not
    print(datetime.datetime.now(), current_process().pid, current_process().name, current_process().is_alive())
    # parent process pid (= main process pid)
    print('parent: ', os.getppid())
    time.sleep(1)

    # len(msg) = 5
    msg = ['A', 'B', 'C', 'D', 'E']
    try:
        for i in msg:
            # as long as q is not full, put msg into q
            if not q.full():
                print("put in q：%s" % i)
                q.put(i)
            else:
                print('Full q !!!')
    except Exception as e:
        print(e)

    return 'pid', current_process().pid, 'pid count', len(psutil.pids()), 'name', name


def func2(name, q):
    '''

    :param q: get msg from q
    :return: child process pid, pid counter, name
    '''
    # child process pid, name, is alive or not
    print(datetime.datetime.now(), current_process().pid, current_process().name, current_process().is_alive())
    # parent process pid (= main process pid)
    print('parent: ', os.getppid())
    time.sleep(1)

    try:
        for i in range(q.qsize()):
            # as long as q is not empty, get msg from q
            if not q.empty():
                print("get from q：%s" % q.get(True, timeout=0.5))
            else:
                print('Empty q !!!')
    except Exception as e:
        print(e)

    return 'pid', current_process().pid, 'pid count', len(psutil.pids()), 'name', name


if __name__ == "__main__":
    print(datetime.datetime.now(), current_process().pid, current_process().name, len(psutil.pids()))

    # qsize = 3, len(msg) = 5 ===> 5 > 3
    q = Manager().Queue(3)  # here define qsize = 3
    # use with to control the termination of pool
    # process count = 4
    with Pool(processes=4) as pl:  # here limit multi-pro count to 4
        # len(PROX) = 5
        PROX = ['1', '2', '3', '4', '5']
        for PRO in PROX:
            # start a process A
            A = pl.apply(func1, kwds={'name': PRO, 'q': q})
            print(A)
            B = pl.apply(func2, kwds={'name': PRO, 'q': q})
            print(B)
            # job_counter = len(PROX) * len([A, B]) = 5 * 2 = 10
            print(pool.job_counter)

    # mark the end of 4 child processes
    print("*" * 10)
    print(datetime.datetime.now(), current_process().pid, current_process().name, len(psutil.pids()))