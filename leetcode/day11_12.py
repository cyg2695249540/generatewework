# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_12.py
# @Author   : Pluto.
# @Time     : 2020/11/12 15:05
"""
exp:922. 按奇偶排序数组 II
给定一个非负整数数组A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当A[i] 为奇数时，i也是奇数；当A[i]为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。
示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
提示：
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""
def sortArrayByParityII():
    j=[]
    o=[]
    r=[]
    for i in A:
        if i%2==1:
            j.append(i)
        else:
            o.append(i)
    for i in range(len(j)):
        r.append(o[i])
        r.append(j[i])
    return r
if __name__ == '__main__':
    A=[4,2,5,7]
    print(sortArrayByParityII())