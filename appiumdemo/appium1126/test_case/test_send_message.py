# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_send_message.py
# @Author   : Pluto.
# @Time     : 2020/11/26 19:36
import allure
import pytest
import yaml

from appiumdemo.appium1126.pages.app import App1126


def get_datas():
    datas = yaml.safe_load(open("../datas/send_message_demo", encoding="utf-8"))
    chatnew = datas["chatnew"]
    case = datas["case"]
    return chatnew, case

@allure.feature("消息模块")
class TestSendmessage:
    def setup(self):
        self.app = App1126()
        self.main = self.app.startapp().goto_main_page()

    def teardown(self):
        self.app.stopapp()

    @allure.story("成功发送消息")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("chatname, new", get_datas()[0], ids=get_datas()[1])
    def test_send_message(self, chatname, new):
        getnews = self.main.goto_search_page().searchchat(chatname).send_new(new).get_news()
        assert getnews[-1].text == new