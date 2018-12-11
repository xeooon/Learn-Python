# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
# 异常分两种
# 语法异常：需要我们手动排除
# 逻辑异常：在特殊情况下使用，正常手段解决费劲可以使用。


'''
异常举例
'''
# if 3>2:
#     print(666)
#    print(777)  # IndentationError 缩进问题

# l1 = [1, 2, 3]
# print(l1[100])  # IndexError 没有此索引

# dic = {'name': '张三'}
# print(dic.get('age'))  # None
# print(dic['age'])  # KeyError 没有此key



'''
异常处理
'''
# if else .... 对于if语句处理异常只能处理简单的，如果考虑多个条件，不合适


'''
单分支try except
'''
# 尝试着运行try里面的代码，出现错误，按照错误类型去寻找相应的excepct，找到执行此except,然后程序继续运转
# try:
#     print(111)
#     print(222)
#     print(333)
#     name  # 只看第一个错误，如果匹配上了exceptname就跳过下面的错误，直接执行except
#     l1 = [1, 2, 3]  # 这里是不运行的
#     print(l1[100])  # 这里是不运行的
# except NameError:
#     print('name没有定义')
#
# print(666)


'''
多支情况。try except except except ....
'''
# try:
#     print(111)
#     print(222)
#     print(333)
#
#     name
#     l1 = [1,2,3]
#     print(l1[100])
#     asdf
# except NameError:
#     print('name is not defined')
# except IndexError:
#     print('没有此value')
# print(666)


'''
万能处理，任何错误都接收
'''
# try:
#     print(111)
#     print(222)
#     print(333)
#
#     name
#     l1 = [1,2,3]
#     print(l1[100])
#     asdf
# except NameError:
#     print('name is not defined')
# except IndexError:
#     print('没有此value')
#
# except Exception:  # 最后走
#     print('没有此东西')
#
# print(666)

# 万能： 如果你对错误原因不关心，只是想不让其报错，那么程序中你就用万能处理。
# 如果你对错误原因需要进行不同分流或者程序处理，那么就需要多分支。


'''
多分支 加 万能处理。 
对某些错误需要进行分流处理，剩下的错误直接跳过。
'''
# try:
#     print(111)
#     print(222)
#     print(333)
#     # name
#     int(input(''))
#     l1 = [1, 2, 3]
#     print(l1[100])
#     dic = {'name': 'alex'}
#     print(dic['age'])
#
#
# except NameError:
#     print('name  is not defined')
#
# except IndexError:
#     print('索引超出范围....')
#
# except KeyError:
#     print('没有此key...')
#
# except Exception:
#     pass
# print(666)


'''
try except else
如果出现异常 就不会走else逻辑，不出现异常，则执行else逻辑。
'''
# try:
#     print(111)
#     print(222)
#     name
#
# except NameError:
#     print('name  is not defined')
#
# else:
#     print(333)
# print(666)


# try:
#     print('二狗 向 脸哥转了 200元')
#     name
#     print('脸哥确认收到了 200元')
#
# except NameError:
#     print('name  is not defined')
#
# else:
#     print('转账成功')
# print(666)


'''
try except else finally
finally 无论报不报错都执行，如果报错，finally是在报错之前执行的！！！
'''
# try:
#     print('二狗 向 脸哥转了 200元')
#     name
#     print('脸哥确认收到了 200元')
#
# except KeyError:
#     print('name  is not defined')
# #
# # else:
# #     print('转账成功')
# #
# finally:
#     print(666)


'''
各种对文件操作的代码,但是可能会出错，出错之后，你的文件句柄无法关闭。
'''
# 解决方案：
# try:
#     f1 = open('a.log', encoding='gbk')
#     f1.read()
#     f1.write('sfdsf')
#     '''
#     各种对文件操作的代码,但是可能会出错，出错之后，你的文件句柄无法关闭。
#     '''
# finally:
#     print(666)
#     f1.close()


'''
finally 会在retrurn之前先执行。
以后如果遇到关闭连接，数据库连接等等。
'''
# def func(a):
#     try:
#         a += 1
#         return a  # 后执行
#     finally:
#         print(333)  # 先执行
#
# print(func(5))


'''
自定义异常处理。
'''
# raise

# raise 666

# python提供了大部分异常，但是不是所有，比如 大的框架的手机连接问题，网络引发的代码问题等等。
# Exception 也处理不了。
#
# EOFError
# NameError
# Exception


# 程序中如果出现了python解决不了的异常 比如 PhoneConnectionError
# class PhoneConnectionError(BaseException):
#     pass
# try:
#     raise PhoneConnectionError('类型错误')
# except PhoneConnectionError:
#     print('手机连接出现问题')

# 源码中经常遇到  条件只要不成立，我就抛出错误
# assert 1 == 2