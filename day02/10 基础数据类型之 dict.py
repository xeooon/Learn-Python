# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 字典是键值对出现, key:value  , 字典的key是唯一不重复的, 可以存储大量的关系型数据
# 字典在3.5版本,包括3.5之前是无序的, 3.6之后有序,无索引,无下标
# 字典的key:str,int,bool值(不常用),tuple(不常用) 不可变的数据类型
# 列表是可变的数据类型叫可哈希的


# 字典的value:任意数据类型

# dic = {'name_list': ['张三', '李四'],
#        'alex': {'sex': '男', '爱好': '非男'}}


'''
增
'''
# 1.按照键值对去增 有则改之,无则加之
# dic = {'name': 'TaiBai', 'age': '25', 'sex': '男'}
# dic['job'] = 'Teacher'
# print(dic)
# dic['name'] = 'alex'
# print(dic)

# 2.setdefault 无则增加, 有则不变
# dic.setdefault('job', 'Teacher')
# print(dic)
# dic.setdefault('name', 'alex')
# print(dic)


'''
删
'''
# dic = {'name': 'TaiBai', 'age': '25', 'sex': '男'}
# 1.通过pop()去删
# ret = (dic.pop('name'))
# print(ret)  # 返回删除的值
# print(dic)

# 2.清空字典
# dic.clear()
# print(dic)

# 3.通过del()去删
# del dic['name']
# print(dic)


'''
改
'''
# dic = {'name': 'TaiBai', 'age': '25', 'sex': '男'}
# dict

# 1.通过key去改
# dic['name'] = 'alex'
# print(dic)

# 2.通过update去改
# dic2 = {'name': 'alex', 'weight': '75'}
# dic2.update(dic)  # 将dic的所有键值对,覆盖添加到dic2中,dic不变
# print(dic2)


'''
查
'''
# dic = {'name': 'TaiBai', 'age': '25', 'sex': '男'}
# 1.用key去查value
# print(dic['name'])  # 没有会报错

# 2.用get
# print(dic.get('name'))
# print(dic.get('name1', '没有此key'))  # 找不到默认返回none,可以自定义返回值


'''
其他操作
'''
# dict_items类型，可迭代的
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# item = dic.items()
# print(item, type(item))  # 查找出当前字典所有的key和value

# keys = dic.keys()
# print(keys, type(keys))  # 查找出当前字典所有的key

# value = dic.values()
# print(value, type(value))  # 查找出当前字典所有的value


'''
字典的循环
'''
# dic = {"name": "jin", "age": 18, "sex": "male", "li": "123"}
# for key in dic:
#     print(key)  # 查找出所有的key
# for item in dic.items():  # 查找出key 和value 并以元组的方式
#     print(item, type(item))

# a, b, c = 1, 2, 3
# a, b, c = [1, 2, 3]
# print(a, b, c)
# a = 10
# b = 100
# a, b = b, a
# print(a,b)

# for key, value in dic.items():
#     print(key, value)  # 把key和value以字符串的方式拿出来

# print(list(dic.keys()))  # 把字典的key转换为列表
# print(list(dic.values()))  # 返回字典的value转换为列表
# print(list(dic.items()))


'''
字典的嵌套
'''
# dic = {'name': 'alex','name_list': ['wusir','taibai'],1: {'name': '日天'}}
# 1.将wusir全部变成大写
# print(dic['name_list'][0])
# dic['name_list'][0] = dic['name_list'][0].upper()
# print(dic)

# 2.将日天 改成 泰迪。
# dic[1]['name'] = '泰迪'
# print(dic)

