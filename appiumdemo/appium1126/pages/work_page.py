# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : work_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:43
from appiumdemo.appium1126.pages.base_page import BasePage1126
from appiumdemo.appium1126.pages.daka_page import DakaPage1126


class WorkPage1126(BasePage1126):
    _daka_text = "打卡"

    def goto_daka_page(self):
        self.find_by_scroll_and_click(self._daka_text)
        return DakaPage1126(self.driver)