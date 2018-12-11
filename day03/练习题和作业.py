# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
"""
标题 : 24期周末班 - day03 - 习题和作业
作者 : 张志强
QQ号 : 1344683865
微信 : qingniaoxiaoqiang
邮箱 : Xeon@xeon.org.cn
"""

# ###################################### 练习题 #######################################


'''
1、文件a1.txt内容
序号  部门  人数 平均年龄 备注
1    python  30   26     单身狗
2    Linux   26   30     没对象
3    运营部  20   24     女生多
.......
通过代码，将其构建成这种数据类型：
[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
'''
# 取出文件第一行作为字典的key
# 取出文件后三行切割为value

# import copy
# with open('testlist', encoding='utf-8') as f1:
#     file = f1.readline().strip().split()  # 取出第一行作为字典的key ['序号', '部门', '人数', '平均年龄', '备注']
#     l1 = []
#     dic = {}
#     for key in f1:  # 取出后三行作为key ['1', 'python', '30', '26', '单身狗']
#         key = key.split()
#         for value in range(len(file)):  # 取出file的下标value, 赋值给后三行的key:value
#             dic[file[value]] = key[value]
#         l1.append(copy.deepcopy(dic))  # 利用深拷贝进行追加
# print(l1)


'''
2、 传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
'''
# def func2(*args, **kwargs):  # 形参: 位置参数,默认参数,万能参数
#     str = args
#     dic = {'字母': 0, '数字': 0, '空格': 0, '其他': 0}
#     for i in str:
#         if i.isdigit(): dic['数字'] += 1
#         elif i.isalpha(): dic['字母'] += 1
#         elif i == ' ': dic['空格'] += 1
#         else: dic['其他'] += 1
#     return dic
# print(func2(*'3a #11!~Fdc123'))  # 实参: 位置参数,关键字参数,混合参数


'''
3、 写函数，接收两个数字参数，返回比较大的那个数字。
'''
# def func3(a, b): return a if a > b else b
# print(func3(100, 200))


'''
4、 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容
返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
'''
# def func4(*args, **kwargs):
#     for k, v in kwargs.items():  # 将kwargs的值以key和value的方式取出来
#         if len(v) > 2:
#             kwargs[k] = v[:2]  # 如果value的长度大于2,那么就保留前2位
#     return kwargs
# print(func4(**{"k1": "v1v1", "k2": [11, 22, 33, 44]}))


'''
5、 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一
个字典，此字典的键值对为此列表的索引及对应的元素。
例如传入的列表为：[11,22,33] 返回的字典为{0:11,1:22,2:33}。
'''
# 方法1：
# def func5(a):
#     dic = {}
#     if type(a) is list:  # 如果a是列表时
#         for i in range(len(a)):  # 测量a的长度并取下标
#             dic[i] = a[i]  # dic[len的值] = a[的下标]
#         return dic
# print(func5([11, 22, 33]))

# 方法2：
# def func5(a):
#     dic = {}
#     for k,v in enumerate(a):
#         dic.setdefault(k,v)
#     return dic
# print(func5([11, 22, 33]))





'''
6、 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这
四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
'''
# def func6(name, sex, age, edu):
#     with open('student_msg', encoding='utf-8', mode='a') as f1:
#         f1.write('{} --- {} --- {} --- {}\n'.format(name, sex, age, edu))
#
# while 1:
#     msg = input('Enter录入 | Q退出:')
#     if msg.upper() == 'Q':break
#     name = input('姓名:').strip()
#     sex = input('性别:').strip()
#     age = input('年龄:').strip()
#     edu = input('学历:').strip()
#     func6(name, sex, age, edu)


'''
7、 升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
'''
# def func7(name, sex, age, edu):
#     with open('student_msg', encoding='utf-8', mode='a') as f1:
#         f1.write('{} --- {} --- {} --- {}\n'.format(name, sex, age, edu))
# while 1:
#     msg = input('性别Enter为男 | Enter录入 | Q退出:')
#     if msg.upper() == 'Q': break
#     name = input('姓名:').strip()
#     sex = input('性别:')
#     if sex == '':
#         sex = '男'
#     age = input('年龄:').strip()
#     edu = input('学历:').strip()
#     func7(name, sex, age, edu)


