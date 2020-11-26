# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:36
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1126.pages.base_page import BasePage1126
from appiumdemo.appium1126.pages.invitemember_page import InvitememberPage1126
from appiumdemo.appium1126.pages.search_page import SearchPage1126


class ContactPage1126(BasePage1126):
    _addmemeber_text = "添加成员"

    _search_element = (MobileBy.ID, "com.tencent.wework:id/i6n")

    def goto_invite_member_page(self):
        self.find_by_scroll_and_click(self._addmemeber_text)
        return InvitememberPage1126(self.driver)

    def goto_search_page(self):
        self.find_and_click(self._search_element)
        return SearchPage1126(self.driver)