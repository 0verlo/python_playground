#!/usr/bin/env python
# coding=utf-8
import logging

try:
    print('try...')
    r = 10 / 0 
    print('result:%s' % r)
except ZeroDivisionError as e:
    print('except:%s' % e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        print('1111')

main()
print('end')
