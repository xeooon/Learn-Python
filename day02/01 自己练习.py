# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn

""""""

'''
基础数据类型
'''
# 数字init
# bit_length()  #  当十进制用二进制表示时,最少使用的位数
# v = 11
# data = v.bit_length()
# print(data)

# 布尔值bool
# 真 1 True
# 假 0 False

'''
字符串str
'''
# 索引即下标,就是字符串组成的元素,从第一个开始,初始索引为0以此类推.
# a = 'ABCDEFGHIJK'
# print(a[0])
# print(a[3])
# print(a[5])
# print(a[7])

# 切片就是通过索引 (索引:索引:步长)截取字符串的一段,形成新的字符串(原则就是顾头不顾尾)
# a = 'ABCDEFGHIJK'
# print(a[0:3])
# print(a[2:5])
# print(a[0:])  # 默认到最后
# print(a[0:-1])  # -1 是列表中最后一个元素的索引,但是要满足顾头不顾尾的原则,所以取不到K
# print(a[0:5:2])  # 加步长
# print(a[5:0:-2])  # 反向加步长

# 字符串常用方法
# capitalize,swapcase,title
# name = 'my Name is Zhangzhiqiang'
# print(name.capitalize())  # 首字母大写
# print(name.swapcase())  # 大小写翻转
# print(name.title())  # 每个单词首字母大写

# 内同居中,总长度,空白处填充
# ret2 = a1.center(20, "*")
# print(ret2)

# 数字符串中的元素出现的个数
# ret3 = a1.center("a", 0, 4)
# print(ret3)

# 默认将一个tab键变成8个空格，如果tab前面的字符长度不足8个，则补全8个，
# 如果tab键前面的字符长度超过8个不足16个则补全16个，以此类推每次补全8个。
# a2 = "hqw\t"
# ret4 = a2.expandtabs()
# print(ret4)

# startswith 判断是否以...开头
# endswith 判断是否以...结尾
# a4 = "dkfjkdfasf54"
# ret4 = a4.endswith('jdk', 3, 6)  # 顾头不顾尾
# print(ret4)  # 返回的是布尔值bool
# ret5 = a4.startswith("kfj", 1, 4)
# print(ret5)

# 寻找字符串中的元素是否存在
# a4 = "dkfjkdfasf54"
# ret6 = a4.find("fjdk", 1, 6)
# print(ret6)  # 返回的找到的元素的索引,如果找不到返回-1
# a4 = "dkfjkdfasf54"
# ret61 = a4.index("fjdk", 4, 6)
# print(ret61)  # 返回找到的元素的索引,找不到报错

# split 以什么分割,最终形成一个列表,此列表不含有这个分割的元素
# ret9 = 'title,Tilte,atre,'.split('t')
# print(ret9)
# ret91 = 'title,Tilte,atre,'.rsplit('t', 1)
# print(ret91)

# format的三种玩法 格式化输出
# res1 = '{} {} {}'.format('egon', 18, 'male')
# res2 = '{1} {0} {1}'.format('egon', 18, 'male')
# res3 = '{name} {age} {sex}'.format(sex='male', name='egon', age=18)

# strip
# name = '*egon**'
# print(name.strip('*'))
# print(name.lstrip('*'))
# print(name.rstrip('*'))

# replace
# name = 'xeon say : i have one bike, my name is xeon'
# print(name.replace('xeon', '666', 1))

# is 系列,返回True or False
# name = 'zhangzhiqiang123'
# print(name.isalnum())  # 字符串由字母或数字组成
# print(name.isalpha())  # 字符串只由字母组成
# print(name.isdigit())  # 字符串只由数字组成


'''
元组 tuple
'''
# 元组被称为只读列表，即数据可以被查询，但不能被修改，
# 所以，字符串的切片操作同样适用于元组。例：（1，2，3）（"a","b","c"）


'''
列表 list
列表相比于字符串，不仅可以储存不同的数据类型，而且可以储存大量数据，
32位python的限制是 536870912 个元素,64位python的限制是 1152921504606846975 个元素。
而且列表是有序的，有索引值，可切片，方便取值。

'''
# ######################### 增 #########################
# li = [1, 'a', 'b', 2, 3, 'a']
# li.insert(0, 55)  # 按照索引去增加
# print(li)

