# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_27.py
# @Author   : Pluto.
# @Time     : 2020/11/27 11:43
def listtodict():
    b=dict(zip(list1,list2))
    return b
if __name__ == '__main__':
    list1=[3,5,3,4,6,7]
    list2=[2,3,4,2,1,2]
    print(listtodict())
