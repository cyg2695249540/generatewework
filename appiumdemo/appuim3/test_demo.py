# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/11/17 18:36
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Z91QGEWM2258H"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清除数据
        caps["noReset"] = True
        # # 不重启应用
        # caps["dontStopAppOnReset"] = True
        # 等待页面空闲的时间
        caps['settings[waitForIdleTimeout]'] = 1
        # 跳过安装，权限设置等操作
        caps["skipDeviceInitialization"] = True
        # 设置可输入中文
        caps["unicodekeyBoard"] = True
        caps["resetkeyBoard"] = True
        # 自动判断弹框
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_send_message(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6n").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpg").send_keys("软件测试")
        sleep(1)
        eles = self.driver.find_elements(MobileBy.XPATH, "//*[@text='软件测试']")
        if len(eles) < 2:
            print("没有该群")
        else:
            eles[-1].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eo7").send_keys("test11.17")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eo3").click()
        news = self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/ens")
        assert "test11.17" == news[-1].text

    def test_dake(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hr_").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        r = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/oy").text
        assert r == "外出打卡成功"

    @pytest.mark.parametrize("name, gander, phone", [("LCQ", "女", 13711111111)], ids={"addmember"})
    def test_addmember(self, name, gander, phone):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@resource-id='com.tencent.wework:id/b4t']").send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gander == "女":
            searchtext = (MobileBy.XPATH, "//*[@text='女']")
            element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(searchtext))
            element.click()
        else:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@text='男']")))
            element.click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert mytoast == "添加成功"

    @pytest.mark.parametrize("name", [("LCQ")], ids={"delete member"})
    def test_deletecontact(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6n").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpg").send_keys(name)
        sleep(1)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        before = len(eles)
        if before == 1:
            print(f"没有名为{name}的成员")
        else:
            eles[1].click()
        sleep(1)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6d").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(5)
        eles2 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        after = len(eles2)
        assert after == before - 1
        result2 = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ccl").text
        assert result2 == "无搜索结果"
