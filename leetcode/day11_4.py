# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day11_4.py
# @Author   : Pluto.
# @Time     : 2020/11/6 19:30
"""
ex:57
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
示例1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10]重叠。
"""


class Test:
    _intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [18, 19]]
    _newInterval = [4, 8]

    def test_insert(self):
        left, right = self._newInterval
        placed = False
        ans = list()
        for le, ri in self._intervals:
            if ri < left:
                ans.append([le, ri])
            elif le > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([le,ri])
            else:
                left = min(le, left)
                right = max(ri, right)
        if not placed:
            ans.append([left, right])
        print(ans)
