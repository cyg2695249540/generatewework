# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : invitemember_page.py
# @Author   : Pluto.
# @Time     : 2020/11/7 14:28
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1.pages.base_page import BasePage
from appiumdemo.appium1.pages.invitemember_detail_page import InviteMemberDetailPage


class InviteMemberPage(BasePage):
    _addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    def goto_invite_member_detail_page(self):
        self.find_and_click(self._addmember_element)
        return InviteMemberDetailPage(self.driver)