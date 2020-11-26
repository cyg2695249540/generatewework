# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : personal_information_setting_page.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:49
from appium.webdriver.common.mobileby import MobileBy

from appiumdemo.appium1126.pages.base_page import BasePage1126
from appiumdemo.appium1126.pages.edit_member_page import EditMemberPage1126


class PersonalInformationSettingPage1126(BasePage1126):
    _edit_member_element = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def go_to_edit_member_page(self):
        self.find_and_click(self._edit_member_element)
        return EditMemberPage1126(self.driver)