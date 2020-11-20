# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_20.py
# @Author   : Pluto.
# @Time     : 2020/11/20 13:49
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    a = sum(nums) - sum(set(nums))
    b = sum(range(len(nums) + 1)) - sum(set(nums))
    return [a, b]


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    print(findErrorNums(nums))
