#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_02_使用Rect描述英雄.py
    @Description    :  
    @CreateTime     :  2020-03-16 18:02
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""


import pygame

# x, y, width, height
hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))

print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))

print("%d %d" % hero_rect.size)

