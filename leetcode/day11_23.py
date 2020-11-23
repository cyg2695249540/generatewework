# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_23.py
# @Author   : Pluto.
# @Time     : 2020/11/23 13:59
"""
exp:680. 验证回文字符串 Ⅱ
给定一个非空字符串s，最多删除一个字符。判断是否能成为回文字符串。
示例 1:
输入: "aba"
输出: True
示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。
"""
def validPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    isPalindrome = lambda x: x == x[::-1]
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return isPalindrome(s[left + 1: right + 1]) or isPalindrome(s[left: right])
    return True


if __name__ == '__main__':
    s = "abcdedfcba"
    print(s[3:6])
    print(s[4:7])
    print(validPalindrome(s))
