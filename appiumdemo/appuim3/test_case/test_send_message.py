# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_send_message.py
# @Author   : Pluto.
# @Time     : 2020/11/17 19:48
import allure
import pytest
from ruamel import yaml

from appiumdemo.appuim3.pages.app import App


def getdatas():
    datas = yaml.safe_load(open("../data/addcontact.yml", encoding="utf-8"))
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
    @pytest.mark.parametrize("chatname, new", getdatas()[0], ids=getdatas()[1])
    def test_send_message(self, chatname, new):
        getnews = self.main.goto_search_page().searchchat(chatname).send_new(new).get_news()
        assert getnews[-1].text == new