# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

"""
标题 : 24期周末班 - day06 - 习题和作业
作者 : 张志强
QQ号 : 1344683865
微信 : qingniaoxiaoqiang
邮箱 : Xeon@xeon.org.cn
"""


# ###################################### 习 题 #######################################
'''
1、new方法和init方法执行的执行顺序
'''
# 先执行__new__方法，在执行__init__方法
# class A:
#     def __new__(cls, *args, **kwargs):
#         print('先执行我__new__方法')
#         return object.__new__(cls)
#
#     def __init__(self):
#         self.name = 'xeon'
#         print('后执行我__init__方法')
#
# obj = A()
# print(obj.name)


'''
2、__call__方法在什么时候被调用
'''
# 对象加()触发__call__方法
# class Foo:
#     def __str__(self): pass
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print('调用了__call__')
#
# obj = Foo()  # 实例化obj对象
# obj('xeon')


'''
3、请用写一个类，用反射为这个类添加一个静态属性
'''
# class A:
#     def __init__(self): pass
#
# obj = A()
# setattr(obj, 'hobby', '大宝剑')  # 给obj这个对象增加hobby属性
# print('我的爱好是：%s' % obj.hobby)


'''
4、请用反射为上题的类的对象添加一个属性name, 值为你的名字
'''
# class A:
#
#     def __init__(self, name):
#         self.name = name
#
# obj = A('xeon')
# setattr(obj, 'age', 23)  # 给obj这个对象增加age属性
# setattr(obj, 'hobby', '大宝剑')  # 给obj这个对象增加hobby属性
# print('我叫%s，今年%s岁，爱好是%s' % (obj.name, obj.age, obj.hobby))


'''
5、请使用new方法实现一个单例模式
'''
# 单列模式：让一个类的实例化对象有且只有一个
# class A:
#     __instance = None  # 定义私有属性为None
#
#     def __new__(cls, *args, **kwargs):  # 先执行__new__方法，走if判断
#         if cls.__instance is None:  # 如果为None
#             obj = object.__new__(cls)  # 在原类创建一个
#             cls.__instance = obj  # 调用私有方法，重新赋值
#         return cls.__instance  # 返回私有属性
#
# i1 = A()  # 实例化对象i1
# i2 = A()  # 实例化对象i2
#
# print(i1, type(i1), i2, type(i2))


'''
6、生成一个6位随机验证码(包含数字和大小写字母)
'''
# import random
# def code():
#     char0 = ''
#     for i in range(5):
#         char1 = str(random.randint(0, 9))  # 需要转换为str取ascii的 0-9
#         char2 = chr(random.randint(33, 47))  # 取ascii的 !-/
#         char3 = chr(random.randint(65, 90))  # 取ascii的 A-Z
#         char4 = chr(random.randint(97, 122))  # 取ascii的 a-z
#         char5 = random.choice([char1, char2, char3, char4])  # 随机取char1,char2,char3,char4的一个值
#
#         char0 += char5
#     return char0
# print(code())


'''
7、发红包、制定金额和个数随机分配红包金额
'''
# import random
# def Red_packet(money, count):
#     miss = money * 100  # 避免浮点数
#     lis = []
#
#     for i in range(count - 1):  # 为什么要减1, 保证留一个
#         num = random.randrange(miss + 1)  # 在range的数字中取一个数
#         lis.append(num / 100)  # 把随机出来的数放到列表里
#         miss -= num
#     lis.append(miss / 100)  # 把剩下的数放到列表里
#
#     return lis
#
# print(Red_packet(1, 10))


# ###################################### 作 业 #######################################


