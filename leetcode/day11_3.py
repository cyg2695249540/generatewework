# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_3.py
# @Author   : Pluto.
# @Time     : 2020/11/6 19:15
"""
ex:349
给定两个数组，编写一个函数来计算它们的交集。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
说明：
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""
class Test:
    _nums1 = [1, 2, 2, 1]
    _nums2 = [2, 2]
    def testset(self):
        set1 = set(self._nums1)
        set2 = set(self._nums2)
        print(list(set1 & set2))
