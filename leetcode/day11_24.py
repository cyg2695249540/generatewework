# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_24.py
# @Author   : Pluto.
# @Time     : 2020/11/24 16:06
"""
exp:66. 加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：
输入：digits = [0]
输出：[1]
提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
def plusOne():

    s="".join(str(x) for x in digits)
    ss=str(int(s)+1)
    r=[int(x) for x in ss]
    return [0]*(len(digits)-len(r))+r

if __name__ == '__main__':
    digits = [0, 0, 0]
    print(plusOne())
