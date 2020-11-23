# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2020/11/23 14:36
from Interfacedemo.Interface1123.apis.base_api1123 import BaseApi1123


class WeWork1123(BaseApi1123):
    def get_token(self, corpsecret):
        corpid = "ww0ae123b953d2b956"
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": get_token_url
        }
        r = self.send_and_request(req)
        self.token = r.json()["access_token"]
        return self.token
