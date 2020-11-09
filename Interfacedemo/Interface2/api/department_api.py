# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : department_api.py
# @Author   : Pluto.
# @Time     : 2020/11/9 11:20

from Interfacedemo.Interface2.api.wework import WeWork


class DepartmentApi(WeWork):
    def create_department(self, department_name, department_id):
        create_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": department_name,
            "name_en": "JSB",
            "parentid": 1,
            "order": 3,
            "id": department_id
        }
        req = {
            "method": "post",
            "url": create_department_url,
            "json": data
        }
        r = self.send_and_requests(req)
        return r.json()

    def update_department(self, department_name, department_id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": department_id,
            "name": department_name,
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        req = {
            "method": "post",
            "url": update_url,
            "json": data
        }
        r = self.send_and_requests(req)
        return r.json()

    def delete_department(self, department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        req = {
            "method": "get",
            "url": delete_url
        }
        r = self.send_and_requests(req)
        return r.json()

    def get_departmemt_list(self):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            "method": "get",
            "url": get_department_list_url
        }
        list = self.send_and_requests(req)
        return list.json()
