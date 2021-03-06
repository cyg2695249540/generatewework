# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/11/23 14:10
import requests
from jsonpath import jsonpath


class TestDemo:
    def setup_class(self):
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=get_token_url)
        self.token = r.json()["access_token"]

    def test_create_department(self):
        create_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 3,
            "id": 4
        }
        r = requests.post(url=create_department_url, json=data)
        backjson = {
            "errcode": 0,
            "errmsg": "created",
            "id": 4
        }
        assert r.json() == backjson
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        re = requests.get(url=get_department_list_url)
        departmentname = jsonpath(re.json(), "$..department[?(@.id==4)].name")[0]
        assert departmentname == "技术部"

    def test_update_department(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": 4,
            "name": "测试研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_url, json=data)
        backjson = {
            "errcode": 0,
            "errmsg": "updated"
        }
        assert r.json() == backjson
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        re = requests.get(url=get_department_list_url)
        departmentname = jsonpath(re.json(), "$..department[?(@.id==4)].name")[0]
        assert departmentname == "测试研发中心"

    def test_delete_department(self):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=4"
        r = requests.get(url=delete_url)
        backjson = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        assert r.json() == backjson
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        departmentidlist = jsonpath(list, "$..id")
        assert 4 not in departmentidlist

    def test_addmember(self):
        addmember_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "13711111111",
            "department": [1]
        }
        r = requests.post(url=addmember_url, json=data)
        backjson = {
            "errcode": 0,
            "errmsg": "created"
        }
        assert r.json() == backjson
        get_memberdetail_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=zhangsan"
        memberdetail = requests.get(url=get_memberdetail_url).json()
        username = jsonpath(memberdetail, "$..name")[0]
        assert username == "张三"

    def test_update_member(self):
        update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "zhangsan",
            "name": "张三1",
            "mobile": "13711111111",
            "department": [1]
        }
        r = requests.post(url=update_member_url, json=data)
        backjson = {
            "errcode": 0,
            "errmsg": "updated"
        }
        assert r.json() == backjson
        get_memberdetail_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=zhangsan"
        memberdetail = requests.get(url=get_memberdetail_url).json()
        username = jsonpath(memberdetail, "$..name")[0]
        assert username == "张三1"

    def test_delete_member(self):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=zhangsan"
        r = requests.get(url=delete_member_url)
        backjson = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        assert r.json() == backjson
        get_department_member_list = f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={self.token}&department_id=1"
        department_member_list = requests.get(url=get_department_member_list).json()
        print(department_member_list)
        department_member_name_list = jsonpath(department_member_list, "$..name")
        assert "张三1" not in department_member_name_list
