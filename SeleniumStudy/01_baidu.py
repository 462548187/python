#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  01_baidu.py
    @Description    :  
    @CreateTime     :  2020/4/11 5:10 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import time

from selenium import webdriver

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# 周期性（每隔半秒钟）重新寻找该元素，直到该元素找到
wd.implicitly_wait(8)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get("http://www.baidu.com")

# 根据id选择元素，返回的就是该元素对应的WebElement对象
baiduElement = wd.find_element_by_id("kw")

# 清除输入框已有的字符串
baiduElement.clear()

# 输入字符串
baiduElement.send_keys("趣海囤\n")

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
elementLeft = wd.find_element_by_id("content_left")
# print(element.get_attribute("outerHTML"))

# 选择css中 href 元素
link = elementLeft.find_element_by_css_selector("h3.t a[href]")
print(link.get_attribute("outerHTML"))

# Element对象的 click方法
link.click()

# 等待2s
time.sleep(2)

# mainWindow变量保存当前窗口的句柄
mainWindow = wd.current_window_handle

# 遍历浏览器全部窗口
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if "儿童优品" in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

print("-" * 50)
print(wd.title)
print("-" * 50)

qLink = wd.find_element_by_css_selector("div.news-r a.tit")
print(qLink.get_attribute("outerHTML"))

qLink.click()

# 等待5s
time.sleep(5)

# 通过前面保存的老窗口的句柄，自己切换到老窗口 -- baidu.com
wd.switch_to.window(mainWindow)

# 清除输入框已有的字符串
baiduElement.clear()

# 重新搜索关键词 宜信
baiduElement.send_keys("宜信\n")

# 等待5s
time.sleep(5)

# 关闭浏览器
wd.quit()