'''
8、 完成以下操作
'''
# 01 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
# import os
# def func8(*args, **kwargs):
#     # ('old', 'a', 'b')
#     old = args[0]
#     falt1 = args[1]
#     falt2 = args[2]
#     with open(old, encoding='utf-8') as f1, \
#         open('new', encoding='utf-8', mode='w') as f2:
#         for line in f1:
#             new_line = line.replace(falt1, falt2)
#             f2.write(new_line)
#     os.remove(old)
#     os.rename('new', old)
#
# fname = input('修改文件名[old]:').strip()
# falter = input('改啥:')
# falter2 = input('改成啥:')
# print(func8(fname, falter, falter2))

# 02.读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a = 10
# b = 20
# def test5(a, b): # 形参
#     print(a, b)  # 的值是: 20 10
# c = test5(b, a)  # 实参, 位置参数,从前至后 一一对应,所以b对应a是20, a对应b是10
# print(c)  # 的值是: None,因为def test5(a, b) 函数体没有返回值,所以返回None值


'''
9、 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
a = 10
b = 20
def test5(a, b):
    a = 3
    b = 5
print(a, b)
c = test5(b,a)
print(c)
'''
# print(a, b) 的值是: a为10 b为20
# print(c)    的值是: None
# 因为def test5(a, b) 函数体没有返回值,所以返回None值


'''
10、 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次
添加到函数的动态参数args里面.
例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
'''
# def func10(*args,**kwargs):
#     return args
# print(func10(*[1, 2, 3], *(22, 33)))


'''
11、 写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
例如 传入函数两个参数{'name': 'alex'} {'age': 1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
'''
# def func11(*args, **kwargs):
#     return kwargs
# print(func11(**{'name': 'alex'}, **{'age': 1000}))


'''
12、 下面代码成立么?如果不成立为什么报错?怎么解决?
'''
# 题目一：成立
# a = 2
# def wrapper():
#     print(a)
# wrapper()

# 题目二：不成立,已修改,见注释
# a = 2
# def wrapper():
#     global a  # 局部名称空间只能引用全局名称空间，修改需要增加global
#     a += 1
#     print(a)
# wrapper()

# 题目三：成立
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# wrapper()

# 题目四：不成立,已修改,见注释
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a  # 子名称空间，只能引用父级名称空间的变量，修改需要增加nonlocal
#         a += 1
#         print(a)
#     inner()
# wrapper()


'''
13、 写函数,接收两个数字参数,将较小的数字返回.
'''
# def func13(a, b): return a if a < b else b
# print(func13(100, 200))


'''
14、 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字
符串,并返回.
例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
'''
# def func14(*args, **kwargs):
#     l1 = []
#     for i in args:
#         if type(i) == int:
#             i = str(i)
#         l1.append(i)
#     return '_'.join(l1)
# print(func14(1, '老男孩', '武sir'))


'''
15、 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
'''
def func15(*args, **kwargs):
    dic = {'最大值': max(args), '最小值': min(args)}
    return dic
print(func15(2, 5, 7, 8, 4))


'''
16、 写函数，传入一个参数n，返回n的阶乘
例如:cal(7) 计算7*6*5*4*3*2*1
'''
# def func16(a):
#     count = 1
#     for i in range(a, 0, -1):
#         count *= i
#     return count
# print(func16(7))


'''
17、 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
例如：[(‘红心’，2),(‘梅花’，2), …(‘黑桃’，‘A’)]
'''
# def func17():
#     l1 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#     l2 = ['红心♥', '草花♣', '黑桃♠', '方块♦']
#     l3 = []
#     for i in l1:
#         for i2 in l2:
#             l3.append('(' + i2 + ')' + ',' + i)
#     print(l3)
# func17()


'''
18、 有如下函数:
def wrapper():
    def inner():
        print(666)
    wrapper()
你可以任意添加代码,用两种或以上的方法,执行inner函数.
'''
# 方法1:
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         print(666)
#     inner()
# wrapper()

# 方法2:
# def wrapper():
#     def inner():
#         print(666)
#     inner()
# wrapper()


