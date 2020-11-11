# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_5.py
# @Author   : Pluto.
# @Time     : 2020/11/6 19:38
"""
ex:941
给定一个整数数组A，如果它是有效的山脉数组就返回true，否则返回 false。
让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
A.length >= 3
在0 < i< A.length - 1条件下，存在i使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
示例 1：
输入：[2,1]
输出：false
示例 2：
输入：[3,5,5]
输出：false
示例 3：
输入：[0,3,2,1]
输出：true
"""


# class Test:
#     _A = [0, 3, 2, 1]
#
#     def test_mountainslist(self):
#         N = len(self._A)
#         i = 0
#         while i + 1 < N and self._A[i] < self._A[i + 1]:
#             i += 1
#         if i == 0 or i == N - 1:
#             print(False)
#         while i < N - 1 and self._A[i] > self._A[i + 1]:
#             i += 1
#         print(i == N - 1)

def mountainslist(lista):
    N = len(lista)
    i = 0
    while i + 1 < N and lista[i] < lista[i + 1]:
        i += 1
    if i == 0 or i == N - 1:
        return False
    while i + 1 < N and lista[i] > lista[i + 1]:
        i += 1
    return i + 1 == N


if __name__ == '__main__':
    A = [2, 1]
    B = [3, 5, 5]
    C = [0, 3, 2, 1]
    print(mountainslist(A))
    print(mountainslist(B))
    print(mountainslist(C))
