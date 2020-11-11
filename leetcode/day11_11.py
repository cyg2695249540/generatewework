# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_11.py
# @Author   : Pluto.
# @Time     : 2020/11/11 10:31
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例2:
输入: [4,1,2,1,2]
输出: 4
"""
from functools import reduce


def singleNumber(nums):
    # #使用额外空间
    # s = list()
    # for i in n:
    #     if i not in s:
    #         s.append(i)
    #     else:
    #         s.remove(i)
    # return s[0]
    # x^y异或运算 位相乘a*0=a a*a=0
    return reduce(lambda x, y: x ^ y, nums)



if __name__ == '__main__':
    nums1 = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    print(singleNumber(nums1))
    print(singleNumber(nums2))
