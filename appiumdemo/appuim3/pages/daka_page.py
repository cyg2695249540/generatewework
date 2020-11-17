# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : daka_page.py
# @Author   : Pluto.
# @Time     : 2020/11/17 19:37
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appuim3.pages.base_page import BasePage


class DakaPage(BasePage):
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