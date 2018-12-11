# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import random
# print(random.random())  # 随机在0~1之间的float
# print(random.uniform(1,10)) # 1 ~10 浮点型
# print(random.randint(1,10)) # 1~10 之间的整数  ***
# print(random.randrange(1,10,2)) # 大于等于1且小于10之间的奇数)
#
print(random.choice([1, '23', [4,5]]))  # 多选择一  ***
print(random.sample([1,'23',[4,5], 'alex'],2)) #  列表元素 任意2个组合)

# item = [1, 3, 5, 7, 9]
# random.shuffle(item)  # 打乱次序
#
# print(item)

'''
生成一个随机5位数的验证码
0~9 随机选一个
a~z 随机选一个
两个选一个
'''
# print(chr(97))  # 打印ascii表的a
# print(chr(122))  # 打印ascii表的z
#
# print(chr(65))  # 打印ascii表的A
# print(chr(90))  # 打印ascii表的Z
#
# def code():
#     codes = ''
#     for i in range(5):
#         num = str(random.randint(0, 9))  # 取整数0到9
#         char1 = chr(random.randint(97, 122))  # 取a到z
#         char2 = chr(random.randint(65, 90))   # 取A到Z
#         c1 = random.choice([num, char1, char2])  # 在这三个里面选一个
#         codes += c1
#     return codes
# print(code())


# 随机生成10位密码？？
# def code():
#     codes = ''
#     for i in range(10):
#         num = str(random.randint(0, 9))  # 取整数0到9
#         char1 = chr(random.randint(97, 122))  # 取a到z
#         char2 = chr(random.randint(65, 90))   # 取A到Z
#         char3 = chr(random.randint(33, 47))  # 取!到/
#         char4 = chr(random.randint(58, 64))  # 取:到@
#         c1 = random.choice([num, char1, char2, char3, char4])
#         codes += c1
#     return codes
# print(code())

