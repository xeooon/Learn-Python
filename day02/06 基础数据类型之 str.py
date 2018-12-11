# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# str 对字符串操作形成的都是新的字符串

'''
索引以及切片
'''

# 下标,索引
# s = 'python24期'
# s1 = s[0]
# print(s1, type(s1))
# s2 = s[2]
# print(s2)
# s3 = s[-1]
# print(s3)

# 切片 顾头不顾尾
# s[起始索引: 结尾索引顺延1位: 步长]
# s = 'python24期'
# print(s[0:3])  # 返回 pyt
# print(s[:6])   # 返回 python
# print(s[:])    # 返回 python24期

# print(s[:6:2])  # 返回 pto
# print(s[-1:-4:-1])  # 返回 期42
# print(s[-1:-6:-2])  # 返回 期2o


'''
# capitalize 首字母大写,其他字母小写 *
'''
# s = 'oldBoy'
# s1 = s.capitalize()
# print(s1)


'''
swapcase 大小写翻转 *
'''
# s = 'oldBoy'
# s2 = s.swapcase()
# print(s2)


'''
center 居中 设置宽度 *
'''
# s = 'oldBoy'
# s3 = s.center(20, '*')
# print(s3)


'''
title() 非字母隔开的'单词' , 首字母大写 *
'''
# ss = 'alex wusir2taibai*ritian'
# s4 = ss.title()
# print(s4)


'''
upper() 全大写   ***
'''
# s = 'oldBoy'
# s5 = s.upper()
# print(s5)


'''
lower() 全小写   ***
'''
# s = 'oldBoy'
# s6 = s.lower()
# print(s6)


'''
模拟验证码登录, 不区分大小写
'''
# username = input('请输入账号:')
# password = input('请输入密码:')
# code = 'QerAg'.upper()
# your_code = input('请输入验证码:').upper()
#
# if username == 'alex' and password == 'SB':
#    if your_code == code:
#        print('登录成功.')


'''
startswith() 判断以什么开头  **
'''
# s = 'oldBoy'
# s6 = s.startswith('o')
# print(s6)
# s61 = s.startswith('old')
# print(s61)
# s62 = s.startswith('B', 3)
# print(s62)


'''
endswith() 判断以什么结尾    **
'''
# s = 'oldBoy'
# s7 = s.endswith('Boy')
# print(s7)


'''
strip() 默认去除字符串前后两端的,空格符,换行符,制表符  ***
lstrip() 只去除左边
rstrip() 只去除右边
'''
# s = '    \noldBoy\t'
# s7 = s.strip()
# print(s7)

# username = input('请输入账号:').strip()
# password = input('请输入密码:').strip()
# if username == 'alex' and password == 'SB':
#     print('登录成功.')

# s = '中aboldboycd'
# print(s.strip('中dcba'))


'''
str ---> list   ***
split   分割,默认按照空格分割
rsplit  右分割,默认按空格分割
'''
# s = 'alex wusir barry'
# s8 = s.split()  # 默认按照空格分割
# print(s8)  # 返回 ['alex', 'wusir', 'barry']

# s = 'alex,wusir,barry'
# s9 = s.split(',')
# print(s9)  # 返回 ['alex', 'wusir', 'barry']

# ss1 = ',alex,wusir,barry'
# s10 = ss1.split(',')
# print(s10)

# print(ss1.split(',', 1))
# print(ss1.rsplit(',', 1))

# s = 'alex,wusir,barry'
# s11 = s.rsplit(',', 1)
# print(s11)

'''
join  ***
'''
# 一个用途list --> str
# l1 = ['alex', 'wusir', 'barry']  # 列表元素必须全部为字符串
# s10 = ' '.join(l1)
# print(s10)

# 连接符
# s = 'oldboy'
# s10 = '_'.join(s)
# print(s10)


'''
replace 替换 ***
'''
# s = '老男孩 老男孩 alex linux 大数据 alex'
# s11 = s.replace('alex', '太白')
# print(s11)
# s12 = s.replace('alex', '太白', 1)
# print(s12)


'''
is 系列
'''
# name = 'jinxin123'
# print(name.isalnum())  # 字符串由字母或数字组成
# print(name.isalpha())  # 字符串只由字母组成
# print(name.isdigit())  # 字符串只由数字组成 str ---> int 可以作为一个判断条件

'''
format 格式化输出
'''
# res = '{} {} {}'.format('egon',18,'male')
# print(res)

# res = '{1} {0} {1}'.format('egon',18,'male')
# print(res)

# res = '{name} {age} {sex}'.format(sex='male',name='egon',age=18)
# print(res)

'''
find index
'''
# find  通过元素找索引,找不到,返回-1
# index 通过元素找索引,找不到,报错
# s = 'oldboy'
# print(s.find('d'))  # 返回 d
# print(s.find('A'))  # 找不到返回 -1
# s2 = 'xeoAoBon'
# print(s2.find('o', 3, 6))  # 可以切片

# print(s.index('d'))  # 返回 2
# print(s.index('A'))  # 找不到返回报错substring not found


'''
公共方法: 字符串 列表 都可以用  ***

'''
# 1.通过len 测量个数
# s = 'asdfasdfasdfasdfasdfasf'
# print(len(s))

# 2.通过count 统计某个元素出现的次数
# s = 'asdfasdfasdfasdfasdfasf'
# print(s.count('f'))
