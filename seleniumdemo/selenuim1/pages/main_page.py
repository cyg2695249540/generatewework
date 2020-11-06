# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/11/6 15:47
from selenium.webdriver.common.by import By

from seleniumdemo.selenuim1.pages.addmember_page import AddmemberPage
from seleniumdemo.selenuim1.pages.base_page import BasePage
from seleniumdemo.selenuim1.pages.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    _addmember_button=(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
    _contact_butto = (By.CSS_SELECTOR, "#menu_contacts")

    def goto_addmemberpage(self):
        self.find_and_click(self._addmember_button)
        return AddmemberPage(self.driver)

    def goto_contactpage(self):
        self.find_and_click(self._contact_butto)
        return ContactPage(self.driver)
