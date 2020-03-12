#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_21_遍历字典的列表.py
    @Description    :  
    @CreateTime     :  2020/3/2 3:09 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

student = [
    {"name": "阿土"},
    {"name": "阿土"},
    {"name": "小美"}
]

# 在学员列表中搜索指定的姓名
find_name = "张三"

for stu_dict in student:

    print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到了 %s" % find_name)

        # 如果已经找到，应该直接退出循环，而不遍历后续的元素
        break

    # else:
    #     print("抱歉没有找到 %s" % find_name)

else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望得到一个统一的提示！
    print("抱歉没有找到 %s" % find_name)

print("循环结束")
