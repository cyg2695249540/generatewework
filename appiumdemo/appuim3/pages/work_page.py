# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : work_page.py
# @Author   : Pluto.
# @Time     : 2020/11/17 19:37
from appiumdemo.appuim3.pages.base_page import BasePage
from appiumdemo.appuim3.pages.daka_page import DakaPage


class WorkPage(BasePage):
    _daka_text = "打卡"

    def goto_daka_page(self):
        self.find_by_scroll_and_click(self._daka_text)
        return DakaPage(self.driver)