# ###################################### 作业 #######################################


'''
作业：
用函数完成登录注册以及购物车的功能。
1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
5，退出则是退出整个程序。
'''
# def my_register(user, passwd):  # 注册函数
#      with open('user_pass', encoding='utf-8') as f1:  # 只读方式打开文件对比当前用户
#         file = f1.readlines()
#         for i in file:
#             i = i.strip().split(':')
#             if user in i[1]:  # 判断用户是否存在
#                 return ('用户%s已存在,请登录.' % user)
#         else:
#             with open('user_pass', encoding='utf-8', mode='a') as f2:
#                 f2.write('帐号:{}  密码:{}\n'.format(user, passwd))
#                 print('用户%s注册成功.' % user)
#
#
# def my_login(user, passwd):  # 登录函数
#     with open('user_pass', encoding='utf-8') as f1:  # 只读方式打开文件对比当前用户
#         file = f1.readlines()
#         for i in file:
#             i = i.strip().split(':')
#             if user in i[1] and passwd == i[3]:  # 对比user_pass文件
#                 print('用户%s请登录成功.' % user)
#                 my_shop()
#         else:
#             print ('用户%s登录失败,请重试.' % user)
#
#
# def my_shop():  # 购物车函数
#     product = {'1': {'name': '电脑', 'price': 200},
#                '2': {'name': '手机', 'price': 300},
#                '3': {'name': '楼房', 'price': 400}}
#     my = {'balance': 0, 'shop_list': {}}
#
#     while 1:  # 充值金额
#         money = input('请充值金额(整数):')
#         if money.isdigit():
#             my['balance'] = int(money)
#             break
#         else: print('充值失败,请重试.')
#
#     while 1:
#         print('商品列表'.center(26, '*'))
#         for i in product: print(i, product[i]['name'], product[i]['price'])
#
#         inp = input('请输入购买的商品编号, N结算并退出购买, Q退出:').strip()
#         if inp in product:  # 计算我买的商品数量
#             count = my['shop_list'].setdefault(inp, 0)
#             my['shop_list'][inp] = count + 1   # {'商品编号': 商品数量}
#             print('已选择1件 %s 商品' % product[inp]['name'])
#         elif inp.upper() == 'Q': quit()
#         elif inp.upper() == 'N':  # 结算并退出购买
#             num = 0
#             for i2 in my['shop_list']: num += product[i2]['price'] * my['shop_list'][i2]
#             if num > my['balance']:  # 余额不够
#                 for i3 in my['shop_list']:
#                     print(i3, product[i3]['name'], product[i3]['price'], my['shop_list'][i3])  ## 商品名称 价格 数量
#                 err = input('结算商品失败,请删除部分商品:')
#                 if err in my['shop_list']: my['shop_list'].pop(err)
#             else:  # 余额够
#                 print('已购商品'.center(26, '*'))
#                 for i4 in my['shop_list']:
#                     print(i4, product[i4]['name'], product[i4]['price'], my['shop_list'][i4])
#                 my['balance'] -= num  # 我的余额 - 商品价格*数量
#                 print('本次消费金额:%d元, 剩余余额:%d元' % (num, int(my['balance'])))
#                 break
#         else: print('没有此商品,请重新输入.')
#
#
# while 1:  # 总函数
#     inp = input('欢迎来到我的商城,登录成功后才能购买东西哦,请选择把.\nA注册, B登录, C退出:')
#     if inp.upper() == 'A':  # 注册
#         user = input('请输入注册的账号:').strip()
#         passwd = input('请输入注册的密码:').strip()
#         my_register(user,passwd)  # 执行注册函数
#         my_shop()  # 执行购物车函数
#
#     elif inp.upper() == 'B':  # 登录
#         count = 1
#         while count < 4:
#             user = input('请输入登录的账号:').strip()
#             passwd = input('请输入登录的密码:').strip()
#             my_login(user, passwd)  # 执行登录函数
#             count += 1
#             if count == 4:
#                 quit()
#         my_shop()  # 执行购物车函数
#
#     elif inp.upper() == 'C': break
#     else: print('输入有误,请重试.')
