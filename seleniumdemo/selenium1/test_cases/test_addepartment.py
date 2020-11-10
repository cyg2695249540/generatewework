# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addepartment.py
# @Author   : Pluto.
# @Time     : 2020/11/6 17:24
import allure
import pytest
import yaml

from seleniumdemo.selenium1.pages.main_page import MainPage


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    addepartment = datas["addepartment"]
    case1 = datas["case5"]
    addepartmentfail = datas["addepartmentfail"]
    case2 = datas["case6"]
    return addepartment, case1, addepartmentfail, case2


@allure.feature("添加部门")
class TestAddepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.story("添加部门成功")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("departmentname", get_datas()[0], ids=get_datas()[1])
    def test_addepartment(self, departmentname):
        departmentnamelist = self.main.goto_contactpage().goto_addepartment_page().addepartment(
            departmentname).save_department().get_department_list()
        assert departmentname in departmentnamelist

    @allure.story("取消添加部门")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("departmentname", get_datas()[2], ids=get_datas()[3])
    def test_addepartment_cancel(self, departmentname):
        departmentnamelist = self.main.goto_contactpage().goto_addepartment_page().addepartment(
            departmentname).cancel_department().get_department_list()
        assert departmentname not in departmentnamelist