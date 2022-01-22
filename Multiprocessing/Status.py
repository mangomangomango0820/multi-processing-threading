# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/1/22 2:59 PM
# File      : Status.py
# Tool      : PyCharm
# Reference : __repr__ << BaseProcess << process.py
#             (https://stackoverflow.com/questions/70527492/how-to-extract-the-status-of-a-subprocess)

import multiprocessing
import time, os

def Subpro(n):
    for i in range(n):
        print(multiprocessing.current_process.__name__, 'is going to sleep', i, 's.')
        time.sleep(i)

def _get_status(subprocess=None):
    '''
    dict = {
        'initlal': {
            subprocess._popen: None,
            subprocess.is_alive(): False,
        },
        'started': {
            subprocess._popen: is not None,
            subprocess.is_alive(): True,
           subprocess._popen.poll: is not None
        },
        'stopped': {
            subprocess._popen: is not None,
            subprocess.is_alive(): False,
            subprocess._popen.poll: 0                       # if exit as expected
        },
        'closed': {
            subprocess._closed: True
        }
    }
    '''

    if subprocess._closed:
        return 'closed'
    if subprocess._popen is None:
        if not subprocess.is_alive():
            return 'initial'
    else:
        exitcode = subprocess._popen.poll()
        if exitcode is not None:
            exitcode = multiprocessing.process._exitcode_to_name.get(exitcode, exitcode)
            return 'stopped'
        else:
            if subprocess._parent_pid != os.getpid():
                return 'unknown'
            else:
                return 'started'


if __name__=='__main__':
    pro = multiprocessing.Process(target=Subpro, args=(3, ), name='ChildProcess')
    print('initial', _get_status(subprocess=pro))

    pro.start()
    print('start', _get_status(subprocess=pro))

    pro.join()
    print('join', _get_status(subprocess=pro))

    pro.close()
    print('close', _get_status(subprocess=pro))