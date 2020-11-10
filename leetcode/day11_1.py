# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_1.py
# @Author   : Pluto.
# @Time     : 2020/11/6 19:19

"""
list = []
    for i in self._listA:
        if i not in list:
            list.append(i)
    print(list)
list降重
list= ['python', '是', '一', '门', '动', '态', '语', '言', '言', '语']
"""


def demo():
    # #循环判断方法
    # list=[]
    # for i in listA:
    #     if i not in list:
    #         list.append(i)
    # return list

    #set去重,不能保留原来的顺序,需配合sort方法
    listB=list(set(listA))
    listB.sort(key=listA.index)
    return listB

if __name__ == '__main__':
    listA = ['python', '是', '一', '门', '动', '态', '语', '言', '言', '语']
    print(demo())
