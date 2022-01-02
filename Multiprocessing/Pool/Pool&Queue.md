<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Knowledge Points](#knowledge-points)
- [Note on Result](#note-on-result)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# Knowledge Points
- [x] psutil <br>psutil.pids()
- [x] multiprocessing<br>
Manager().Queue() <br>
Pool() <br>
Process().is_alive() <br>
pool.job_counter()
- [x] os <br>
os.getpid() <br>
os.getppid()


# Note on Result
```python

2022-01-02 18:07:00.272495 86470 MainProcess 420              # pid 86470, main process,      pid cnt 420
2022-01-02 18:07:00.386738 86476 SpawnPoolWorker-5 True       # pid 86476, SpawnPoolWorker-5, pid cnt 425, process 1
parent:  86470                                                # starting from here, start 4 processes
put in q：A
put in q：B
put in q：C
Full q !!!
Full q !!!                                                    # qsize = 3
('pid', 86476, 'pid count', 425, 'name', '1')
2022-01-02 18:07:01.411424 86474 SpawnPoolWorker-3 True       # pid 86474, SpawnPoolWorker-3, pid cnt 426, process 2
parent:  86470
get from q：A
get from q：B
get from q：C                                                
('pid', 86474, 'pid count', 426, 'name', '1')
count(2)                                                      
2022-01-02 18:07:02.433931 86475 SpawnPoolWorker-4 True       # pid 86475, SpawnPoolWorker-4, pid cnt 426, process 3
parent:  86470
put in q：A
put in q：B
put in q：C
Full q !!!
Full q !!!
('pid', 86475, 'pid count', 426, 'name', '2')
2022-01-02 18:07:03.452020 86473 SpawnPoolWorker-2 True       # pid 86473, SpawnPoolWorker-2, pid cnt 426, process 4
parent:  86470
get from q：A
get from q：B
get from q：C
('pid', 86473, 'pid count', 426, 'name', '2')
count(4)
2022-01-02 18:07:04.462452 86476 SpawnPoolWorker-5 True       # pid 86476, SpawnPoolWorker-5, pid cnt 424, process 1
parent:  86470                                               
put in q：A
put in q：B
put in q：C
Full q !!!
Full q !!!
('pid', 86476, 'pid count', 424, 'name', '3')
2022-01-02 18:07:05.471305 86474 SpawnPoolWorker-3 True       # pid 86474, SpawnPoolWorker-3, pid cnt 424, process 2
parent:  86470
get from q：A
get from q：B
get from q：C
('pid', 86474, 'pid count', 424, 'name', '3')
count(6)
2022-01-02 18:07:06.483477 86475 SpawnPoolWorker-4 True       # pid 86475, SpawnPoolWorker-4, pid cnt 424, process 3
parent:  86470
put in q：A
put in q：B
put in q：C
Full q !!!
Full q !!!
('pid', 86475, 'pid count', 424, 'name', '4')
2022-01-02 18:07:07.494109 86473 SpawnPoolWorker-2 True       # pid 86473, SpawnPoolWorker-2, pid cnt 424, process 4
parent:  86470
get from q：A
get from q：B
get from q：C
('pid', 86473, 'pid count', 424, 'name', '4')
count(8)
2022-01-02 18:07:08.502460 86476 SpawnPoolWorker-5 True       # pid 86476, SpawnPoolWorker-5, pid cnt 424, process 1
parent:  86470
put in q：A
put in q：B
put in q：C
Full q !!!
Full q !!!
('pid', 86476, 'pid count', 424, 'name', '5')
2022-01-02 18:07:09.512080 86474 SpawnPoolWorker-3 True       # pid 86474, SpawnPoolWorker-3, pid cnt 423, process 2
parent:  86470
get from q：A
get from q：B
get from q：C
('pid', 86474, 'pid count', 423, 'name', '5')
count(10)                                                     # job counter 10
**********
2022-01-02 18:07:10.524936 86470 MainProcess 419              # pid 86470, main process,      pid cnt 419
                                                              #                                       423-419=4
Process finished with exit code 0
```


