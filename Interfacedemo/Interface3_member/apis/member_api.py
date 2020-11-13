# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : member_api.py
# @Author   : Pluto.
# @Time     : 2020/11/13 16:25
from Interfacedemo.Interface3_member.apis.wework import WeWork


class MemberApi(WeWork):
    def addmember(self,name):
        addmember_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "zhangsan",
            "name": name,
            "mobile": "13711111111",
            "department": [1]
        }
        req = {
            "method": "post",
            "url": addmember_url,
            "json": data
        }
        r = self.send_and_requests(req)
        return r.json()

    def update_member(self,name):
        update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "zhangsan",
            "name": name,
            "mobile": "13711111111",
            "department": [1]
        }
        req = {
            "method": "post",
            "url": update_member_url,
            "json": data
        }
        r = self.send_and_requests(req)
        return r.json()

    def delete_member(self,userid):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        req = {
            "method": "get",
            "url": delete_member_url
        }
        r = self.send_and_requests(req)
        return r.json()

    def get_memberdetail(self,userid):
        get_memberdetail_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        req = {
            "method": "get",
            "url": get_memberdetail_url
        }
        r = self.send_and_requests(req)
        return r.json()

    def get_department_member_list(self):
        get_department_member_list = f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={self.token}&department_id=1"
        req = {
            "method": "get",
            "url": get_department_member_list
        }
        r = self.send_and_requests(req)
        return r.json()
