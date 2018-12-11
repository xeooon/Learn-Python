# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


# 可迭代对象:
# 内部含有'__iter__'方法的数据就是可迭代对象
# 可迭代对象: list str tuple set dict range() 文件句柄

# 可迭代协议





# 迭代器与可迭代对象的关系

# 迭代器能看见内存地址
# 迭代器 next  对应一个值


# 迭代器的好处
# 1.非常非常节省内存, 只占用一个数据的内存地址
# 2.它满足惰性机制,取一个来一个,不取不来
# 3. 一条道走到黑


# 利用while 循环模拟for循环 的机制

# 1.将可迭代对象抓换成迭代器
# 2. 利用net进行取值
# 3. 利用异常处理,终止循环


# l1 = [1, 2, 3, 'alex']
# iter1 = l1.__iter__()
# while 1:
#     try:
#         print(iter1.__next__())
#     except StopIteration:
#         break


# 生成器, 自己用python代码写的迭代器,本质就是
# 1.函数式写法 只要函数中出现yield,那么它就不是函数了,他是生成器函数
# 2.生成器表达式


# 一个next对应一个yield,这个yield相当于指针,


# yield 与return的区别
# return 结束函数 给函数返回值
# yield 不会结束生成器函数, next对应一个yield进行取值





# 场景: 做衣服
# def cloth():
#     for i in range(1, 11):
#         print('老男孩老年T-shirt %s号' % i)
# cloth()



# def cloth():
#     for i in range(1, 11):
#         yield '老男孩老年T-shirt %s号' % i
# g = cloth()
#
# for i in range(5):
#     print('前部分', g.__next__())
#
#
# for i in range(5):
#     print('后部分', next(g))




# 生成器表达式















