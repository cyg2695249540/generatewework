# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : daka_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:44
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1126.pages.base_page import BasePage1126


class DakaPage1126(BasePage1126):
    _outside_element = (MobileBy.ID, "com.tencent.wework:id/hr_")
    _daka = (MobileBy.XPATH, "//*[contains(@text,'次外出')]")
    _result = (MobileBy.ID, "com.tencent.wework:id/oy")

    def outside_daka(self):
        self.find_and_click(self._outside_element)
        sleep(1)
        self.find_and_click(self._daka)
        return self

    def get_daka_result(self):
        r = self.find_and_get_text(self._result)
        return r