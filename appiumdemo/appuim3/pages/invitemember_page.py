# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : invitemember_page.py
# @Author   : Pluto.
# @Time     : 2020/11/17 19:05
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appuim3.pages.base_page import BasePage
from appiumdemo.appuim3.pages.invitemember_detail_page import InvitememberDetailPage


class InvitememberPage(BasePage):
    _addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def goto_invite_member_detail_page(self):
        self.find_and_click(self._addmember_element)
        return InvitememberDetailPage(self.driver)