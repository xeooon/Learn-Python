# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# hashlib 模块

# hash
# 对不可变对数据(int str bool tuple)进行哈希算法
# 将strtuple转化成等长度等一串数字

# 加密模块，摘要算法。
# 它里面包含的加密算法非常多：MD5 sha。

# 算法加密
# 1,加密类型必须是str。
# 2,无论这个str多长，加密之后都是转化成等长度的数字。
# 3,无论在任何机器上，对相同的字符串进行加密 密文一致。
# 4,不同的字符串加密之后的密文一定不同。


# 用途：
# 1，对密码进行加密。
# 2. 对文件进行校验


'''
普通加密
'''
# import hashlib
#
# def encryption(password):
#     ret = hashlib.md5()
#     ret.update(password.encode('utf-8'))
#     return ret.hexdigest()
#
#
# def register():
#     username = input('>>>').strip()
#     password = input('>>>').strip()
#     password = encryption(password)
#     with open('register', encoding='utf-8', mode='a') as f1:
#         f1.write('{}|{}'.format(username, password))
#
# register()


'''
加固定盐加密
'''
# import hashlib
#
# ret = hashlib.md5('xeon 666'.encode('utf-8'))
# ret.update('alex3714'.encode('utf-8'))
# print(ret.hexdigest())


'''
动态加盐
'''
# import hashlib
#
# username = 'alex'
# password = 'alex3714'
#
# ret = hashlib.md5(username[::2].encode('utf-8'))
# ret.update('alex3714'.encode('utf-8'))
# print(ret.hexdigest())


'''
sha加密,方法与上面一致
'''
# import hashlib
# ret = hashlib.sha1()
# ret.update('alex'.encode('utf-8'))
# print(ret.hexdigest())


# import hashlib
# ret = hashlib.sha512()
# ret.update('alex'.encode('utf-8'))
# print(ret.hexdigest())



'''
文件的校验
'''
# 全部读取文件，占用内存太大。
# import hashlib
# def file_hashlib(file):
#     ret = hashlib.md5()
#     with open(file, mode='rb') as f1:
#         ret.update(f1.read())
#     return ret.hexdigest()
#
# print(file_hashlib('文件校验1'))
# print(file_hashlib('文件校验2'))



# import hashlib
#
# s1 = '我草了,读取文件校验'
# ret = hashlib.md5()
# ret.update('我草了'.encode('utf-8'))
# ret.update(',读取文件校验'.encode('utf-8'))
# print(ret.hexdigest())


'''
循环文件句柄校验，占用内存少
'''
# import  hashlib
#
# def file_hashlib2(file):
#     ret = hashlib.md5()
#     with open(file, mode='rb') as f1:
#         for i in f1:
#             ret.update(i)
#     return ret.hexdigest()
#
# print(file_hashlib2('文件校验1'))
# print(file_hashlib2('文件校验2'))
#

