# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_daka.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:36
import allure
import pytest

from appiumdemo.appium1126.pages.app import App1126


@allure.feature("打卡模块")
class TestDaka:
    def setup(self):
        self.app = App1126()
        self.main = self.app.startapp().goto_main_page()

    def teardown(self):
        self.app.stopapp()

    @allure.story("外出打卡成功")
    @pytest.mark.flaky(reruns=1)
    def test_daka(self):
        r = self.main.goto_work_page().goto_daka_page().outside_daka().get_daka_result()
        assert r == "外出打卡成功"