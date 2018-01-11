#!/usr/bin/env python
# coding=utf-8
import random, time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

#task distributor
task_queue = Queue()
#task result
result_queue = Queue()

class QueueManager(BaseManager):
    pass

#init task queue on internet
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
#queue set on port 5000,set key
manager = QueueManager(address=('', 5000), authkey=b'abc')
#start queue
manager.start()
#get queue form net
task = manager.get_task_queue()
result = manager.get_result_queue()

#distribute tasks
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
#get result for queue
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

#clean up
manager.shutdown()
print('master exit.')
