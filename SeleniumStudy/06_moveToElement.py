#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  06_moveToElement.py 
    @CreateTime     :  2020/4/11 10:22 下午
    @Software       :  PyCharm
    @Description    : 
"""
from selenium import webdriver
from selenium.webdriver import ActionChains

wb = webdriver.Chrome()
wb.implicitly_wait(8)

wb.get('http://www.baidu.com')

ac = ActionChains(wb)

element = wb.find_element_by_css_selector('[name="tj_briicon"]')

# 鼠标移动到 元素上
ac.move_to_element(element).perform()


wb.quit()
