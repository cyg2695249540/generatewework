# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : df.py
# @Author   : Pluto.
# @Time     : 2020/12/1 16:45
def mi(a, n):
    if n == 0:
        return 1
    else:
        return a * mi(a, n - 1)

if __name__ == '__main__':
    print(mi(2,3))

