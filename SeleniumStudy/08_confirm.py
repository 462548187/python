#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  08_confirm.py
    @CreateTime     :  2020/4/11 10:49 下午
    @Software       :  PyCharm
    @Description    : 
"""
import time

from selenium import webdriver

wb = webdriver.Chrome()
wb.implicitly_wait(5)

wb.get('http://cdn1.python3.vip/files/selenium/test4.html')

# --- confirm ---
wb.find_element_by_id('b2').click()

time.sleep(2)

# 打印 弹出框 提示信息
print(wb.switch_to.alert.text)

# 点击 OK 按钮
wb.switch_to.alert.accept()

wb.find_element_by_id('b2').click()
# 点击取消 按钮
wb.switch_to.alert.dismiss()

wb.quit()
