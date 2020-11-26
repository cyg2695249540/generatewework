# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : edit_member_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:50
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1126.pages.base_page import BasePage1126


class EditMemberPage1126(BasePage1126):
    _right_element = (MobileBy.XPATH, "//*[@text='确定']")

    def delete_member(self):
        from appiumdemo.appium1.pages.search_page import SearchPage
        self.find_by_scroll_and_click("删除成员")
        self.find_and_click(self._right_element)
        return SearchPage(self.driver)