# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_member.py
# @Author   : Pluto.
# @Time     : 2020/11/11 20:05
import allure
import pytest
import yaml

from appiumdemo.appium2.pages.app import App


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
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
    @pytest.mark.parametrize("name, gender, phone,toast", get_datas()[0], ids=get_datas()[1])
    def test_addmember(self, name, gender, phone, toast):
        toast_text = self.main.goto_contact_page().goto_invite_member_page().goto_invite_member_detail_page().addname(
            name).addgender(gender).addphone(phone).click_save().get_toast_text()
        assert toast_text == toast

    @allure.story("正确删除成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name,resultNone", get_datas()[2], ids=get_datas()[3])
    def test_deletemember(self, name, resultNone):
        result = self.main.goto_contact_page().goto_search_page().searchmember(
            name).go_to_personal_information_setup_page().go_to_edit_member_page().delete_member().search_result()
        assert result == resultNone