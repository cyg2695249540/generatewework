# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_13.py
# @Author   : Pluto.
# @Time     : 2020/11/13 18:27
"""
epx:125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出 false
"""


def isPalindrome(s):
    s = filter(str.isalnum, s.lower())
    ss = ''.join(list(s))
    return ss == ss[::-1]


def shuzi(s):
    s = filter(str.isdigit, s)
    return ''.join(list(s))


def zimu(s):
    s = filter(str.isalpha, s)
    return ''.join(list(s))


if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(isPalindrome(s1))
    print(isPalindrome(s2))
    s = "sadisjh34ras21i"
    print(shuzi(s))
    print(zimu(s))
