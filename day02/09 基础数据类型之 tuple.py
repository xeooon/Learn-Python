# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn

tuple
tu = (1, True, [12, 3], 'asdf')
# 元组是只读列表,尽量不要嵌套
# 可以索引,可以切片(步长)
# 不能增删改(儿子不能,孙子可以),只能查询

# index 通过元素查索引
# tu1 = tu[::]
# print(tu1)

# 1.count 统计个数
print(tu.count())

# 2.len 统计个数

# 3.for循环


'''
# 元组被称为只读列表，即数据可以被查询，但不能被修改，如果元组内包含列表,则列表内容可以修改.
# 所以，字符串的切片操作同样适用于元组。例：（1，2，3）（"a","b","c"）
'''

# tu = (1, 2, True, [2, 3, 4], 'alex')
# 1.for 循环查找
# for i in tu:
#     print(i)

# 2.通过索引找元素,索引,切片,
# tu = (1, 2, True, [2, 3, 4], 'alex')
# print(tu[1])  # 返回2
# print(tu[0:3:2])  # 指定步长为2, 返回(1, True)

# 3.index方法:通过元素找索引
# tu = (1, 2, True, [2, 3, 4], 'alex')
# print(tu.index(True))  # 找到True的索引, 返回0, 因为True为真则为0,则找第一个索引位置的元素为1

# 4.count方法:统计元素出现的次数
# tu = (1, 2, True, [2, 3, 4], 'alex')
# print(tu.count(2))  # 指定查找元素为2, 总共出现了1次

# 5.len方法:测试当前列表有多少个元素
# print(len(tu))  # tu列表里面一共有5个元素

# 6.如果元组内包含列表,则列表内容可以修改.
# tu = (1, 2, True, [2, 3, 4], 'alex')
# tu[3].append(666)  # 在tu的元组里,索引第四位置,增加666
# print(tu)  # 返回(1, 2, True, [2, 3, 4, 666], 'alex')



