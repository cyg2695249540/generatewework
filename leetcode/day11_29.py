# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_29.py
# @Author   : Pluto.
# @Time     : 2020/11/29 8:51
def wanquanshu():
    a = []
    for i in range(1, 1000):
        s = 0
        for j in range(1, i):
            if i % j == 0 and j < i:
                s += j
                if s == i:
                    a.append(i)
    return a
if __name__ == '__main__':
    print(wanquanshu())
