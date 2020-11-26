# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:36
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1126.pages.base_page import BasePage1126
from appiumdemo.appium1126.pages.contact_page import ContactPage1126
from appiumdemo.appium1126.pages.search_page import SearchPage1126
from appiumdemo.appium1126.pages.work_page import WorkPage1126


class MainPage1126(BasePage1126):
    _contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    _search_element = (MobileBy.ID, "com.tencent.wework:id/i6n")

    _work_element = (MobileBy.XPATH, "//*[@text='工作台']")

    def goto_contact_page(self):
        self.find_and_click(self._contact_element)
        return ContactPage1126(self.driver)

    def goto_search_page(self):
        self.find_and_click(self._search_element)
        return SearchPage1126(self.driver)

    def goto_work_page(self):
        self.find_and_click(self._work_element)
        return WorkPage1126(self.driver)