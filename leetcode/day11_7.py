# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_7.py
# @Author   : Pluto.
# @Time     : 2020/11/7 11:56
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为[−2^31, 2^31− 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

"""


# class Test:
#     _str = -120
#
#     def test_reverse(self):
#         s = str(abs(self._str))[::-1]
#         if self._str < 0:
#             s = "-" + s
#         r = int(s)
#         print(r)
#         if r >= -2 ** 31 and r <= 2 ** 31 - 1:
#             print(r)
#         else:
#             print(0)

def reverse(string):
    s = str(abs(string))[::-1]
    if string < 0:
        s = "-" + s
    r = int(s)
    if r >= -2 ** 31 and r < 2 ** 31 - 1:
        return r
    else:
        return 0


if __name__ == '__main__':
    str1 = 123
    str2 = -123
    str3 = 120
    print(reverse(str1))
    print(reverse(str2))
    print(reverse(str3))
