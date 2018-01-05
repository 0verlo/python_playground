#!/usr/bin/env python
# coding=utf-8

def calc_sum(*numbers):
    sum = 0
    for value in numbers:
        sum = sum + value
    return sum

sum = 0
for x in list(range(11)):
    sum = sum + x
print(sum)
print(calc_sum(1,2,3,4,5))
