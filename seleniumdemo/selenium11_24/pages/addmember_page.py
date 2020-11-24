# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addmember_page.py
# @Author   : Pluto.
# @Time     : 2020/11/24 19:11
from selenium.webdriver.common.by import By

from seleniumdemo.selenium11_24.pages.base_page import BasePage1124
from seleniumdemo.selenium11_24.pages.contact_page import ContactPage1124


class AddmemberPage1124(BasePage1124):
    _username = (By.ID, "username")
    _acctid = (By.ID, "memberAdd_acctid")
    _phone = (By.ID, "memberAdd_phone")
    _save_member = (By.CSS_SELECTOR, ".js_btn_save")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")
    _leave = (By.CSS_SELECTOR, "[node-type='cancel']")

    def addusername(self, username):
        self.find_and_send_keys(self._username, username)
        return self

    def addacctid(self, acctid):
        self.find_and_send_keys(self._acctid, acctid)
        return self

    def addphone(self, phone):
        self.find_and_send_keys(self._phone, phone)
        return self

    def save_member(self):
        self.find_and_click(self._save_member)
        return ContactPage1124(self.driver)

    def cancel_member(self):
        self.find_and_click(self._cancel_member)
        self.find_and_click(self._leave)
        return ContactPage1124(self.driver)