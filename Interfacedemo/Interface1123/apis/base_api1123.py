# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_api1123.py
# @Author   : Pluto.
# @Time     : 2020/11/23 14:36
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi1123:
    def send_and_request(self, req: dict):
        return requests.request(**req)

    def base_jsonpath(self, obj, expr):
        return jsonpath(obj, expr)

    def base_jsonschema(self, instance, schema):
        return validate(instance, schema)
