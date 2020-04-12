#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  Student_Manage_System.py
    @Description    :  
    @CreateTime     :  2020/3/29 12:12 上午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
# 等待存储所有学员的信息
info = []

# 添加学员信息字典
info_dict = {}


# 定义功能界面函数
def info_print():
    """ 功能界面显示 """
    print("-" * 20)
    print("请选择功能：")
    print("1、添加学员")
    print("2、删除学员")
    print("3、修改学员")
    print("4、查询学员")
    print("5、显示所有学员")
    print("6、退出系统")

    print("-" * 20)


# 添加学员信息
def add_info():
    """添加学习函数"""
    # 1. 用户输入：学号、姓名、手机号
    new_id = input("请输入学员学号：")
    new_name = input("请输入学员姓名：")
    new_tel = input("请输入学员手机号：")

    # 2. 判断是否添加了这个学员：如果学员姓名已经存在报错提示；如果姓名不存在添加数据
    # 2.1 不允许姓名重复：判断用户输入的姓名 和 列表中字段的 name 对应的值相等 提示
    for item in info:
        if item["name"] == new_name:
            print("用户已经存在")
            return

    # 2.2 如果输入的姓名不存在，添加数据；准备空字典，字典新增数据，列表追加字典

    # 字典新增数据
    info_dict["id"] = new_id
    info_dict["name"] = new_name
    info_dict["tel"] = new_tel

    # 列表追加字典
    info.append(info_dict)
    print("已添加成功")


# 删除学院信息
def del_info():
    """ 删除学员 """
    # 1. 用户输入要删除的学员的姓名
    del_name = input("请输入要删除的学员的姓名：")
    # 2. 判断学员是否存在：存在则删除，不存在提示
    # 2.1 声明info是全局变量
    # 2.2 遍历列表
    for item in info:
        # 2.3 判断学员是否存在，存在执行删除（列表里的字典），break： 这个系统不允许重名，删除一个后面的不需要再遍历，不存在提示
        if del_name == item["name"]:
            info.remove(item)
            print("删除 %s 学员成功" % del_name)
            break
    else:
        print("%s 学员不存在" % del_name)


# 修改学员信息
def modify_info():
    """修改学员信息"""
    # 1. 用户输入想要的修改的学员的姓名
    modify_name = input("请输入要修改学员姓名：")

    # 2. 判断学员是否存在，存在修改手机号码，不存在，提示
    # 遍历列表，判断输入的 姓名==字典["name"]
    for item in info:
        if modify_name == item["name"]:
            # 将tel的这个key修改值，并终止此循环
            item["tel"] = input("请输入要修改的手机号码：")
            print("您要修改的 %s 学员已成功" % modify_name)
            break
    else:
        print("您要修改 %s 学员不存在" % modify_name)


# 查询学员信息
def search_info():
    """查询学员信息"""
    # 1. 输入目标学员姓名
    search_name = input("请输入要查询的学生姓名：")

    # 2. 检查学习是否存在，存在打印这个学员的信息，不存在则提示
    for item in info:
        if search_name == item["name"]:
            print("您查询的 %s 学员信息如下：" % search_name)
            print("学号：%s, 姓名：%s, 手机：%s " % (item["id"], item["name"], item["tel"]))
            break
    else:
        print("您查询 %s 学员不存在" % search_name)


# 显示所有学员
def show_info():
    """显示所有学员信息"""
    print("所有学员信息如下：")
    print("学号\t姓名\t手机")
    for item in info:
        print("%s\t%s\t%s" % (item["id"], item["name"], item["tel"]))


while True:
    # 1. 显示功能界面
    info_print()

    # 2. 用户输入功能序号
    user_num = input("请输入功能序号：")

    # 3. 按照用户输入的功能序号，执行不能的功能函数

    if user_num == "1":
        print("添加学员")
        add_info()

    elif user_num == "2":
        print("删除")
        del_info()

    elif user_num == "3":
        print("修改")
        modify_info()

    elif user_num == "4":
        print("查询")
        search_info()

    elif user_num == "5":
        print("显示")
        show_info()

    elif user_num == "6":
        exit_flag = input("您确定退出系统？yes or no ：")
        if exit_flag == "yes" or exit_flag == "Yes":
            print("退出系统")
            break

    else:
        print("输入内容错误")
