# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : persinal_information_page.py
# @Author   : Pluto.
# @Time     : 2020/11/17 19:33
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appuim3.pages.base_page import BasePage
from appiumdemo.appuim3.pages.personal_information_setting_page import PersonalInformationSettingPage


class PersonalInformationPage(BasePage):
    _edit_element = (MobileBy.ID, "com.tencent.wework:id/i6d")

    def go_to_personal_information_setup_page(self):
        self.wait_for_clickable(self._edit_element)
        self.find_and_click(self._edit_element)
        return PersonalInformationSettingPage(self.driver)