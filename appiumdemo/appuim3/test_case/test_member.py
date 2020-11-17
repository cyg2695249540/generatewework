# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_member.py
# @Author   : Pluto.
# @Time     : 2020/11/17 19:04
import allure
import pytest
from ruamel import yaml

from appiumdemo.appuim3.pages.app import App


def getdatas():
    datas = yaml.safe_load(open("../data/addcontact.yml", encoding="utf-8"))
    add = datas["add"]
    case1 = datas["case1"]
    del1 = datas["del1"]
    case2 = datas["case2"]
    return add, case1, del1, case2

@allure.feature("成员模块")
class TestMember:
    def setup(self):
        self.app = App()
        self.main = self.app.startapp().goto_main_page()

    def teardown(self):
        self.app.stopapp()

    @allure.story("成功添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name, gender, phone,toast", getdatas()[0], ids=getdatas()[1])
    def test_addmember(self, name, gender, phone, toast):
        toast_text = self.main.goto_contact_page().goto_invite_member_page().goto_invite_member_detail_page()\
            .addname(name).addgender(gender).addphone(phone).click_save().get_toast_text()
        assert toast_text == toast

    @allure.story("正确删除成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name,resultNone", getdatas()[2], ids=getdatas()[3])
    def test_deletemember(self, name, resultNone):
        result = self.main.goto_contact_page().goto_search_page().searchmember(name).\
            go_to_personal_information_setup_page().go_to_edit_member_page().delete_member().search_result()
        assert result == resultNone
