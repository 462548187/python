#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  10_currentUrl.py 
    @CreateTime     :  2020/4/12 12:07 下午
    @Software       :  PyCharm
    @Description    : 
"""
from selenium import webdriver

wb = webdriver.Chrome()

# 打开网站
wb.get('http://www.baidu.com')

# 获取网站标题栏文本
print(wb.title)
# 获取网站的地址文本
print(wb.current_url)

wb.quit()
