# 在控制台连续输出五行 * ， 每一行星号的数量依次递增
# *
# **
# ***
# ****
# *****

# 1. 定义一个计数器变量，从数字1开始，循环会比较方便
row = 1

# 2. 开始循环
while row <= 5:

    print("*" * row)
    
    row += 1
