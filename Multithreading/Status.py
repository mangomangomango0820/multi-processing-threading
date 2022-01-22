# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/1/22 2:59 PM
# File      : Status.py
# Tool      : PyCharm
# Reference : __repr__ << Thread << threading.py

import threading
import time, os

def Subthread(n):
    for i in range(n):
        print('is going to sleep', i, 's.')
        time.sleep(i)

def _get_status(thread=None):
    '''
    dict = {
        'initlal': {
            thread.is_alive(): False,
            thread._ident: None,                                 # type <class 'NoneType'>
            thread._started.is_set(): False,
            thread._is_stopped: False
        },
        'started': {
            thread.is_alive(): True,
            thread._ident: 1001,                                 # type <class 'int'>
            thread._started.is_set(): True,
            thread._is_stopped: False
        },
        'stopped': {
            thread.is_alive(): False,
            thread._ident: 1001,                                 # type <class 'int'>
            thread._started.is_set(): True,
            thread._is_stopped: True
        }
    }
    '''

    if not thread.is_alive():
        if thread._is_stopped:
            return 'stopped'
        else:
            return 'initial'
    else:
        if thread._started.is_set():
            return 'started'


if __name__=='__main__':
    subthread = threading.Thread(target=Subthread, args=(3, ), name='Childthread')
    print('initial', _get_status(thread=subthread))

    subthread.start()
    print('start', _get_status(thread=subthread))

    subthread.join()
    print('join', _get_status(thread=subthread))