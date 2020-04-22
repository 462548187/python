#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  11_screenShot.py 
    @CreateTime     :  2020/4/12 12:10 下午
    @Software       :  PyCharm
    @Description    : 
"""
from selenium import webdriver

wb = webdriver.Chrome()
wb.implicitly_wait(8)

# 打开网站
wb.get('http://www.baidu.com')

# 截屏保存为图片文件
wb.get_screenshot_as_file('1.png')

wb.quit()
