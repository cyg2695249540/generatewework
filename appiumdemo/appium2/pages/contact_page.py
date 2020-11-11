# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/11/11 20:06
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium2.pages.base_page import BasePage
from appiumdemo.appium2.pages.invitemember_page import InviteMemberPage
from appiumdemo.appium2.pages.search_page import SearchPage


class ContactPage(BasePage):
    _addmemeber_text = "添加成员"

    _search_element = (MobileBy.ID, "com.tencent.wework:id/i6n")

    def goto_invite_member_page(self):
        self.find_by_scroll_and_click(self._addmemeber_text)
        return InviteMemberPage(self.driver)

    def goto_search_page(self):
        self.find_and_click(self._search_element)
        return SearchPage(self.driver)
