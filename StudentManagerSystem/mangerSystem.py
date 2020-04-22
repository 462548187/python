#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  mangerSystem.py
    @Description    :  
    @CreateTime     :  2020/4/5 1:24 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""
from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据 -- 列表
        self.student_list = []

    # 一、 程序入库函数
    def run(self):
        # 1. 加载文件里面的学员数据
        self.load_student()

        while True:
            # 2. 显示功能菜单
            self.show_menu()

            # 3. 用户输入目标功能序号
            menu_num = input('请输入您需要的功能序号：')

            # 4. 根据用户输入的序号执行不同的功能 -- 如果用户输入1. 执行添加
            if menu_num == "1":
                # 添加学员
                self.add_student()

            elif menu_num == "2":
                # 删除学员信息
                self.del_student()

            elif menu_num == "3":
                # 修改学员信息
                self.modify_student()

            elif menu_num == "4":
                # 查询学员信息
                self.search_student()

            elif menu_num == "5":
                # 显示所有学员信息
                self.show_student()

            elif menu_num == "6":
                # 保存学员信息
                self.save_student()

            elif menu_num == "7":
                # 退出系统 -- 退出循环
                break

    # 二、 系统功能函数
    # 2.1 显示功能菜单 -- 打印序号的功能对应关系 -- 静态
    @staticmethod
    def show_menu():
        print("请选择如下功能：")
        print("1:添加学员信息")
        print("2:删除学员信息")
        print("3:修改学员信息")
        print("4:查询学员信息")
        print("5:显示所有学员信息")
        print("6:保存学员信息")
        print("7:退出系统")

    # 2.2 添加学员
    def add_student(self):
        # print("添加学员")
        # 1. 用户输入姓名、性别、手机号码
        name = input("请输入您的姓名：")
        gender = input("请输入您的性别：")
        tel = input("请输入您的手机号：")

        # 2. 创建学员对象 -- 类？ 类的student 文件里，先导入student模块，在创建对象
        student = Student(name, gender, tel)

        # 3. 将该对象添加到学员列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 2.3 删除学员
    def del_student(self):
        # print("删除学员")
        # 1. 用户旧目标学员姓名
        del_name = input("请输入要删除的学员姓名：")

        # 2. 遍历学员列表，如果用户输入的学员存在则删除学员对象，否则提示学员不存在
        for item in self.student_list:
            if item.name == del_name:
                self.student_list.remove(item)
                print("删除功能")
                break
        else:
            # 循环正常结束执行的代码：循环结束都没有删除任何一个对象，所以说明用户输入的目标学员不存在
            print("查无此人")

        # 打印学员列表，验证删除功能
        print(self.student_list)

    # 2.4 修改学员
    def modify_student(self):
        # print("修改学员")
        # 1. 用户输入目标学员姓名
        modify_name = input("请输入要修改的学员姓名：")

        # 2. 遍历列表数据，如果学员存在修改姓名、性别、手机号，否则提示学员不存在
        for item in self.student_list:
            if item.name == modify_name:
                item.name = input("姓名：")
                item.gender = input("性别：")
                item.tel = input("手机号：")
                print(f"修改的学员信息成功，姓名{item.name}, 性别{item.gender}, 手机号{item.tel}")
                break
        else:
            print("查无此人")

        print(self.student_list)

    # 2.5 查询学员信息
    def search_student(self):
        # print("查询学员")
        # 1. 用户输入目标学员姓名
        search_name = input("请输入您要搜索的学员姓名：")

        # 2. 遍历学员列表，如果学员存在就打印学员信息，否则提示学员不存在
        for item in self.student_list:
            if item.name == search_name:
                print(f"姓名是{item.name}, 性别是{item.gender}, 手机号是{item.tel}")
                break
        else:
            print("查无此人")

        print(self.student_list)

    # 2.6 显示所有学员信息
    def show_student(self):
        # print("显示所有学员信息")
        # 1. 打印表头
        print("姓名\t性别\t手机号")

        # 2. 打印学员数据
        for item in self.student_list:
            print(f"{item.name}\t{item.gender}\t{item.tel}")

    # 2.7 保存学员信息
    def save_student(self):
        # print("保存学员信息")
        # 1. 打开文件
        f = open("student.data", "w")
        # 2. 文件写入数据
        # 2.1 [学员对象]转换成[字典] -- 列表推导式
        new_list = [item.__dict__ for item in self.student_list]

        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        # print("加载学员信息")
        # 1. 打开文件：尝试r打开，如果有异常w
        try:
            f = open("student.data", "r")
        except:
            f = open("student.data", "w")
        # 2. 读取数据：文件读取的数据是字符串还原列表类型；[{}]转换[学员对象]
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(item["name"], item["gender"], item["tel"]) for item in new_list]

        # 3. 关闭文件
        finally:
            f.close()
