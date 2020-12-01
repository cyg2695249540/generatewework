# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day12_1.py
# @Author   : Pluto.
# @Time     : 2020/12/1 19:57
import os


def get_files(path, rule=''):
    files = []
    for fpath, dirs, fs in os.walk(path):
        for f in fs:
            if os.path.join(fpath, f).endswith(rule):
                files.append(f)
    return files


if __name__ == '__main__':
    b = get_files(r"C:\Users\uiui\Desktop\软件测试工具\python脚本")
    for i in b:
        print(i)
