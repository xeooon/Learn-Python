# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
"""
标题 : 24期周末班 - day05 - 作业
作者 : 张志强
QQ号 : 1344683865
微信 : qingniaoxiaoqiang
邮箱 : Xeon@xeon.org.cn
"""

# ###################################### 作 业 #######################################

'''
作业题目：校园管理系统（01）

作业需求:
    从“学生选课系统” 这几个字就可以看出来，我们最核心的功能其实只有 选课。
    
    角色：
        学生、管理员
        
    功能：
        登陆：管理员和学生都可以登陆，且登陆之后可以自动区分身份
        选课：学生可以自由的为自己选择课程
        创建用户：选课系统是面向本校学生的，因此所有的用户都应该由管理员完成
        查看选课情况：每个学生可以查看自己的选课情况，而管理员应该可以查看所有学生的信息
        
    工作流程：
        登陆 ：用户输入用户名和密码
        判断身份 ：在登陆成功的时候应该可以直接判断出用户的身份 是学生还是管理员

        学生用户：对于学生用户来说，登陆之后有三个功能
            1、查看所有课程
            2、选择课程
            3、查看所选课程
            4、退出程序
            
        管理员用户：管理员用户除了可以做一些查看功能之外，还有很多创建工作
            1、创建课程
            2、创建学生学生账号
            3、查看所有课程
            4、查看所有学生
            5、查看所有学生的选课情况
            6、退出程序

踩分点:
    类的创建和规划 20分
    登陆自动识别身份 10分
    管理员创建各种信息 20分
    学生选课 20分
    将内存中的数据保存到文件中 10分
    代码简洁、调理清晰10分
'''
login_status = {'username': None, 'status': False, 'identity': None}

def auth(f):  # 装饰器
    def inner(*args, **kwargs):
        for count in range(3):  # 循环3次
            username = input('请输入帐号:').strip()
            password = input('请输入密码:').strip()
            with open('register', encoding='utf-8') as f1:
                for i in f1:
                    i = i.strip().split('|')
                    if i[0] == username and i[1] == password:  # 判断用户名和密码
                        login_status['username'] = username
                        login_status['status'] = True
                        if i[2] == 'Student': login_status['identity'] = i[2] # 判断用户角色
                        else: login_status['identity'] = i[2]
                        ret = f(*args, **kwargs)
                        return ret
                else: print('\033[31;1m帐号或密码或身份有误,剩余尝试%s次.\033[0m' % (2 - count))
    return inner

@auth
def login():  # 登录函数
    print('\033[33;1m\n用户 %s 以 %s 身份登录成功.\033[0m' % (login_status['username'], login_status['identity']))


class Student:  # 学生类
    def check_all_courses(self):  # 查看所有课程方法
        with open('course', encoding='utf-8') as f1:
            for i in f1:
                i = i.strip().split('|')
                print('所有的课程: %s' % i)

    def student_login(self):  # 学生登录 方法
        while 1:
            l3 = {1: '查看所有课程', 2: '选择课程', 3: '查看所选课程', 4: '退出程序'}
            for k, v in l3.items(): print(k, v)
            num3 = input('\n请输入访问的编号:').strip()
            if num3 == '1': s1.check_all_courses()
            elif num3 == '2': s1.select_courses()
            elif num3 == '3': s1.check_the_course()
            else: quit()

    def select_courses(self):  # 选择课程 方法
        with open('select_courses', encoding='utf-8', mode='a') as f1:
            courses = input('请输选择课程:')
            f1.write('{}|{}\n'.format(courses, login_status['username']))

    def check_the_course(self):  # 查看所选课程 方法
        with open('select_courses', encoding='utf-8') as f1:
            for i in f1:
                i = i.strip().split('|')
                if login_status['username'] == i[1]: print('您选择的课程有: %s' % i[0])  # 只查看自己用户的课程

    def exit(self): quit() # 退出程序 方法


class Admin(Student):  # 管理员类, 继承Student部分方法
    def create_course(self):  # 创建课程 方法
        with open('course', encoding='utf-8', mode='a') as f1:
            courses = input('请输入课程名称:')
            f1.write('{}|'.format(courses))

    def admin_login(self):  # 管理员登录 方法
        while 1:
            l2 = {1: '创建课程', 2: '创建学生学生账号', 3: '查看所有课程',
                  4: '查看所有学生', 5: '查看所有学生的选课情况', 6: '退出程序'}
            for k, v in l2.items(): print(k, v)
            num2 = input('\n请输入访问的编号:').strip()
            if num2 == '1': a1.create_course()
            elif num2 == '2': a1.create_student()
            elif num2 == '3': a1.check_all_courses()
            elif num2 == '4': a1.check_all_student()
            elif num2 == '5': a1.check_all_student_course()
            else: quit()

    def create_student(self):  # 创建学生学生账号 方法
        username = input('请输入注册的账号:').strip()
        password = input('请输入注册的密码:').strip()
        with open('register', encoding='utf-8') as f1:
            for i in f1:
                i = i.strip().split('|')
                if username in i[0]:  # 判断用户是否存在
                    print('\033[31;1m学生%s已存在,请登录.\033[0m' % username)
                    break
            else:
                with open('register', encoding='utf-8', mode='a') as f2:
                    f2.write('{}|{}|Student\n'.format(username, password))
                    print('\033[33;1m学生%s帐号创建成功.\033[0m' % username)

    def check_all_student(self):  # 查看所有学生 方法
        with open('register', encoding='utf-8') as f1:
            for i in f1:
                i = i.strip().split('|')
                if i[2] == 'Student': print('所有的学生的账号: %s' % i[0])

    def check_all_student_course(self):  # 查看所有学生的选课情况 方法
        with open('select_courses', encoding='utf-8') as f1:
            for i in f1:
                i = i.strip().split('|')
                print('学生:%s 课程: %s' % (i[1], i[0]))
                
s1 = Student()  # 实例化对象 学生
a1 = Admin()   # 实例化对象 管理员


def index():  # 执行整个程序函数
    while 1:
        print('\033[33;1m欢迎来到校园管理系统\033[0m'.center(40, '-'))
        print('管理员: 张三, 密码:222\n')
        l1 = {0: '请登录', 1: '退出'}
        for k, v in l1.items(): print(k, v)
        num = input('\n请输入访问的编号:').strip()
        if num == '0':
            login()
            if login_status['identity'] == 'Admin': a1.admin_login()
            elif login_status['identity'] == 'Student': s1.student_login()
            else: break
            
        elif num == '1': break
        else: print('\033[31;1m无此编号\033[0m')
index()
