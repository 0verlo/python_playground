#!/usr/bin/env python
# coding=utf-8
import math

def multi_isinstance(input_list):
    judge_result = True
    for i in input_list:
        if not isinstance(i,(int,float)):
            raise TypeError('A bad operand type!')
            judge_result = False
    return judge_result

def my_quadratic(a, b, c):
#    if not isinstance(a,(int,float)):
#        raise TypeError('A bad operand type!')
    input_list = (a, b, c)
    multi_isinstance(input_list)
    count_result1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    count_result2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    return count_result1, count_result2

print(my_quadratic(2, 3, 1))
print(my_quadratic(1, 3, -4))
#print(my_quadratic('A', 3, 1))
