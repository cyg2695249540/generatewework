# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : invitemember_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:48
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1126.pages.base_page import BasePage1126
from appiumdemo.appium1126.pages.invitemember_detail_page import InvitememberDetailPage1126


class InvitememberPage1126(BasePage1126):
    _addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def goto_invite_member_detail_page(self):
        self.find_and_click(self._addmember_element)
        return InvitememberDetailPage1126(self.driver)