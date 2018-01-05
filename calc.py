#!/usr/bin/env python3
# coding=utf-8

from functools import reduce

#100+200+300
print(100+200+300)

s1 = 72
s2 = 85
r = (s2 - s1)/s1
print('%f' % r)

#斐波数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        (a , b) = (b, a + b)
        n = n + 1
        G_COUNTER += 1
    return 'done'

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self #Fib is iterable
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

#reduce sample
def func1(x ,y):
    return x * y

def func2(x ,y):
    return (x * 10) + y

def prods(L2):
    return reduce(func1,list(L2))
    
print('3 * 5 * 7 * 9 =', prods([3, 5, 7, 9]))

#str2float
def str2float(str_input):
    decimal_point = 0 
    decimal_num = 0
    L = []
    for s in str_input:
        num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}[s]
        if num == -1:
            decimal_point = 1
        else:
            L.append(num)
            if decimal_point != 0:
                decimal_num += 1
    return reduce(func2,L)/(10**decimal_num)

print(str2float('123.44'))

#打印素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def primes_print(x):
    L_primes = []
    for n in primes():
        if n < x:
            L_primes.append(n)
        else:
            break
    print(L_primes)

#回数
def is_palindrome(n):
    list_input = str(n)
    nums = 0
    while nums < int(len(list_input)/2 + 0.5):
        if list_input[nums] != list_input[-nums-1]:
            return False
        nums += 1
    return True

L_pal = list(filter(is_palindrome, (x for x in range(1,999))))
print(L_pal)

#返回函数
def count():
    def f(i):
        return lambda:i*i
    L = [] 
    for i in range(1,6):
        print(f(i))
        L.append(f(i))
    return L


