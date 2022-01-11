<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [log](#log)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# log
```python
2022-01-11 23:05:34,808  Multithreading_While.py : INFO  ****** loop 0 ******
2022-01-11 23:05:34,808  Multithreading_While.py : INFO  >>> Sub loop 0 <<<
2022-01-11 23:05:34,808  Multithreading_While.py : INFO  WORKER: ident None, is_alive() False, _started.is_set() False, _is_stopped False
2022-01-11 23:05:34,808  Multithreading_While.py : INFO  Worker 'Hanna': 1 s.
2022-01-11 23:05:34,808  Multithreading_While.py : INFO  WORKER: ident 6158495744, is_alive() True, _started.is_set() True, _is_stopped False
2022-01-11 23:05:34,808  Multithreading_While.py : INFO  Boss 'BOSS': 4 s.
2022-01-11 23:05:35,813  Multithreading_While.py : INFO  Worker 'Hanna': done.
2022-01-11 23:05:38,813  Multithreading_While.py : INFO  Boss 'BOSS': done.
2022-01-11 23:05:38,814  Multithreading_While.py : INFO  WORKER: ident 6158495744, is_alive() False, _started.is_set() True, _is_stopped True
2022-01-11 23:05:38,814  Multithreading_While.py : INFO  >>> Sub loop 1 <<<
......
2022-01-11 23:05:50,828  Multithreading_While.py : INFO  >>> Sub loop 4 <<<
2022-01-11 23:05:50,828  Multithreading_While.py : INFO  WORKER: ident None, is_alive() False, _started.is_set() False, _is_stopped False
2022-01-11 23:05:50,829  Multithreading_While.py : INFO  Worker 'Hanna': 1 s.
2022-01-11 23:05:50,829  Multithreading_While.py : INFO  WORKER: ident 6158495744, is_alive() True, _started.is_set() True, _is_stopped False
2022-01-11 23:05:50,829  Multithreading_While.py : INFO  Boss 'BOSS': 4 s.
2022-01-11 23:05:51,830  Multithreading_While.py : INFO  Worker 'Hanna': done.
2022-01-11 23:05:54,831  Multithreading_While.py : INFO  Boss 'BOSS': done.
2022-01-11 23:05:54,832  Multithreading_While.py : INFO  WORKER: ident 6158495744, is_alive() False, _started.is_set() True, _is_stopped True
2022-01-11 23:05:54,832  Multithreading_While.py : INFO  Post Loop
2022-01-11 23:05:54,832  Multithreading_While.py : INFO  ****** loop 1 ******
......
2022-01-11 23:07:14,930  Multithreading_While.py : INFO  ****** loop 5 ******
......
2022-01-11 23:07:34,960  Multithreading_While.py : INFO  > End.
```
<br>

> notes：<br><br>
> 1 main loop costs ```looptime```, 20 s <br>
> total running time costs ```runTime```，120 s <br>
> main process adopts ```Boss``` function, which takes up 4 s，```join()``` main process waiting for sub process to be done
>> ```runTime``` = 120 s = ```6 main loop``` * ```looptime``` <br>
>> ```looptime``` = 20 s = ```main process``` * ```5 Subloop```