# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_1.py
# @Author   : Pluto.
# @Time     : 2020/11/6 19:19
"""
list降重
"""

class Test:
    _listA = ['python', '是', '一', '门', '动', '态', '语', '言', '言', '语']

    def test_demo(self):
        list = []
        for i in self._listA:
            if i not in list:
                list.append(i)
        print(list)
