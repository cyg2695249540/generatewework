# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_22.py
# @Author   : Pluto.
# @Time     : 2020/11/22 17:05
def aaa():
    a = str.replace("?", "!").split("!")
    b=[]
    for i in a:
        if i !='':
            b.append(i)
    b=sorted(b,key=lambda x:x[-1])
    return b


if __name__ == '__main__':
    str = "192.0.0.1?!289.0.0.1!192.163.10.28?192.0.0.1"
    print(aaa())
