# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_10.py
# @Author   : Pluto.
# @Time     : 2020/11/10 19:30
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例2:
输入: "()[]{}"
输出: true
示例3:
输入: "(]"
输出: false
示例4:
输入: "([)]"
输出: false
示例5:
输入: "{[]}"
输出: true
"""
def isValid(s):
    if len(s) % 2 == 1:
        return False
    p = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = list()
    for i in s:
        if i in p:
            if not stack or stack[-1] != p[i]:
                return False
            stack.pop()
        else:
            stack.append(i)
    return not stack

if __name__ == '__main__':
    s1="()"
    s2="()[]{}"
    s3="(]"
    s4 = "([)]"
    s5 = "{[]}"
    print(isValid(s1))
    print(isValid(s2))
    print(isValid(s3))
    print(isValid(s4))
    print(isValid(s5))


