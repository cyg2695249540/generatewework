# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/11/24 17:12
from selenium.webdriver.common.by import By

from seleniumdemo.selenium11_24.pages.addmember_page import AddmemberPage1124
from seleniumdemo.selenium11_24.pages.base_page import BasePage1124
from seleniumdemo.selenium11_24.pages.contact_page import ContactPage1124


class MainPage1124(BasePage1124):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    _addmember_button = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
    _contact_butto = (By.CSS_SELECTOR, "#menu_contacts")
    def goto_addmember_page(self):
        self.find_and_click(self._addmember_button)
        return AddmemberPage1124(self.driver)

    def goto_contact_page(self):
        self.find_and_click(self._contact_butto)
        return ContactPage1124(self.driver)
