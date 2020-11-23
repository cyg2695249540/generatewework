# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2020/11/23 14:35
import json

import allure
import pytest
import yaml

from Interfacedemo.Interface1123.apis.department_api import DepartmentApi


def getdatas():
    datas = yaml.safe_load(open("../datas/department_case", encoding="utf-8"))
    create_department = datas["create_department"]
    case1 = datas["case1"]
    update_department = datas["update_department"]
    case2 = datas["case2"]
    delete_department = datas["delete_department"]
    case3 = datas["case3"]
    return create_department, case1, update_department, case2, delete_department, case3


@allure.feature("部门模块")
class TestDepartment:
    def setup(self):
        self.department = DepartmentApi()
        token_info = yaml.safe_load(open("config.yaml", encoding="utf-8"))
        department_secret = token_info["token_info"]["department_secret"]
        self.department.get_token(department_secret)

    @allure.story("添加部门")
    # @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("department_name, department_id", getdatas()[0], ids=getdatas()[1])
    def test_addmember(self, department_name, department_id):
        r = self.department.create_department(department_name, department_id)
        backjson = {
            "errcode": 0,
            "errmsg": "created",
            "id": department_id
        }
        assert r == backjson
        departmentlist = self.department.get_departmemt_list()
        departmentname = self.department.base_jsonpath(departmentlist,
                                                       f"$..department[?(@.id=={department_id}).name]")[0]
        assert departmentname == department_name

    @allure.story("更新部门")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("department_name,department_id", getdatas()[2], ids=getdatas()[3])
    def test_update_department(self, department_name, department_id):
        r = self.department.update_department(department_name, department_id)
        backjson = {
            "errcode": 0,
            "errmsg": "updated"
        }
        assert r == backjson
        departmentlist = self.department.get_departmemt_list()
        departmentname = self.department.base_jsonpath(departmentlist,
                                                       f"$..department[?(@.id=={department_id})].name")[0]
        assert departmentname == department_name

    @allure.story("删除部门")
    @pytest.mark.parametrize("department_id", getdatas()[4], ids=getdatas()[5])
    def test_delete_department(self, department_id):
        r = self.department.delete_department(department_id)
        backjson = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        assert r == backjson
        list = self.department.get_departmemt_list()
        departmentids = self.department.base_jsonpath(list, "$..id")
        assert department_id not in departmentids

    @allure.story("字段校验")
    @pytest.mark.flaky(reruns=1)
    def test_get_department_list(self):
        list = self.department.get_departmemt_list()
        schemalist = json.load(open("./json_schema/get_list_schema.json", encoding="utf-8"))
        self.department.base_jsonschema(list, schemalist)
