#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  04_select.py 
    @CreateTime     :  2020/4/11 10:02 下午
    @Software       :  PyCharm
    @Description    : 
"""

from selenium import webdriver
# 导入Select类
from selenium.webdriver.support.select import Select

wb = webdriver.Chrome()
wb.implicitly_wait(8)

# 打开示例链接
wb.get("http://cdn1.python3.vip/files/selenium/test2.html")

# 创建Select对象
select = Select(wb.find_element_by_id("ss_single"))

# 通过 Select 对象选中小雷老师
select.select_by_visible_text("小雷老师")

wb.quit()
