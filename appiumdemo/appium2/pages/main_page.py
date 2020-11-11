# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/11/11 20:05
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium2.pages.base_page import BasePage
from appiumdemo.appium2.pages.contact_page import ContactPage
from appiumdemo.appium2.pages.search_page import SearchPage
from appiumdemo.appium2.pages.work_page import WorkPage


class MainPage(BasePage):
    _contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    _search_element = (MobileBy.ID, "com.tencent.wework:id/i6n")

    _work_element = (MobileBy.XPATH, "//*[@text='工作台']")

    def goto_contact_page(self):
        self.find_and_click(self._contact_element)
        return ContactPage(self.driver)

    def goto_search_page(self):
        self.find_and_click(self._search_element)
        return SearchPage(self.driver)

    def goto_work_page(self):
        self.find_and_click(self._work_element)
        return WorkPage(self.driver)
