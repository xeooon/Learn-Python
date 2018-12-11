# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
''''''

# s1 = 'asdfasdfasdfadfasdfasf'
# sum = 0
# for i in s1:
#     sum += 1
# print(sum)

# 面向过程编程(流水账)
# 1.代码重复
# 2.可读性差
#

# 一个函数,是封装一个功能

# 自己写一个函数,完全与len相同.
'''
def 函数名():
    函数体
    
'''

# 函数的执行
# 函数名()  函数的执行者也叫函数的调用者

'''
返回值return
'''
# 1.函数中,遇到return终止函数
# 2.返回值,返回给了函数的调用者
#     return 单个值 返回单个值
#     return 多个值 返回一个由多个值组成的元组
#

# def my_len():
#     print(111)
#     print(222)
#     return (1, 2, 3), [12,4]
#     # print(333)
# ret = my_len()
# print(ret, type(ret))  # 返回 ((1, 2, 3), [12, 4]) <class 'tuple'>


# def my_len():
#     l1 = [1, 2, 34, 55, 66]
#     c = 0
#     for i in l1:
#         print(i)
#         c += 1
#     return c
#
# print(my_len())  # 返回 5


# def my_len():
#     print(111)
#     print(222)
#     return '太白', 666, '吴老板'
# print(my_len(), type(my_len()))  # 返回tuple


# def my_len():
#     print(111)
#     print(222)
#     return '太白'
# ret = my_len()
# print(ret, type(ret))   # 返回str


# def my_len():
#     print(111)
#     print(222)
#     return (1, 2, 3),[1,2,4]
# ret = my_len()
# print(ret, type(ret))


'''
函数的传参
'''
'''
实参角度: 函数的调用者
    1.位置参数: 从前至后 一一对应
    2.关键字传参: 不用按照顺序, 一一对应
    3.混合传参: 位置参数一定要在前面
'''


# 1.位置传参
# a = 'alex'
# b = 'wusir'
#
# def func1(a,b):
#     print(a+b)
# func1(b,a)


# 三元运算,简单的if else,对它的优化
# a = 3
# b = 2
# if a > b:
#     ret = a
# else:
#     ret = b
# ret = a if a > b else b
# print(ret)


# 返回较大的类型
# 方法1:
# def fun1(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# print(fun1(1, 2))

# 方法2:
# def func1(a, b):
#     return a if a > b else b
#
#
# print(func1(1,3))

# 方法3:
# def func1(a,b): return a if a > b else b
#
#
# print(func1(100,200))


# 2.关键字传参
# def func2(age,name):
#     print(name,age)
# func2(name='alex', age=73)

# 3.混合传参:
# 关键字参数一定要在位置参数的后面
# def func3(a,b,c,name):
#     print(a,b,c,name)
#
# func3(1,2,3,name='alex')


'''
形参角度
    # 位置传参: 按照顺序，一一对应
    # 默认传参: 如果不传，则默认使用默认参数，传参则覆盖。 常用的会设置默认参数
    # 动态参数，万能参数 *args **kwargs
'''

# 位置参数
# def func1(a,b,c,d):
#     print(a,b,c)
# func1(1,2,3)


# 默认参数
# 写函数,定义name age sex ,男生默认, 追加到文件里面
# def wfile(name, age, sex='男'):
#     with open('名单', encoding='utf-8', mode='a') as f1:
#         f1.write('{}----{}----{}\n'.format(name, age ,sex))
#
# while 1:
#     name = input('姓名,Q退出')
#     if name.upper() == 'Q':break
#     age = input('年龄')
#     if name.startswith('1'):
#         wfile(name, age)
#     else:
#         sex = input('性别')
#         wfile(name, age, sex)


'''
万能参数
'''
# 在函数的定义时, * **代表聚合

# *args  位置参数 元组
# **kwargs 关键字参数 字典里

'''
# *的魔性用法
'''
# def func1(*args, **kwargs):
#     print(args)
#
# l1 = [1,2,3]
# l2 = [11,22,33]
# l3 = (55,66,77)
# func1(*l1,*l2,*l3)
# 函数执行时 *iterable 打散
# 函数执行时 ** dict 打散


# 形参角度:所有参数的顺序
# 位置参数 ---> *args ---> 默认参数 ---> **kwargs
# def func5(a,b,*args,sex='男'):
# #     print(a)
# #     print(b)
# #     print(sex)
# #     print(args)
# #
# # func5(1,2,4,5,6,7,8,9)
# len
# def func5(a,b,*args,sex='男',**kwargs,):
#     print(a)
#     print(b)
#     print(sex)
#     print(args)
#
# func5(1,2,4,5,6,7,8,9,sex='女')
