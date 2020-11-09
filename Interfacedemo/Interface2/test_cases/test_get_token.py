# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_get_token.py
# @Author   : Pluto.
# @Time     : 2020/11/9 11:01
import allure
import pytest
import yaml

from Interfacedemo.Interface2.api.base_api import BaseApi


def get_datas():
    datas = yaml.safe_load(open("../datas/datas.yaml", encoding="utf-8"))
    demo = datas["demo"]
    case = datas["case"]
    return demo, case


@allure.feature("获取token模块")
class TestGetToken:
    def setup_class(self):
        self.gettoken = BaseApi()

    @allure.story("获取token用例")
    @pytest.mark.falky(reruns=1)
    @pytest.mark.parametrize("corpid,corpsecret,errmsg", get_datas()[0], ids=get_datas()[1])
    def test_get_token(self, corpid, corpsecret, errmsg):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": get_token_url
        }
        r = self.gettoken.send_and_requests(req)
        assert r.json()["errmsg"] == errmsg
