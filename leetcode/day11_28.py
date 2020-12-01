# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_28.py
# @Author   : Pluto.
# @Time     : 2020/11/28 10:27
def sxh():
    sxh = []
    for i in range(1, 1000):
        s = 0
        for j in str(i):
            s += int(j) ** 3
            if i == int(j) ** 3:
                sxh.append(i)
    return sxh
if __name__ == '__main__':
    print(sxh())