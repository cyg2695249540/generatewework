# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_21.py
# @Author   : Pluto.
# @Time     : 2020/11/21 12:45
"""
exp:219. 存在重复元素 II
给定一个整数数组和一个整数k，判断数组中是否存在两个不同的索引i和j，使得nums [i] = nums [j]，并且 i 和 j的差的 绝对值 至多为 k。
示例1:
输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""














def containsNearbyDuplicate(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic and i - dic[nums[i]] <= k:
            return True
        dic[nums[i]] = i
    return False


if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    print(containsNearbyDuplicate(nums, k))
