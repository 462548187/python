#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  09_prompt.py 
    @CreateTime     :  2020/4/12 11:56 上午
    @Software       :  PyCharm
    @Description    : 
"""
import time

from selenium import webdriver

wb = webdriver.Chrome()
wb.implicitly_wait(8)

wb.get("http://cdn1.python3.vip/files/selenium/test4.html")

# --- prompt ---
wb.find_element_by_id("b3").click()

# 获取 alert 对象
alert = wb.switch_to.alert

# 打印 弹出框 提示信息
print(alert.text)

# 输入信息，并且点击 OK 按钮 提交
alert.send_keys('web自动化测试')

time.sleep(3)
alert.accept()

# 点击 Cancel 按钮 取消
wb.find_element_by_id('b3').click()
alert = wb.switch_to.alert
alert.send_keys('取消web自动化')
time.sleep(3)
alert.dismiss()

wb.quit()
