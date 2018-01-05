#!/usr/bin/env python
#coding=utf-8
import global_list

G_COUNTER = 0

def hanMove(n, A, C):
    global_list.GLOBAL_COUNTER += 1
    print('step%d,%c-->%c' %(global_list.GLOBAL_COUNTER,A,C))

def hanSolve(n, A, B, C):
    if 1 == n:
        hanMove(n,A,C)
    else:
        hanSolve(n-1, A, C, B)
        #step one moving all 1~n-1 A to B
        #so star form A end on B
        #because hanSolve(n,A,B,C) means star from A end on C
        #so start form A end on B means hanSolve(n,A,C,B)
        hanMove(n, A, C)
        #a real moveing step.The bottom one move from A to C
        hanSolve(n-1, B, A, C)
        #an imagination step like step one
        #it means move all 1~n-1 B to C

#A better code(but more difficult to understand)
def hanSolve2(n, A, B, C):
    if 1 == n:
        global G_COUNTER
        G_COUNTER += 1
        print('step%d,%c-->%c' %(G_COUNTER,A,C))
    else:
        hanSolve2(n-1,A,C,B) #move n-1 plates from A to B 
        hanSolve2(1,A,B,C)   #move 1 plate from A to C  
        hanSolve2(n-1,B,A,C) #move n-1 plates from B to C  

n = 5
hanSolve(n,'A','B','C')
print('-------------------------------------------------------------')
hanSolve2(n,'A','B','C')
