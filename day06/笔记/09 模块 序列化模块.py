# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

import json
import pickle

'''
模块：就是python文件
1.内置模块： time os rando shelve re 等等
2.拓展模块: 大神写的 beautifulsoup iteat
3.自定义模块： 我们自己写的
'''

'''
序列化模块
将重要的数据，变成可以传输，并且得到后能够反解出来
'''

'''
json：适用于所有语言
'''
# dict list, tuple str int, float True False None
#     +------------------+------
#     | Python     | JSON    |
#     += == == == === == == == 
#     | dict       | object  |
#     +-----------------+------
#     | list,tuple | array   |
#     +-----------------+------
#     | str        | string  |
#     +-----------------+------
#     | int, float | number  |
#     +-----------------+------
#     | True       | true    |
#     +-----------------+------
#     | False      | false   |
#     +-----------------+------
#     | None       | null    |
#     +-----------------+------

# 序列化
# dic = {'name': '二狗', 'age': 25, 'sex': '男'}
# ret = str(dic).encode('utf-8')
#
# ret1 = ret.decode('utf-8')  # 编码
# print(ret1, type(ret1))  # 类型为str
# print(type(eval(ret1)))  # 类型为dict


'''
json 四个两对儿方法A
dumps序列化  loads反序列化  : 主要用于网络传输
'''
# dic = {'name': '二狗', 'age': 25, 'sex': '男'}
# ret = json.dumps(dic, ensure_ascii=False)  # 序列化过程：就是变成一个特殊的字符串,显示人能看懂的
# respon = json.loads(ret)  # 反序列化：将序列化的特殊字符串反解成原来的类型
# print(ret, type(ret))  # json的str类型用双引号
# print(dic, type(dic))  # python的str类型默认用单引号
# print(respon, type(respon))  # python的dict类型默认单引号

'''
json 四个两对儿方法B
dump写入文件  load读取文件   : 主要用于写入文件
'''
# dic = {1: {'username': '二狗1', 'password': 123456},
#        2: {'username': '二狗1', 'password': 123456},
#        3: {'username': '二狗1', 'password': 123456},
#        4: {'username': '二狗1', 'password': 123456}
#        }
#
# f = open('json_file', 'w')
# json.dump(dic, f)  #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
# f.close()
#
f = open('json_file')
dic2 = json.load(f)  # load方法接收一个文件句柄，直接将文件中的json字符串转成数据结构返回
print(dic2, type(dic2))
f.close()



'''
pickle: 只用于python语言之间的传输， 包含所有的python支持的数据类型
shelve只提供给我们一个open方法，是用key来访问的，使用起来和字典类似。
'''
# dic = {'name': '二狗', 'age': 25, 'sex': '男'}
# ret = pickle.dumps(dic)  # 序列化后看不懂
# respon = pickle.loads(ret)  # 反序列化可以看懂
# print(ret, type(ret))
# print(respon, type(respon))


# 写入文件 ,写的人看不懂
# class A:
#     name = 'alex'
#
#     def func(self): print(666)
# obj = A()
# # f = open('pickle_file', 'wb')  # 以byte类型写入
# # pickle.dump(obj, f)
# # f.close()
#
# f = open('pickle_file', 'rb')  # 以byte类型读取
# ret = pickle.load(f)
# print(ret.name)
# ret.func()
# f.close()


'''
shelve
'''
# import shelve
# f = shelve.open('shelve_file')
# f['key'] = {'int': 10, 'float': 9.5, 'string': 'Sample data'}  #直接对文件句柄操作，就可以存入数据
# f.close()

# import shelve
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)
