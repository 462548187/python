#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  02_radio.py 
    @CreateTime     :  2020/4/11 9:19 下午
    @Software       :  PyCharm
    @Description    : 
"""

from selenium import webdriver

wb = webdriver.Chrome()
wb.implicitly_wait(8)

# 打开示例链接
wb.get("http://cdn1.python3.vip/files/selenium/test2.html")

# 获取当前选中的元素
ele = wb.find_element_by_css_selector("#s_radio input[checked=checked]")

# 打印默认选中的radio
print("当前选中的是：" + ele.get_attribute("value"))

# 点选 小雷老师
wb.find_element_by_css_selector("#s_radio input[value='小雷老师']").click()

wb.quit()
