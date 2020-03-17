#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_07_认识游戏循环.py
    @Description    :  
    @CreateTime     :  2020-03-17 9:54
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
# pygame.display.update()


# 绘制英雄的飞机
# 1> 加载图像
hero = pygame.image.load("./images/me1.png")
# 2> 绘制在屏幕
screen.blit(hero, (150, 500))
# 3> 更新显示


# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏的正式开始！
i = 0

# 游戏循环
while True:

    # 可以指定循环体内部的代码的执行的频率
    clock.tick(60)

    print(i)
    i += 1

pygame.quit()

