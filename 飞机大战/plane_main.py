#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  plane_main.py
    @Description    :  
    @CreateTime     :  2020-03-17 15:03
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
import pygame
from plane_sprites import *


class PlaneGame(object):
    """ 飞机大战主游戏 """

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞监测
            self.__check_collide()
            # 4. 更新/绘制精灵
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            # 监听敌机出厂监听
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出厂...")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            # 监听发射子弹方法
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")

        # 使用键盘提供的方法提供按键
        keys_passed = pygame.key.get_pressed()

        # 判断元组中对应的按键索引值 1
        if keys_passed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_passed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pass

    def __update_sprites(self):
        # 背景更新 加载屏幕
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 敌机更新、加载屏幕
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 英雄更新、加载屏幕
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 子弹更新、加载屏幕
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