# li.append('aaa')  # 增加到最后
# li.append([1, 2, 3])  # 增加到最后
# print(li)

# li.extend(['q, a, w'])  # 迭代的去增
# li.extend(['q, a, w', 'aaa'])
# li.extend('a')
# li.extend('abc')
# li.extend('a, b, c')
# print(li)


# ######################### 删 #########################
# li = [1, 'a', 'b', 2, 3, 'a']
# l1 = li.pop(1)  # 按位置删除,有返回值
# print(l1)
#
# del li[1:3]  # 按位置去删除,也可以切片删除,没有返回值
# print(li)
#
# li.remove('a')  # 按元素去删除
# print(li)
#
# li.clear()  # 清空列表


# ######################### 改 #########################
# li = [1, 'a', 'b', 2, 3, 'a']
# print(li[1])
# li[1] = 'dfasdfas'  # 按下标更改
# print(li)

# li[1:3] = ['a', 'b']
# print(li)


# ######################### 查 #########################
# 切片去查, 或者循环去查


# ######################### 其他操作 #########################
# count数,方法统计摸个元素,在列表中出现的次数
# a = ["q", "w", "q", "r", "t", "y"]
# print(a.count("q"))

# index 方法用于从列表中,找出某个值,第一个匹配项的索引位置
# a = ["q", "w", "q", "r", "t", "y"]
# print(a.index("r"))

# sort 方法用于,在原位置对列表进行排序
# reverse 方法用于,将列表中的元素,反向存放
# a = [2, 1, 3, 4, 5]
# a.sort()  # 他没有返回值,所以只能打印a
# print(a)
#
# a.reverse()  # 他没有返回值,所以只能打印a
# print(a)


'''
字典 dict
字典是无序的对象集合,列表是有序的对象结合
字典中的元素是通过键值对来存取的,而不是通过偏移量存取.
'''

# ######################### 增 #########################
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# dic['li'] = ["a", "b", "c"]
# print(dic)

# setdefault 在字典添加键值对,如果只有键,那对应的值是none.
# 但是如果原子典中存在设置的键值对,则他不会改变或者覆盖
# dic.setdefault('k', 'v')
# print(dic)
# dic.setdefault('k', 'v1')
# print(dic)


# ######################### 删 #########################
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# dic_pop = dic.pop("a", '无key默认返回值')  # pop根据key删除键值对,并返回值,# 如果没有key则返货默认返回值.
# print(dic_pop)
#
# del dic["name"]  # 没有返回值
# print(dic)

# dic_pop1 = dic.popitem()  # 随机删除字典中的摸个键值对,将删除的键值对以元组的形式返回
# print(dic_pop1)

# dic_clear = dic.clear()  # 清空字典
# print(dic, dic_clear)  # {} None


# ######################### 改 #########################
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# dic2 = {"name": "xeon", "weight": 70}
# dic2.update(dic)  # 将dic素有的键值对覆盖添加(相同的覆盖,没有的添加)到dic2中
# print(dic2)


# ######################### 查 #########################
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# value1 = dic["name"]  # 没有value会报错
# print(value1)
#
# value2 = dic.get("djffdsafg", "默认返回值")  # 没有可以返回设定的返回值
# print(value2)


# ######################### 其他操作 #########################
# dict_items类型，可迭代的
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# item = dic.items()
# print(item, type(item))  # 查找出当前字典所有的key和value

# keys = dic.keys()
# print(keys, type(keys))  # 查找出当前字典所有的key

# value = dic.values()
# print(value, type(value))  # 查找出当前字典所有的value

# ######################### 字典的循环 #########################
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# for key in dic:
#     print(key)
# for item in dic.items():
#     print(item)
# for key, value in dic.items():
#     print(key, value)







'''
作业:用户登录
1. 三次重试机会
2. 每次输错误时显示剩余错误次数
'''

flag = 3
count = 1
while count < 4:
    username = input('请输入用户名:')
    password = input('请输入密码:')
    if username == 'xeon' and password == '123456':
        print(username, '登录成功.')
        count = 3
        break
    else:
        flag = flag - 1
        print(username, '登录失败.剩余登录次数为', flag)
    count += 1





