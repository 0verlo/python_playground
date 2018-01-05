#!/usr/bin/env python
# coding=utf-8

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

dataList = (s32IES0,s32SBS0,s32SBS1,s32SBS2,s32SBS3,s32SDS0,s32SDS1,s32SDS2,s32SDS3,s32STH0,s32STH1,s32STH2,s32STH3,s32MDP,s32MATH1,s32MATH2,s32Pro3,s32MDDZ1,s32MDDZ2,s32TFS1,s32TFS2,s32SFC,s32TFC,s32TPC,s32TRC)

i = 0
print(i)
while 100 > i:
    print('?')
    for attrList in dataList:
        print(attrList.__name__)
        if ('s32SFC' == attrList.__name__):
            attrList.append(1)
        i = i+1
print(s32SFC)
