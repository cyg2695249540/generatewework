# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_member.py
# @Author   : Pluto.
# @Time     : 2020/11/23 14:35
import allure
import pytest
import yaml

from Interfacedemo.Interface1123.apis.member_api import MemberApi1123


def getdatas():
    datas = yaml.safe_load(open("../datas/member_case", encoding="utf-8"))
    create_member = datas["create_member"]
    case1 = datas["case1"]
    update_member = datas["update_member"]
    case2 = datas["case2"]
    delete_member = datas["delete_member"]
    case3 = datas["case3"]
    return create_member, case1, update_member, case2, delete_member, case3


@allure.feature("成员模块")
class TestMember:
    def setup_class(self):
        self.member = MemberApi1123()
        token_info = yaml.safe_load(open("config.yaml", encoding="utf-8"))
        department_secret = token_info["token_info"]["department_secret"]
        self.member.get_token(department_secret)

    @allure.story("添加成员")
    @pytest.mark.parametrize("name,userid", getdatas()[0], ids=getdatas()[1])
    def test_addmember(self, name, userid):
        r = self.member.addmember(name)
        backjson = {
            "errcode": 0,
            "errmsg": "created"
        }
        assert r == backjson
        memberdetail = self.member.get_memberdetail(userid)
        username = self.member.base_jsonpath(memberdetail, "$..name")[0]
        assert username == name

    @allure.story("更新成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name,userid", getdatas()[2], ids=getdatas()[3])
    def test_update_member(self, name, userid):
        r = self.member.update_member(name)
        backjson = {
            "errcode": 0,
            "errmsg": "updated"
        }
        assert r == backjson
        memberdetail = self.member.get_memberdetail(userid)
        username = self.member.base_jsonpath(memberdetail, "$..name")[0]
        assert username == name

    @allure.story("删除成员")
    @pytest.mark.parametrize("name, userid", getdatas()[4], ids=getdatas()[5])
    def test_delete_member(self, name, userid):
        r = self.member.delete_member(userid)
        backjson = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        assert r == backjson
        department_member_list = self.member.get_department_member_list()
        department_member_name_list = self.member.base_jsonpath(department_member_list, "$..name")
        assert name not in department_member_name_list

    @allure.story("读取成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("userid", [("zhangsan")], ids={"get memberdetail"})
    def test_get_memberdetail(self, userid):
        # backjson = self.member.get_memberdetail(userid)
        # schemajson = json.load(open("./json_schema/get_memberdetail_schema.json", encoding="utf-8"))
        # self.member.base_jsonschema(backjson, schemajson)
        pass

    @allure.story("获取部门成员")
    @pytest.mark.flaky(reruns=1)
    def test_get_department_member_list(self):
        # backjson = self.member.get_department_member_list()
        # schemajson = json.load(open("./json_schema/get_department_member_list_schema.json", encoding="utf-8"))
        # self.member.base_jsonschema(backjson, schemajson)
        pass
