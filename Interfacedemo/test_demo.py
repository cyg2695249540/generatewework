# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/11/11 21:21
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        option=Options()
        option.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def test_ddd(self):
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID,"su")).click()

