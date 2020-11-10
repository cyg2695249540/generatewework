# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_member.py
# @Author   : Pluto.
# @Time     : 2020/11/10 14:28
from time import sleep

import allure
import pytest
import yaml
from selenium.webdriver.common.by import By

from seleniumdemo.selenium2.pages.main_page import MainPage


def get_datas():
    datas = yaml.safe_load(open("../datas/contact.yml", encoding="utf-8"))
    add1 = datas["add1"]
    case1 = datas["case1"]
    addfail = datas["addfail"]
    case2 = datas["case2"]
    add2 = datas["add2"]
    case3 = datas["case3"]
    del1 = datas["del1"]
    case4 = datas["case4"]
    return add1, case1, addfail, case2, add2, case3, del1, case4


@allure.feature("成员模块")
class TestMember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.story("添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username,acctid,phone,result", get_datas()[0], ids=get_datas()[1])
    def test_addmember(self, username, acctid, phone, result):
        result_tips = self.main.goto_addmember_page().addusername(username).addacctid(acctid).addphone(
            phone).save_member().get_tips_text()
        assert result_tips == result
        namelist = self.main.goto_contact_page().get_member_list()
        assert username in namelist

    @allure.story("添加成员失败")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username,acctid,phone", get_datas()[2], ids=get_datas()[3])
    def test_addmember_fail(self, username, acctid, phone):
        namelist = self.main.goto_addmember_page().addusername(username).addacctid(acctid).addphone(
            phone).cancel_member().get_member_list()
        assert username not in namelist

    @allure.story("通讯录添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username, acctid, phone,result", get_datas()[4], ids=get_datas()[5])
    def test_contact_addmember(self, username, acctid, phone, result):
        get_tips = self.main.goto_contact_page().goto_addmember_page().addusername(username).addacctid(acctid).addphone(
            phone).save_member().get_tips_text()
        assert get_tips == result
        namelist = self.main.goto_contact_page().get_member_list()
        assert username in namelist

    @allure.story("删除成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username,result", get_datas()[6], ids=get_datas()[7])
    def test_delete_member(self, username, result):
        get_tips = self.main.goto_contact_page().deletemember(username).get_tips_text()
        assert get_tips == result
        namelist = self.main.goto_contact_page().get_member_list()
        assert username not in namelist


