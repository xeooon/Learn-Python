# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


'''
迭代器
'''
# 可迭代对象：内部含有‘__iter__’方法的数据就是可迭代对象
# 可迭代对象：list str tuple set dict range() 文件句柄

# 通过dir()查看当前对象支持的方法
# s1 = '二狗的周末生活'
# print(dir(s1))
# print('__iter__' in dir(s1))

# 迭代器
# 内部还有'__iter__'方法的并且含有'__next__'方法的就是迭代器
# f1 = open('register', encoding='utf-8')
# print('__iter__' in dir(f1))
# print('__next__' in dir(f1))
# f1.close()

# 可迭代对象 ---> 迭代器
# 迭代器： next ---> 一个值

# l1 = [1, 2, 3, 'alex']
# iter1 = iter(l1)  # 等同于 l1.__iter__()
# print(iter1)
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())  # 当没有结果会报错StopIteration

# 迭代器：
# 1，非常非常节省内存。
# 2，他满足惰性机制。
# 3， 一条路走到黑。



'''
生成器
'''
# 利用while循环模拟for循环 的机制。
# 1， 将可迭代对象转化成迭代器
# 2， 利用next 进行取值
# 3， 利用异常处理终止循环。

# l1 = [1, 2, 3, 'alex']
# iter1 = l1.__iter__()
# while 1:
#     try:
#         print(next(iter1))
#     except StopIteration:
#         break


# 生成器：自己用python代码写的迭代器 本质就是迭代器
# 1，函数式写法
# 2，生成器表达式



# 函数式写法 构建生成器
# 只要函数中出现yield,那么 他就不是函数了，他是生成器函数。

# def func1():
#     yield 3
#     yield 4
#     yield 5
#     yield 6
# g = func1()
# print(g)
# print(next(g))  # 等同于 print(g.__netxt__())
# # 一个next要对应一个yield
# print(next(g))
# print(next(g))
# print(next(g))


# yield 与return的区别
# return 结束函数, 给函数返回值
# yield 不会结束, 生成器函数, next对应一个yield取值

# def cloth():
#     for i in range(1,21):
#         yield '老男孩老年T-Shirt %s号' % i
# num = cloth()
#
# for i in range(5):
#     print('前5件',next(num))
# for i in range(15):
#     print('后15件',num.__next__())