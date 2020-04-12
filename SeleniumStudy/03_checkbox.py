#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  03_checkbox.py
    @CreateTime     :  2020/4/11 9:19 下午
    @Software       :  PyCharm
    @Description    : 
"""

from selenium import webdriver

wb = webdriver.Chrome()
wb.implicitly_wait(8)

# 打开示例链接
wb.get("http://cdn1.python3.vip/files/selenium/test2.html")

# 先把 已经选中的选项全部点击一下
elements = wb.find_elements_by_css_selector("#s_checkbox input[checked=checked]")

for element in elements:
    element.click()

# 再点击 小雷老师
wb.find_element_by_css_selector("#s_checkbox input[value='小雷老师']").click()

wb.quit()
