#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_04_绘制图像.py
    @Description    :  
    @CreateTime     :  2020-03-16 18:19
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

import pygame

# 游戏的初始化
pygame.init()

# 创建游戏主窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")

# 2> blit 绘制图像
screen.blit(bg, (0, 0))

# 3> update 更新屏幕显示
pygame.display.update()


# 游戏循环
while True:
    pass


pygame.quit()
