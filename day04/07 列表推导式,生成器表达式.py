# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
列表推导式: 不要超过三层.
优点:构造简单,一行完成
缺点:1, 不能排错 2. 他不能构建复杂的数据结构

'''

# 创建列表从1,100
# l1 = []
# for i in range(1, 101):
#     l1.append(i)
# print(l1)


# 凡是用列表推导式能构建的数据,python的代码都能构建,列表推导式不能构建的数据,python代码亦可以构建

# 循环模式: [变量（加工后的变量） for 变量 in iterable]
# 构建一个列表,['python1期','python2期' ... 'python24期']
# print(['python%s期'% i for i in range(1, 25)])


# 筛选模式: [变量（加工后的变量） for 变量 in iterable if 条件]
# 构建一个列表,30以内能被2整除的数
# print([i for i in range(31) if i %2 ==0])

# 10以内所有数的平方, 1, 4, 9, 16, 100
# print([i ** 2 for i in range(1,11)])

# 30以内所有数能被3整除的平方 39, 36, 81 ... 900
# print([i ** 2 for i in range(1, 31) if i % 3 == 0])

# 过滤长度小于3的字符串列表,并将剩下的转换为都大写
# l1 = ['alex', 'taibai', 'wusir', 're', 'ab']
# print([i.upper() for i in l1 if len(i) > 3])



'''
# 生成器表达式
用()括起来,其他规则与列表推导式一样
'''
g1 = (i * i for i in range(100000))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))




