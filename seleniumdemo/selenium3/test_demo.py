# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/11/16 14:29
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,acctid,phone,result", [("aaa", 12345, 13711111111, "保存成功")],
                             ids={"add member success"})
    def test_addmember(self, username, acctid, phone, result):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(1)
        js_tips = self.driver.find_element(By.ID, "js_tips").text
        assert js_tips == result
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert username in namelist

    @pytest.mark.parametrize("username,acctid,phone", [("bbb", 123456, 13711111112)]
        , ids={"add member fail"})
    def test_addmember_fail(self, username, acctid, phone):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(acctid)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel").click()
        self.driver.find_element(By.CSS_SELECTOR, "[node-type='cancel']").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert username not in namelist

    @pytest.mark.parametrize("username,acctid,phone,result", [("ccc", 1234567, 13711111113, "保存成功")],
                             ids={"contact add member success"})
    def test_contact_addmember(self, username, acctid, phone, result):
        self.driver.find_element(By.ID, "menu_contacts").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".ww_operationBar .js_add_member")))
        while True:
            self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            try:
                if self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save") is not None:
                    break
            except:
                print("再次点击")
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(acctid)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(1)
        get_tips = self.driver.find_element(By.CSS_SELECTOR, ".success").text
        assert get_tips == result
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert username in namelist

    @pytest.mark.parametrize("username1,username2,result", [("aaa", "ccc", "删除成功")],
                             ids={"delete member success"})
    def test_delete_member(self, username1, username2, result):
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        if username1 and username2 not in namelist:
            print(f"不存在成员{username1}或{username2}")
        else:
            self.driver.find_element(By.XPATH, f"//*[@title='{username1}']/..//*[@class='ww_checkbox']").click()
            self.driver.find_element(By.XPATH, f"//*[@title='{username2}']/..//*[@class='ww_checkbox']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_delete").click()
        self.driver.find_element(By.CSS_SELECTOR, "[d_ck='submit']").click()
        sleep(1)
        get_tips = self.driver.find_element(By.CSS_SELECTOR, ".success").text
        assert get_tips == result
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert username1 and username2 not in namelist
