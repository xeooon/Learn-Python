# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

"""
标题 : 24期周末班 - day07 - 习题
作者 : 张志强
QQ号 : 1344683865
微信 : qingniaoxiaoqiang
邮箱 : Xeon@xeon.org.cn
"""


# ###################################### 习 题 #######################################


'''
1、计算两个格式化时间之间差了多少年月日时分秒
'''
# import time
# def func1():
#     # 将格式化好的时间交给mktime转化为时间戳
#     set_time = time.mktime(time.strptime('2011-11-11 11:11:11', '%Y-%m-%d %H:%M:%S'))
#     now_time = time.time()
#
#     # 获取相差的时间戳
#     dif_time = now_time - set_time
#
#     # 用格林威治时间，加上当前的时间差
#     struct_time = time.gmtime(dif_time)
#     print('时间相差: %d年%d月%d日%d时%d分%d秒' % (struct_time.tm_year - 1970, struct_time.tm_mon - 1,
#                                                 struct_time.tm_mday - 1, struct_time.tm_hour,
#                                                 struct_time.tm_min, struct_time.tm_sec))
# func1()


'''
2、计算当前时间所在月1号的时间戳
'''
# import time
# def func2():
#     now_time = time.localtime()  # 获取当前的时间戳
#     print('当前时间所在月1号的时间戳为：%d年%d月%d日%d时%d分%d秒' % (now_time.tm_year, now_time.tm_mon, 1,
#                                                  now_time.tm_hour, now_time.tm_min, now_time.tm_sec))
# func2()


'''
3、生成一个6位随机验证码(包含数字和大小写字母)
'''
# import random
# def code():
#     char0 = ''
#     for i in range(6):
#         char1 = str(random.randint(0, 9))  # 需要转换为str取ascii的 0-9
#         char2 = chr(random.randint(33, 47))  # 取ascii的 !-/
#         char3 = chr(random.randint(65, 90))  # 取ascii的 A-Z
#         char4 = chr(random.randint(97, 122))  # 取ascii的 a-z
#         char5 = random.choice([char1, char2, char3, char4])  # 随机取char1,char2,char3,char4的一个值
#         char0 += char5
#     return char0
# print(code())


'''
4、发红包、制定金额和个数随机分配红包金额
'''
# import random
# def Red_packet(money, count):
#     miss = money * 100  # 避免浮点数
#     lis = []
#     for i in range(count - 1):  # 为什么要减1, 保证留一个
#         num = random.randrange(miss + 1)  # 在range的数字中取一个数
#         lis.append(num / 100)  # 把随机出来的数放到列表里
#         miss -= num
#     lis.append(miss / 100)  # 把剩下的数放到列表里
#     return lis
# print(Red_packet(1, 10))


'''
5、分别列出给定目录下所有的文件和文件夹
'''
# import os
# path5 = os.path.dirname(__file__)
# print(os.listdir(path5))


'''
6、获取当前文件所在目录
'''
# import os
# print(os.getcwd())


'''
7、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
'''
# import os
# import sys
#
# def func(dir,file):
#     if os.path.isdir(dir):
#         print('%s目录已存在.' % dir)
#     else:
#         os.mkdir(dir)
#         print('%s目录创建成功.' % dir)
#         if sys.platform == 'darwin':  # 我的mac os 平台名
#             f = os.path.dirname(__file__) + '/' + dir + '/' + file
#             with open(f, encoding='utf-8', mode='a') as f1:
#                 f1.write('在%s目录下建立了一个%s文件' % (dir, file))
#                 print('%s文件创建成功.' % file)
#         else:
#             win = '\%s\%s' % (dir, file)
#             f = os.path.dirname(__file__) + win
#             with open(f, encoding='utf-8', mode='a') as f1:
#                 f1.write('在%s目录下建立了一个%s文件' % (dir, file))
#                 print('%s文件创建成功.' % file)
#
# func('xeon', 'f1')


'''
8、计算某路径下所有文件和文件夹的总大小
'''
# import os
# path8 = os.path.dirname(__file__)
# print(os.path.getsize(path8))
