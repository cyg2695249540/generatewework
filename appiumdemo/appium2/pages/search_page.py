# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : search_page.py
# @Author   : Pluto.
# @Time     : 2020/11/11 20:06
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium2.pages.base_page import BasePage
from appiumdemo.appium2.pages.chat_page import ChatPage
from appiumdemo.appium2.pages.persinal_information_page import PersonalInformationPage


class SearchPage(BasePage):
    _search_element = (MobileBy.XPATH, "//*[@text='搜索']")
    _search_result = (MobileBy.ID, "com.tencent.wework:id/ccl")

    def searchmember(self, name):
        search_name = (MobileBy.XPATH, f"//*[@text='{name}']")
        self.find_and_send_keys(self._search_element, name)
        sleep(1)
        eles = self.finds(search_name)
        if len(eles) < 2:
            print("没有该联系人")
        else:
            eles[1].click()
        return PersonalInformationPage(self.driver)

    def searchchat(self,chatname):
        search_chat=(MobileBy.XPATH, f"//*[@text='{chatname}']")
        self.find_and_send_keys(self._search_element,chatname)
        sleep(1)
        eles = self.finds(search_chat)
        if len(eles) < 2:
            print("没有该群")
        else:
            eles[-1].click()
        return ChatPage(self.driver)

    def search_result(self):
        result = self.find_and_get_text(self._search_result)
        return result