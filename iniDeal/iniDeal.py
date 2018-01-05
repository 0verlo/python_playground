#!/usr/bin/env python
# coding=utf-8

import re

s32IES0 = []
s32SBS0 = []
s32SBS1 = []
s32SBS2 = []
s32SBS3 = []
s32SDS0 = []
s32SDS1 = []
s32SDS2 = []
s32SDS3 = []
s32STH0 = []
s32STH1 = []
s32STH2 = []
s32STH3 = []
s32MDP = []
s32MATH1 = []
s32MATH2 = []
s32Pro3 = []
s32MDDZ1 = []
s32MDDZ2 = []
s32TFS1 = []
s32TFS2 = []
s32SFC = []
s32TFC = []
s32TPC = []
s32TRC = []

strFileName = 'test.txt'
class valueTable(object):
    pass

#def initStore():
#    resule = valueTable()
#    return resule

def regularReset(strInput,table):
    matchObj = re.match('\s*([A-Za-z0-9]+)_(\d+)\s*=\s*(\d+)',strInput) 
    if matchObj:
        #print("matchObj:%s" % matchObj.group())
        print("matchObj:%s" % matchObj.group(1))
        print("matchObj:%s" % matchObj.group(2))
        print("matchObj:%s" % matchObj.group(3))

def funReader():
    resuleTable = valueTable()
    with open(strFileName, 'r') as fileReader:
        for line in fileReader: 
            print line
            regularReset(line,resuleTable)
            #print(type(line))

funReader()
