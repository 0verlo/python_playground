#!/usr/bin/env python
# coding=utf-8

L1 = ['Hello','World',18,'Apple',None]
L2 = [s.lower() for s in L1 if(isinstance(s, str))]

print(L2)

def normalizes(str_input):
    return str_input.title()

L3 = ['adam', 'LISA', 'barT']
L4 = list(map(normalizes, L3))
print(L4)
