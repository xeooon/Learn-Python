# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# what: list与其他语言的数组相似,基础数据类型, 可以存储各种数据类型,可以含有大量的数据.容器类的数据类型
# 32位python的限制是 536870912 个元素,64位python的限制是 1152921504606846975 个元素
# li = ['alex', 123, Ture, (1, 2, 3, 'wusir'), [1, 2, 3, '小明', ], {'name': 'alex'}]
#
# s1 = '123'




# how:
#    1.索引切片
#    2.增删改查,以及其他操作
#    3.列表的嵌套

'''
索引切片
'''
# 和字符串的索引切片一模一样
# l1 = ['alex', 'wusir', '太白', 100, '女神']
# print(l1[0])
# print(l1[-2])
#
# print(l1[0:2], type(l1[0:2]))

'''
增3种
append  追加
insert  插入
extend  迭代的追加
'''
l1 = ['alex', 'wusir', '太白', 100, '女神']
# 1.append  追加
# l1.append('文刚')
# print(l1)

# 2.insert  插入
l1.insert(1, 'oldboy')
print(l1)

# 3.extend  迭代的追加
# l1.extend('abc')
# print(l1)
# l1.extend(['abc', 'erf'])
# print(l1)


'''
删4种
pop 按照索引删除,有返回值
remove 按照元素删除
clear 清空列表
del 切片删除

'''

# l1 = ['alex', 'wusir', '太白', 100, '女神']

# 1.pop 按照索引删除
# ret = l1.pop(1)
# print(ret)
# print(l1)

# 2.remove 按照元素删除
# l1.remove('alex')
# print(l1)

# 3.clear 清空列表
# l1.clear()
# print(l1)

# 4.del 切片删除,公共的方法
# 4.1.按照索引删除
# del l1[1]
# print(l1)

# 4.2.按照切片删除(步长)
# del l1[:2]
# print(l1)
# del l1[::2]
# print(l1)


'''
改3种
按照索引
按照切片
按照切片步长
'''
# l1 = ['alex', 'wusir', '太白', 100, '女神']

# 1.按照索引
# 变量[下标] = '替换内容'
# l1[1] = 'SB'
# print(l1)


# 2.按照切片
# l1[:2] = 'asdfsadflkdklk'
# print(l1)

# 3.按照切片加步长
# l1[::2] = 'abc'  # 加步长,一定要一一对应
# print(l1)
# l1[::2] = [1, 2, 3]
# print(l1)


'''
查4种
按照索引去查
按照切片去查
按照切片加步长去查
'''
# l1 = ['alex', 'wusir', '太白', 100, '女神']

# 1.按照索引去查
# s = l1[0]
# print(s)

# 2.按照切片去查
# s2 = l1[:2]
# print(s2)

# 3.按照切片加步长去查
# s3 = l1[::2]
# print(s3)

# 4.按照for循环去查
# for i in l1:
#     print(i)


'''
其他方法
'''
# l1 = ['alex', 'wusir', '太白', 100, '女神', 'wusir']  # 通过元素查索引

# 1.通过元素找索引
# print(l1.index('太白'))

# 2.统计元素len
# print(len(l1))

# 3.count 统计次数
# c = l1.count('wusir')
# print(c)

# 4.sort 排序
# l1 = [2, 3, 5, 1, 9, 8, 7, 6]

# l1.sort()  # 默认从小到大排列
# print(l1)

# l1.sort(reverse=True)  # 从大到小排列
# print(l1)

# l1.reverse()  # 翻转排列
# print(l1)

'''
列表嵌套
'''

# l1 = ['alex', 'wusir', [1, 'taibai']]

# wusir全部大写
# 方法1:
# l1[1] = l1[1].upper()
# print(l1)

# 方法2:
# l1[1] = 'WUSIR'
# print(l1)

# taibai首字母大写
# 方法1:
# l1[2][1] = l1[2][1].capitalize()
# print(l1[2][1])

# 方法2:
# l1[2][1] = 'Taibai'
# print(l1)


# why:
# 列表可以储存大量的数据, 列表可以保持原来的数据类型


'''
range 可以看做自定义的数字范围的列表,一般以for循环结合
'''
# print(range(1, 100))

# for i in range(1, 100):
#     print(i)  # 顾头不顾尾

# for i in range(1, 20, 2):
#     print(i)  # 指定步长

# for i in range(20, 1, -1):
#     print(i)  # 反向取,顾头不顾尾


# l1 = ['alex', 'wusir', [1, 'taibai']]
#
# # for 循环将列表索引打印出来
# for i in l1:
#     print(l1.index(i))

# 利用for range 打印出列表的索引
# l1 = ['alex', 'wusir', 'wusir', '太白', 100, '女神', 'wusir']
# for i in range(len(l1)):
#     print(i)


list