'''
校园管理系统（02）
    需求：
        从“学生选课系统” 这几个字就可以看出来，我们最核心的功能其实只有选课。
        
    角色：
        学生、管理员、讲师
        
    功能：
        登陆 ： 管理员和学生都可以登陆，且登陆之后可以自动区分身份
        选课 ： 学生可以自由的为自己选择课程
        创建用户 ： 选课系统是面向本校学生的，因此所有的用户都应该由管理员完成
        查看选课情况 ：每个学生可以查看自己的选课情况，而管理员应该可以查看所有学生的信息
        
    工作流程：
        登陆 ：用户输入用户名和密码
        判断身份 ：在登陆成功的时候，可以直接判断出用户的身份是学生、讲师还是管理员
        
    学生用户 ：对于学生用户来说，登陆的工作几乎不变
        1、查看所有课程
        2、选择课程
        3、查看所选课程
        4、退出程序
        
    管理员用户：管理员用户也可以做更多的事情
        1、创建课程
        2、创建学生学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生的选课情况
        6、创建讲师
        7、为讲师指定班级
        8、创建班级
        9、为学生指定班级
        10、退出程序
    
    讲师用户 ：对于讲师用户来说，可以完成的功能如下
        1、查看所有课程
        2、查看所教班级
        3、查看班级中的学生
        4、退出程序
    
    踩分点:
        练习题：10
        继续对上一个作业进行相应的完善
'''
# import json
# import os
# # import hashlib
#
# def auth(file):  # 定义登录装饰器
#     def inner(*args, **kwargs):
#         for count in range(3):  # 循环3次
#             username = input('请输入帐号:').strip()
#             password = input('请输入密码:').strip()
#             with open('user_info', encoding='utf-8') as f1:
#                 for i in f1:
#                     i = i.strip().split('|')
#                     # 此处缺少密文登录
#                     if i[0] == username and i[1] == password:  # 判断用户名和密码
#                         f_dic = {'username': username, 'status': True, 'identity': None}  # 定义用户状态字典
#                         # 根据不同的角色修改f_dic的identity
#                         if i[2] == 'Student': f_dic['identity'] = i[2]
#                         elif i[2] == 'Teacher': f_dic['identity'] = i[2]
#                         else: f_dic['identity'] = i[2]
#                         f = open('login_status', 'w')  # 把用户的登录状态写入json文件
#                         json.dump(f_dic, f, ensure_ascii=False)  # 写成人可以认识的
#                         f.close()
#                         ret = file(*args, **kwargs)
#                         return ret
#                 else: print('\033[31;1m帐号或密码或身份有误,剩余尝试%s次.\033[0m' % (2 - count))
#     return inner
#
# @auth
# def login():  # 登录函数
#     f = open('login_status')
#     f_dic = json.load(f)
#     print('\033[32;1m\n用户 %s 以 %s 身份登录成功.\033[0m' % (f_dic['username'], f_dic['identity']))
#     f.close()
#
# class Func:
#     def __init__(self, name):  # 从login_status文件里面取用户
#         f = open('login_status')
#         f_init = json.load(f)
#         self.name = f_init['username']
#         f.close()
#
#     def show(self):  # 学生登录 方法
#         while 1:
#             tmp = {}
#             for k, v in enumerate(self.func_dic, 1):  # 打印学生类的菜单，从1开始枚举
#                 print('%s.%s' % (k, v))
#                 tmp[str(k)] = self.func_dic[v]  # 生成新的字典格式为：{序号: '类的动态方法'}
#
#             choice = input('\n请输入选择的编号:')  # 根据不同的选择, 执行不同的函数
#             if choice in tmp:  # 判断输入的范围
#                 getattr(self, tmp[choice])()  # 获取s对象，选择的属性，并执行
#             else:
#                 print('\033[31;1m无此编号\033[0m')
#
#
# class Student(Func):  # 定义学生类
#     func_dic = {'查看所有课程': 'check_all_courses', '选择课程': 'select_courses',
#                '查看所选课程': 'check_the_course', '退出程序': 'exit'}
#
#     def check_all_courses(self):  # 查看所有课程 方法
#         with open('course', encoding='utf-8') as f:  # 课程文件的格式：语文|数学|英语
#             tmp = {}
#             for k, v in enumerate(f.read().split("|"), 1):  # 通过枚举方式打印课程
#                 print('所有的课程为：%s.%s' % (k, v))  # 打印出课程
#                 tmp[str(k)] = v  # 把课程放到che_dic，待后选择课程方法续调用
#             return tmp  # 返回课程
#
#     def select_courses(self):  # 选择课程 方法
#         tmp = self.check_all_courses()  # 输入选择课程，调用查看所有课程方法
#         choice = input('请选择课程:')
#         if choice in tmp:  # 判断选的课在不在课程列表里
#             with open('user_course', encoding='utf-8') as f:  # 选课文件格式{'张三':['语文', '英语']}
#                 user_course = json.load(f)  # 是一个字典, key用户名, value是所选课的列表
#                 if user_course.get(self.name):  # 用户和课程里有没有那个用户
#                     user_course.get(self.name).append(tmp[choice])  # 有用户增加课程
#                 else:
#                     user_course.setdefault(self.name, [tmp[choice]])  # 无用户，增加用户及课程
#
#             with open('user_course', encoding='utf-8', mode='w') as f:  # 以人能看懂的格式写入文件
#                 json.dump(user_course, f, ensure_ascii=False)
#         else: print('\033[31;1m无此编号\033[0m')
#
#     def check_the_course(self):  # 查看所选课程 方法
#         with open("user_course", encoding="utf-8") as f:
#             user_course = json.load(f)  # 读取文件的数据结构
#             print('您选择的课程有: %s' % (user_course.get(self.name)))  # 返回value值
#
#     def exit(self): exit()  # 退出程序 方法
#
#
# class Admin(Student, Func):  # 定义管理员类, 继承Student部分 方法
#     func_dic = {'创建课程': 'create_course', '创建学生账号': 'create_student_teacher',
#                '查看所有课程': 'check_all_courses', '查看所有学生': 'check_all_student',
#                '查看所有学生的选课情况': 'check_all_student_course', '创建讲师': 'create_student_teacher',
#                '为讲师指定班级': 'set_teacher_class', '创建班级': 'create_class',
#                '为学生指定班级': 'set_student_class', '退出程序': 'exit'}
#
#     def create_course(self):  # 创建课程 方法
#         choice = input('请输入课程名称:')
#         with open('course', encoding='utf-8') as f1:
#             for i in f1:
#                 if choice in f1:
#                     print('您所创建的%s课程已存在,请勿重复添加.' % choice)
#                 else:
#                     with open('course', encoding='utf-8', mode='a') as f2:
#                         f2.write('{}|'.format(choice))
#                         break
#
#     def create_student_teacher(self):  # 创建讲师和学生账号 方法
#         username = input('请输入为创建的账号:').strip()
#         password = input('请输入为创建的密码:').strip()
#         identity = input('请输入为创建的身份,[Teacher, Student]：').strip()
#         with open('user_info', encoding='utf-8') as f1:
#             for i in f1:
#                 i = i.strip().split('|')
#                 if username in i[0]:  # 判断用户是否存在
#                     print('\033[31;1m%s账号已存在,请登录.\033[0m' % username)
#                     break
#             else:
#                 with open('user_info', encoding='utf-8', mode='a') as f2:
#                     if identity == 'Teacher' or identity == 'Student':  # 判断输入的身份
#                         # 加密功能待v3版本增加
#                         # pass_word = hashlib.md5()  # 创建md5对象
#                         # pass_word.update(password.encode(encoding='utf-8'))  # 此处必须声明encode
#                         # pass_word.hexdigest()
#
#                         f2.write('{}|{}|{}|\n'.format(username, password, identity))
#                         print('\033[33;1m %s 帐号创建成功.\033[0m' % username)
#                     else:
#                         print('没有此身份')
#
#     def check_all_student(self):  # 查询所有学生
#         with open('user_info', encoding='utf8') as f1:
#             tmp = {}
#             count = 1
#             for i in f1:
#                 i = i.strip().split('|')
#                 if i[2] == 'Student':
#                     tmp[str(count)] = i[0]
#                     count += 1
#             for key in tmp:
#                 print('所有的学生为：%s.%s' % (key, tmp[key]))
#             return tmp
#
#     def check_all_student_course(self):  # 查看所有学生的选课情况 方法
#         f = open('user_course')
#         f_dic = json.load(f)
#         for i in f_dic:
#             print('学生:%s，课程:%s' % (i, f_dic[i]))
#         f.close()
#
#     def check_all_teacher(self):  # 查询所有讲师
#         with open('user_info', encoding='utf8') as f1:
#             tmp = {}
#             count = 1
#             for i in f1:
#                 i = i.strip().split('|')
#                 if i[2] == 'Teacher':
#                     tmp[str(count)] = i[0]
#                     count += 1
#
#             for key in tmp:
#                 print('所有的讲师为：%s.%s' % (key, tmp[key]))
#             return tmp
#
#     def set_teacher_class(self):  # 为讲师指定班级 方法
#         tmp = self.check_all_teacher()  # 拿到了一个讲师字典 {'1': '讲师1', '2': '讲师2'}
#         for key in tmp:
#             print(key, tmp[key])
#         choice = input('请选择讲师:')  # 讲师的序号
#         c_dic = self.check_all_class()  # 拿到user_info
#         for i in c_dic:
#             print(i)
#         class_name = input('请输入讲师:')
#         self.gairen(tmp[choice], class_name)
#
#     def create_class(self):  # 创建班级 方法
#         cre_class = input('请输入创建的班级名称:')
#         with open('class', encoding='utf-8') as f1:
#             for i in f1:
#                 i = i.strip().split('|')
#                 if cre_class in i[0]:
#                     print(cre_class)
#                     print('您所创建的 %s 班级已存在,请勿重复添加.' % cre_class)
#                     break
#                 else:
#                     with open('class', encoding='utf-8', mode='a') as f2:
#                         f2.write('{}|'.format(cre_class))
#                         break
#
#     def set_student_class(self):   # 为学生指定班级 方法
#         tmp = self.check_all_student()  # 拿到了一个学生字典 {'1': '张三', '2': '二狗'}
#         for key in tmp:
#             print(key, tmp[key])
#         choice = input("请选择学生")  # 学生的序号
#         c_dic = self.check_all_class()  # 拿到user_info
#         for i in c_dic:
#             print(i)
#         class_name = input("请输入班级名")
#         self.gairen(tmp[choice], class_name)  # 修改用户文件
#
#     def check_all_class(self):  # 查询所有班级
#         with open('class', encoding='utf-8') as f1:
#             dic = f1.read().split('|')
#             return dic
#
#     def gairen(self, user_name, class_name):  # 修改用户文件
#         with open('user_info', encoding='utf-8') as fr, \
#                 open('user_info.bak', encoding='utf-8', mode='w') as fw:
#             for i in fr:
#                 if i.startswith(user_name):  # 如果是这个用户, 就修改这个用户的班级,
#                     i = i.split('|')  # 分割列表
#                     fw.write("%s|%s|%s|%s\n" % (i[0], i[1], i[2], class_name))  # 按位置依次写入
#                 else:
#                     fw.write(i)  # 如果不是这个用户就直接写到fw里
#         os.remove('user_info')
#         os.rename('user_info.bak', 'user_info')
#
#
# class Teacher(Student, Func):  # 定义老师类, 继承Student部分 方法
#     func_dic = {'查看所有课程': 'check_all_courses', '查看所教班级': 'check_class',
#                '查看班级中的学生': 'check_class_student', '退出程序': 'exit'}
#
#     def cat_class(self):
#         f = open('login_status')
#         f_init = json.load(f)
#         with open("user_info", encoding="utf-8") as f1:
#             cla = []
#             file = f1.readlines()
#             for i in file:
#                 i = i.strip().split('|')
#                 if f_init['identity'] in i and f_init['username'] in i:
#                     # cla.append(i[3])
#                     cla.append(i)
#         f.close()
#         return cla
#
#     def check_class(self):  # 查看所教班级 方法
#         tmp = self.cat_class()  # 接到一个字典['王五', '333', 'Teacher', '班级222']
#         print('您所教班级为: %s' % tmp[0][3])
#
#     def check_class_student(self):  # 查看班级中的学生
#         tmp = self.cat_class()
#         tmp2 = tmp[0][3]  #
#         with open('user_info', encoding='utf-8') as f1:
#             file = f1.readlines()
#             for i in file:
#                 i = i.strip().split('|')
#                 if 'Student' in i and tmp2 in i:  # 吧学生和班级打印 ['学生1', '111', 'Student', '班级222']
#                     print('班级中的学生: %s 所在班级为:%s' % (i[0], i[3]))
#
#
# s1 = Student(None)  # 实例化对象 学生
# a1 = Admin(None)  # 实例化对象 管理员
# t1 = Teacher(None)  # 实例化对象 老师
#
#
# def index():  # 执行整个程序函数
#     while 1:
#         print('\033[33;1m欢迎来到校园管理系统-v2\033[0m'.center(40, '-'))
#         print('学生账号：张三  账号密码：111\n管理账号：李四  账号密码：222\n老师账号：王五  账号密码：333\n')
#         l1 = {0: '请登录', 1: '退出'}
#         for k, v in l1.items(): print(k, v)
#         num = input('\n请输入访问的编号:').strip()
#         if num == '0':
#             login()
#             f = open('login_status')
#             f_dic = json.load(f)
#             if f_dic['identity'] == 'Admin':
#                 a1.show()
#
#             elif f_dic['identity'] == 'Student':
#                 s1.show()
#
#             elif f_dic['identity'] == 'Teacher':
#                 t1.show()
#
#             else: break
#             f.close()
#
#         elif num == '1': break
#         else:
#             print('\033[31;1m无此编号\033[0m')
# index()
