#!/usr/bin/env python
# coding=utf-8
import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()
def process_student():
    # 获取当前线程关联的student:
    sName = local_school.sName
    sClass = local_school.sClass
    print('Hello, %s in class %s (in %s)' % (sName,sClass,threading.current_thread().name))
def process_thread(sName,sClass):
    # 绑定ThreadLocal的student:
    student_info = local_school
    student_info.sName = sName
    student_info.sClass = sClass
    process_student()
t1 = threading.Thread(target= process_thread, args=('Alice','Alpha',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob','Beta',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
