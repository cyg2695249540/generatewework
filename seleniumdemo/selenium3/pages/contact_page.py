# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/11/16 15:19
from selenium.webdriver.common.by import By

from seleniumdemo.selenium3.pages.base_page import BasePage


class ContactPage(BasePage):
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    _delete_butto = (By.CSS_SELECTOR, ".js_delete")
    _determine = (By.CSS_SELECTOR, "[d_ck='submit']")

    _addmember_butto = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")

    _create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _addepartment = (By.CSS_SELECTOR, ".js_create_party")
    _jstree_anchor = (By.CSS_SELECTOR, ".jstree-anchor")

    def get_member_list(self):
        self.wait_for_clickable(self._member_list)
        eles = self.finds(self._member_list)
        return [name.text for name in eles]

    def goto_addmember_page(self):
        from seleniumdemo.selenium2.pages.addmember_page import AddmemberPage
        self.wait_for_clickable(self._addmember_butto)
        while True:
            self.find_and_click(self._addmember_butto)
            try:
                if self.find(self._cancel_member) is not None:
                    break
            except:
                print("再次点击")
        return AddmemberPage(self.driver)

    def deletemember(self, username1,username2):
        deletename_checkbox1 = (By.XPATH, f"//*[@title='{username1}']/..//*[@class='ww_checkbox']")
        deletename_checkbox2 = (By.XPATH, f"//*[@title='{username2}']/..//*[@class='ww_checkbox']")
        eles = self.finds(self._member_list)
        namelist = [name.text for name in eles]
        if username1 and username2 in namelist:
            self.find_and_click(deletename_checkbox1)
            self.find_and_click(deletename_checkbox2)
            self.find_and_click(self._delete_butto)
            self.find_and_click(self._determine)
        else:
            print(f"不存在成员{username1}和{username2}")
        return self

    def goto_addepartment_page(self):
        from seleniumdemo.selenium2.pages.addpartment_page import AdDepartmentPage
        self.find_and_click(self._create_dropdown)
        self.find_and_click(self._addepartment)
        return AdDepartmentPage(self.driver)

    def get_department_list(self):
        self.wait_for_clickable(self._jstree_anchor)
        eles = self.finds(self._jstree_anchor)
        return [name.text for name in eles]

    def delete_department(self, departmentname):
        search_department = (By.LINK_TEXT, f"{departmentname}")
        botto = (By.CSS_SELECTOR, ".jstree-clicked .jstree-contextmenu-hover")
        delete = (By.CSS_SELECTOR, "[rel='3']")
        self.find_and_click(search_department)
        self.find_and_click(botto)
        self.find_and_click(delete)
        self.find_and_click(self._determine)
        return self
