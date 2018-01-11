#!/usr/bin/env python
# coding=utf-8
import random, time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

#get queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#connect to master
server_addr = '127.0.0.1'
print('Connect to server %s.Successed' % server_addr)
#the same sets as the MASTER
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
manager.connect()
#get queue form net
task = manager.get_task_queue()
result = manager.get_result_queue()

#start working
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d + 1' % n)
        r = '%d + 1 = %d' % (n, n+1)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queueu is empty!Faild')
#END
print('All work done!')
