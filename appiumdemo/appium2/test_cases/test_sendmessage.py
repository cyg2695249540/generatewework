# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_sendmessage.py
# @Author   : Pluto.
# @Time     : 2020/11/11 20:05
import allure
import pytest
import yaml

from appiumdemo.appium2.pages.app import App


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    chatnew = datas["chatnew"]
    case3 = datas["case3"]
    return chatnew, case3

@allure.feature("消息模块")
class TestSendmessage:
    def setup(self):
        self.app = App()
        self.main = self.app.startapp().goto_main_page()

    def teardown(self):
        self.app.stopapp()

    @allure.story("成功发送消息")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("chatname, new", get_datas()[0], ids=get_datas()[1])
    def test_send_message(self, chatname, new):
        getnews = self.main.goto_search_page().searchchat(chatname).send_new(new).get_news()
        assert getnews[-1].text == new