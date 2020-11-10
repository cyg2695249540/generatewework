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
from typing import List

#  & 交集  | 并集  - 非集
def intersection(num1,num2):
    set1 = set(num1)
    set2 = set(num2)
    return list(set1 & set2)


if __name__ == '__main__':
    case1 = [1, 2, 2, 1]
    case2 = [2, 2]
    case3 = [4, 9, 5]
    case4 = [9, 4, 9, 8, 4]
    print(intersection(case1,case2))
    print(intersection(case3,case4))
