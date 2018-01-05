#!/usr/bin/env python
# coding=utf-8

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

g = triangles()

n = 0
while n < 10:
    n = n+1
    print(next(g))
