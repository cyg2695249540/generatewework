# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_get_token.py
# @Author   : Pluto.
# @Time     : 2020/11/23 14:35
import pytest
import yaml

from Interfacedemo.Interface1123.apis.base_api1123 import BaseApi1123


def getdatas():
    datas = yaml.safe_load(open("../datas/get_token_case.yaml", encoding="utf-8"))
    demo = datas["demo"]
    case = datas["case"]
    return demo, case


class TestGetToken:
    def setup_class(self):
        self.gettoken = BaseApi1123()

    @pytest.mark.parametrize("corpid,corpsecret,errmsg", getdatas()[0], ids=getdatas()[1])
    def test_get_token(self, corpid, corpsecret, errmsg):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": get_token_url
        }
        r = self.gettoken.send_and_request(req)
        assert r.json()["errmsg"] == errmsg
