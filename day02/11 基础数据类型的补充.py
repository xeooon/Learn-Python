# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn


# tuple 元组中如果只有一个元素且没有逗号,则他不是元组,而是对应的类型
# tu1 = (1,)
# print(tu1, type(tu1))
# tu2 = ('alex')
# print(tu2, type(tu2))

# tu3 = ([1, 2, 3])
# print(tu3, type(tu3))

# tu1 = (1,)
# print(tu1, type(tu1))


# dict 生成字典
# dic = dict.fromkeys('abc', 'alex')
# print(dic)


# ==  比较的是两边的数值是否相同
# is  比较的是内存地址是否相同
# id  查询的是内存地址(不是真实的内存地址,不像C语言)


# 在 正向 循环一个列表中,如果改变了列表的的大小, 那么结果肯能和你预想的不一样
# l1 = [11, 22, 33, 44, 55, 66]
# 将索引为奇数位置的元素删除。

# 方法1:通过切片加步长
# del l1[1::2]
# print(l1)

# 方法2: 倒叙删除
# print(len(l1))
# for i in range(len(l1)-1 ,-1, -1):
#     if i % 2 == 1:
#         del l1[i]
# print(l1)


'''
 将字典中的key键含有'k'元素的所有键值对删除。
'''

# dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'name': 'alex'}
# # 在循环一个字典时,不能改变该字典的大小
# l1 = []
# for key in dic:
#     if 'k' in key:
#         l1.append(key)
# for keys in l1:
#     del dic[keys]
# print(dic)

