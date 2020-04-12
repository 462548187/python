#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :
  ----------------------------------
    @File           :  student.py
    @Description    :
    @CreateTime     :  2020/4/5 1:13 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     :
"""


class Student(object):
    def __init__(self, name, gender, tel):
        # 姓名、性别、手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'


if __name__ == '__main__':
    aa = Student('aa', '女', '13817331916')
    print(aa)
