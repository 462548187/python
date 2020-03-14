#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_17_方法综合案例.py
    @Description    :  
    @CreateTime     :  2020/3/14 6:15 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""



class Game(object):

    # 历史最高分
    # 类属性
    top_score = 0

    def __init__(self, name):
        # 初始化方法中，定义了实现属性
        self.player_name = name

    @staticmethod
    def show_help():
        # 定义静态方法
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        # 定义类方法
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        # 定义实例方法
        print("%s 开始游戏啦..." % self.player_name)


# 1. 查看游戏的帮助信息
Game.show_help()

# 2. 查看历史最高分
Game.show_top_score()

# 3. 创建游戏对象
game = Game("小明")

# 用定义的对象去调用实例方法
game.start_game()
