# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_member.py
# @Author   : Pluto.
# @Time     : 2020/11/24 19:12
import allure
import pytest
import yaml

from seleniumdemo.selenium11_24.pages.main_page import MainPage1124


def getdatas():
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
        self.main = MainPage1124()

    def teardown(self):
        self.main.driver.quit()

    @allure.story("添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username,acctid,phone,result", getdatas()[0], ids=getdatas()[1])
    def test_addmember(self, username, acctid, phone, result):
        result_text = self.main.goto_addmember_page().addusername(username).addacctid(acctid).addphone(
            phone).save_member().get_tips_text()
        assert result_text == result
        namelist = self.main.goto_contact_page().get_member_list()
        assert username in namelist

    @allure.story("添加成员失败")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username,acctid,phone", getdatas()[2], ids=getdatas()[3])
    def test_addmember_fail(self, username, acctid, phone):
        namelist = self.main.goto_addmember_page().addusername(username).addacctid(acctid).addphone(
            phone).cancel_member().get_member_list()
        assert username not in namelist

    @allure.story("通讯录添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username, acctid, phone,result", getdatas()[4], ids=getdatas()[5])
    def test_contact_addmember(self, username, acctid, phone, result):
        result_text = self.main.goto_contact_page().goto_addmember_page().addusername(username).addacctid(acctid)\
            .addphone(phone).save_member().get_tips_text()
        assert result_text == result
        namelist = self.main.goto_contact_page().get_member_list()
        assert username in namelist

    @allure.story("删除成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username1,username2,result", getdatas()[6], ids=getdatas()[7])
    def test_delete_member(self, username1, username2, result):
        result_text = self.main.goto_contact_page().deletemember(username1, username2).get_tips_text()
        assert result_text == result
        namelist = self.main.goto_contact_page().get_member_list()
        assert username1 and username2 not in namelist
