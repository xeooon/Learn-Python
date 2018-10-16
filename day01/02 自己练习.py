# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


'''
程序的前几行
'''
# !/usr/bin/env python           # 指定Python解释器
# -*- encoding:utf-8 -*-         # 指定字符集编码
# CHANG_LIANG = 'ZhangZhiQiang'  # 常量优先写在前面


'''
变量和程序交互
'''
# name1 = 'xeon'
# age_of_student = 23

# name = input('请输入用户名:')   # input 输入的都是str类型
# print(name)

# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# name = input("What's your name ?")
# age = input("How old are you ?")
# hometown = input("Where is your hometown ?")
# print("Hello", name, "your are", age, "years old,", "you come from", hometown)


'''
基础数据类型
'''
# a = 2
# b = '2'
# print(type(a))
# print(type(b))


'''
字符串拼接
'''
# name = "xeon"
# age = "22"
# age2 = 22

# print(type(name))
# print(type(age2))

# print(msg)
# print(name + age)  # 字符串与字符串可以相加
# print(name*8)  # 字符串可以与数字相乘


'''
布尔值,成立就是True, 否则为False
'''
# a = 3
# b = 5
# print('a > b', a > b)
# print('a < b', a < b)


'''
格式化输出
'''
# 方法1:
# name = input('姓名: ')
# age = int(input('年龄: '))
# job = input('职业: ')
# hobby = input('爱好: ')
#
# msg = '''
# ------ 个人信息 ------
# 姓名 : %s
# 年龄 : %d
# 职业 : %s
# 爱好 : %s
# ----------------------
# ''' % (name, age, job, hobby)
# print(msg)

# 方法2:
# dic = {'name': '张志强', 'age': '23', 'job': 'IT', 'hobby': '骑行'}
# msg = '''
# ------ 个人信息 ------
# 姓名 : %(name)s
# 年龄 : %(age)s
# 职业 : %(job)s
# 爱好 : %(hobby)s
# ----------------------
# ''' % dic
# print(msg)


'''
求1-5阶乘之和
'''
# cheng = 1
# count = 1
# while count < 6:
#     cheng *= count
#     count += 1
# print(cheng)


'''
打印1 到100 的偶数,然后相加
'''
# 方法1:
# sum = 0
# count = 0
# while count < 101:
#     sum = sum + count
#     count += 2
# print(sum)

# 方法2:
# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 1:
#         count += 1
#         sum += count
#     print(count)
#     count = count + 1
# print(sum)


'''
打印1 到100 的奇数,然后相加
求100内所有奇数的和
'''
# 方法1:
# sum = 0
# count = 1
# while count < 101:
#    print(count)
#    sum += count
#    count += 2
# print(sum)

# 方法2:
# sum = 0
# count = 1
# while count < 101:
#     if count % 2 == 1:
#         sum = sum + count
#     print(count)
#     count = count + 2
# print(sum)


'''
打印一个边长为N的正方形
'''
# 方法1:
# flag = '#'
# count = 0
# while count < 3:
#     print(flag * 6)
#     count += 1

# 方法2:
# a = ' '
# msg = '''
# ######
# #%s%s%s%s#
# ######
# ''' % (a, a, a, a)
# print(msg)

'''
打印99 乘法表
1*1=1
1*2=2   2*2=4
1*3=3   2*3=6    3*3=9
1*4=4   2*4=8    3*4=12   4*4=16
1*5=5   2*5=10   3*5=15   4*5=20   5*5=25
1*6=6   2*6=12   3*6=18   4*6=24   5*6=30   6*6=36
1*7=7   2*7=14   3*7=21   4*7=28   5*7=35   6*7=42   7*7=49
1*8=8   2*8=16   3*8=24   4*8=32   5*8=40   6*8=48   7*8=56   8*8=64
1*9=9   2*9=18   3*9=27   4*9=36   5*9=45   6*9=54   7*9=63   8*9=72   9*9=81
'''


'''
打印100以内裴波纳契数列
斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13
特别指出：第0项是0，第1项是第一个1。从第三项开始(第二个1)，每一项都等于前两项之和。
定义a=0 b=1 .那么斐波那契数列就是    a   b    a+b
'''
# 方法1:
# x, y = 0, 1
# while x < 100:
#     print(x)
#     x, y = y, x + y

# 方法2:
# x = 0
# y = 1
# count = 1
# while count > 0:
#     z = x + y
#     x = y
#     y = z
#     if z > 100:
#         break
#     count += 1
#     print(z)


'''
指定一个5位数，判断该数的位数
依次打印出个位，十位，百位，千位，万位的数字
'''

