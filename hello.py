#!/usr/bin/env python3
# coding=utf-8

name_list = ['Bart','Lisa','Adam']
for name in name_list:
    print('Hello,%s!'%name)
print('hello,world')
name = input('Please enter your name:')
print('Hello,%s!'%name)

d = {'a':1,'b':2,'c':3}
for key,value in d.items():
    print('%s:%d'%(key,value))

#装饰器sample
def log(text = ''):
    beginText = 'begin call' 
    endText = 'end call'
    if ''==text:
        pass
    elif isinstance(text, str):
        beginText = text
        endText = text
    else:
        pass
    def decorator(func):
        def wrapper(*args,**kw):
            print('begin call')
            tmp = func(*args,**kw)
            print('end call')
            return tmp #注意此处为保留func的返回值
        return wrapper
    return decorator

@log()
def now1():
    print('2017-10-17')
@log
def now2():
    print('2017-10-11')

#about class
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def printScore(self):
        print('%s: %s' % (self.name,self.score))
    def __str__(self):
        return 'Student %s here' % (self.name)
    __repr__ = __str__

bat = Student('bat',25)
bat.printScore()

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')
    def bark(self):
        print('woof,woof')

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._height*self._width
