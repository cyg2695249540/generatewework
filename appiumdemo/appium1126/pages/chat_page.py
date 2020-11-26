# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : chat_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:45
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1126.pages.base_page import BasePage1126


class ChatPage1126(BasePage1126):
    _send_new = (MobileBy.ID, "com.tencent.wework:id/eo7")
    _send_element = (MobileBy.ID, "com.tencent.wework:id/eo3")
    _news = (MobileBy.ID, "com.tencent.wework:id/ens")

    def send_new(self, new):
        self.find_and_send_keys(self._send_new, new)
        self.find_and_click(self._send_element)
        return self

    def get_news(self):
        news = self.finds(self._news)
        return news