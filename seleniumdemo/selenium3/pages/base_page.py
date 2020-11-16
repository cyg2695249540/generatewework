# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_page.py
# @Author   : Pluto.
# @Time     : 2020/11/16 15:19
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, base_driver=None):
        if base_driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver : WebDriver= base_driver
        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)

    def find(self,locator):
        return self.driver.find_element(*locator)
    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_send_keys(self, locator, value):
        self.find(locator).send_keys(value)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_clickable(self, element):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))

    def get_tips_text(self):
        sleep(1)
        get_tips = (By.CSS_SELECTOR, "#js_tips")
        return self.find_and_get_text(get_tips)
