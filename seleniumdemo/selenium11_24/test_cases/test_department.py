# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2020/11/24 19:12
import allure
import pytest
import yaml

from seleniumdemo.selenium11_24.pages.main_page import MainPage1124


def getdatas():
    datas = yaml.safe_load(open("../datas/department.yml", encoding="utf-8"))
    addepartment = datas["addepartment"]
    case1 = datas["case1"]
    addepartmentfail = datas["addepartmentfail"]
    case2 = datas["case2"]
    deletedepartment = datas["deletedepartment"]
    case3 = datas["case3"]
    return addepartment, case1, addepartmentfail, case2, deletedepartment, case3


@allure.feature("部门模块")
class TestAddepartment:
    def setup(self):
        self.main = MainPage1124()

    def teardown(self):
        self.main.driver.quit()

    @allure.story("添加部门成功")
    # @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("departmentname,result", getdatas()[0], ids=getdatas()[1])
    def test_addepartment(self, departmentname, result):
        result_text = self.main.goto_contact_page().goto_addepartment_page().addepartment(
            departmentname).save_department().get_tips_text()
        assert result_text == result
        departmentnamelist = self.main.goto_contact_page().get_department_list()
        assert departmentname in departmentnamelist

    @allure.story("取消添加部门")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("departmentname", getdatas()[2], ids=getdatas()[3])
    def test_addepartment_cancel(self, departmentname):
        departmentnamelist = self.main.goto_contact_page().goto_addepartment_page().addepartment(
            departmentname).cancel_department().get_department_list()
        assert departmentname not in departmentnamelist

    @allure.story("删除部门成功")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("departmentname,result", getdatas()[4], ids=getdatas()[5])
    def test_delete_department(self, departmentname, result):
        result_text = self.main.goto_contact_page().delete_department(departmentname).get_tips_text()
        assert result_text == result
        departmentnamelist = self.main.goto_contact_page().get_department_list()
        assert departmentname not in departmentnamelist