# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
什么是函数
'''
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
#
# 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，
# 比如print()，len()等。但你也可以自己创建函数，这被叫做用户自定义函数。





# 不用系统中的len函数,做出一个相似的来

# s1 = 'Hello world'
# length = 0
# for i in s1:
#     length += 1
# print(length)




'''
函数的定义与调用
'''

# def 是关键词,空格之后接函数名称和圆括号(), 最后还有一个冒号:


# def mylen():
#     # 计算s1的长度
#     s1 = 'Hello world'
#     length = 0
#     for i in s1:
#         length += 1
#     print(length)
# mylen()
#
# str_len = mylen()
#
# print('str_len: %s' %str_len)



# 只写return
# def ret_demo():
#     print(111)
#     return  # 一旦遇到retrun 结束整个函数
#     print(222)
# ret = ret_demo()
# print(ret)



# 返回一个值
# def mylen():
#     # 计算s1的长度
#     s1 = 'Hello world'
#     length = 0
#     for i in s1:
#         length += 1
#     return length
# str_len = mylen()
# print('str_len: %s' %str_len)


# # 返回多个值
# def ret_demo1():
#     # 返回多个值
#     retrun 1,2,3,4
#
# def ret_demo2():
#     # 返回多个任意类型的值
#     return 1, ['a', 'b'], 3, 4
#
# ret1 = ret_demo1()
# print(ret1)
# ret2 = ret_demo2()
# print(ret2)


# 传递多个参数
# def mymax(x,y):
#     the_max = x if x > y else y
#     return the_max
# ma = mymax(10,20)
# print(ma)


'''
位置参数
'''
# 位置参数必须在关键字参数的前面
# 对于一个形参只能赋值一次

# 站在实参角度,按位置传值
# def mymax(x,y):
#     # 此时x=10, y=20
#     the_max = x if x > y else y
#     return the_max
# ma = mymax(10, 20)
# print(ma)

# 站在实参角度,按关键字传值
# def mymax(x,y):
#     # 此时x=20,y=10
#     the_max = x if x > y else y
#     return the_max
# my = mymax(y=10,x=20)
# print(my)

# 站在实参角度,位置、关键字形式混着用
# def mymax(x,y):
#     # 此时,x=10, y=20
#     print(x,y)
#     the_max = x if x > y else y
#     return the_max
# my = mymax(10, y=20)
# print(my)


'''
默认参数
'''
# 将变化较小的值,设置成默认参数

# def stu_info(name, sex='male'):
#     # 打印学生信息函数, 由于班中大部分学生都是男生,
#     # 所以设置默认参数sex的值为'male'
#     print(name, sex)
# stu_info('alex')
# stu_info('eva','famale')

# 参数陷阱:默认参数是一个可变数据类型
# def defult_param(a ,l=[]):
#     l.append(a)
#     print(a)
# defult_param('alex')
# defult_param('egon')


'''
动态参数
'''
# 动态参数，也叫不定长传参，就是你需要传给函数的参数很多，不定个数，那这种情况下，
# 你就用*args，**kwargs接收，args是元祖形式，接收除去键值对以外的所有参数，
# kwargs接收的只是键值对的参数，并保存在字典中。


# def trans_para(*args, **kwargs):
#     print(args, type(args))
#     print(kwargs, type(kwargs))
# trans_para("jinxin",12,[1,2,3,4],[3,4,],(1,4,7),{"a":"123","c":456},country="china")

