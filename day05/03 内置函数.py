# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
'''
内置函数
python 将一些常用的重要的功能,全部都封装到函数中,拿来即用.

'''

'''
已经学过的内置函数
input() print() open()  int() str()  tuple() set()
dict()  list()  float() len() bool() id()    next()  range()
'''


'''
作用域相关
locals()  : 获取当前作用域的所有的变量
globals() : 永远获取的是全局作用域,所有的变量
'''
# name = 'xeon'
# def func1():
#     a1 = '哈哈'
#     print(globals())  # 返回: 'name': 'xeon', 'func1': <function func1 at 0x000001895F521E18>
#     print(locals())  # 返回: {'a1': '哈哈'}
# func1()


'''
字符串类型代码的执行
慎用# 用的话,必须是写死的代码流程.
eval() : 执行字符串中的代码,并将结果返回给执行者    # 慎用
exec() : 执行字符串中的代码,没有返回值. 执行代码流. # 慎用
'''
# 例子1:
# a = '2 + 2'
# print(a)
# print(eval(a))

# 例子2:
# s = '''for i in [1, 2, 3]: print(i)'''
# exec(s)


'''
输入输出相关
input() : 函数接受一个标准输入, 返回str类型
print() : 打印输出
'''
# 源码分析
# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
#     """
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#     file:  默认是输出到屏幕，如果设置为文件句柄，输出到文件
#     sep:   打印多个值之间的分隔符，默认为空格
#     end:   每一次打印的结尾，默认为换行符
#     flush: 立即把内容输出到流文件，不作缓存
#     """

# 例子1: 指定分隔符
# print(11, 22, 33, sep='*')  # 返回11*22*33

# 例子2:合并两行
# print(111, end='')
# print(222)


'''
内存相关
hash() : 获取一个对象（可哈希对象：int，str，Bool，tuple）的哈希值
         将不可变的数据类型,hash成不同的等长的数字
         
id()   : 用于获取对象的内存地址
'''
# 例子1: hash的举例
# print(hash(12322))  # 数字返回本身
# print(hash('123'))  # 字符串返回的hash值是变动的
# print(hash('arg'))  # 字符串返回的hash值是变动的
# print(hash('alex'))  # 字符串返回的hash值是变动的
# print(hash(True))  # 返回 1
# print(hash(False))  # 返回 0
# print(hash((1, 2, 3)))  # 元组的hash值是固定的

# 例子2:比对内存地址
# a = 123
# b =a
# print(id(a))  # 返回 1424325472
# print(id(b))  # 返回 1424325472


'''
文件操作相关
open() : 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写
'''


'''
调用相关
callable() : 判断对象是否可调用,是否可以执行
             如果返回True，object仍然可能调用失败；
             但如果返回False，调用对象ojbect绝对不会成功。
'''
# 例子1:
# def add(a, b):
#     return a + b
# print(callable(add))  # 返回True


'''
查看内置属性
dir() : 获得当前模块的属性列表
'''
# print(dir('alex'))


'''
进制转换
bin：将十进制转换成二进制并返回。
oct：将十进制转化成八进制字符串并返回。
hex：将十进制转化成十六进制字符串并返回。
'''
# print(bin(10), type(bin(10)))  # 返回 0b1010 <class 'str'>
# print(oct(10), type(oct(10)))  # 返回 0o12 <class 'str'>
# print(hex(10), type(hex(10)))  # 返回 0xa <class 'str'>


'''
数学运算
abs()    ：函数返回数字的绝对值。
divmod() ：分页会用到,计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。
round()  ：保留浮点数的小数位数，默认保留整数。
pow()    ：求x**y次幂。（三个参数为x**y的结果对z取余）

sum：对可迭代对象进行求和计算（可设置初始值）。
min：返回可迭代对象的最小值（可加key，key为函数名，通过函数的规则，返回最小值）。
max：返回可迭代对象的最大值（可加key，key为函数名，通过函数的规则，返回最大值）。
'''
# 例子1:
# print(divmod(7, 3))  # 返回 (2, 1), （商数，余数）  **

# 例子2:
# print(sum(i for i in range(10)))  # 返回45
# print(sum([i for i in range(10)], 100))  # 设置初始值为100,返回145

# 例子3
# print(min(1, 2, 3, 4, 5))  # 返回 1
# print(min([1, 2, 3, 4, 5]))  # 返回1

# 例子4:
# 默认将可迭代对象中的每个元素依次传入函数中，按照函数的返回值去取最小元素。
# l1 = [('alex', 3), ('太白', 1), ('wS', 2)]
# def func(x):
#     return x[1]
# print(min(l1, key=func))  # 比较元组中第二位数值的大小, 返回 ('太白', 1)


'''
reversed  返回一个新的翻转的迭代器
'''
# 方法1:
# l1 = [2, 3, 4, 1]
# l1.reverse()
# print(l1)  # 返回 [1, 4, 3, 2]

# 方法2:
# l1 = [2, 3, 4, 1]
# l2 = reversed(l1)
# print(list(l2))  # 返回 [1, 4, 3, 2]


'''
format : 格式化输出
'''
# print(format('test', '<20'))  # 以20字符左对齐
# print(format('test', '>20'))  # 以20字符右对齐
# print(format('test', '^20'))  # 以20字符居中


'''
bytes：用于不同编码之间的转化
encode : 编码
decode : 解码
'''
# 方法1:
# s1 = '太白'
# unicode ---> utf-8 bytes
# b1 = s1.encode('utf-8')
# # print(b1)
# # utf-8 bytes ---> unicode
# s2 = b1.decode('utf-8')
# print(s2)

# 方法2: 将字符串转换为UTF-8显示
# s1 = '太白'
# # unicode ---> utf-8 bytes
# b1 = bytes(s1, encoding='utf-8')
# print(b1)

# 方法3: 通过输入字符找到 Unicode 对应的位置
# print(ord('中'))
# print(ascii('a'))
# print(ascii('中'))


'''
repr:返回一个对象的string形式（原形毕露）
'''
# 方法1：
# s1 = "alex"
# l3 = '[1,2,3]'
# print(s1)  # 返回 alex
# print(l3)  # 返回 [1,2,3]

# 方法2：
# s1 = "alex"
# l3 = '[1,2,3]'
# print(repr(s1))  # 返回 'alex'
# print(repr(l3))  # 返回 '[1,2,3]'

# 方法3：格式化输出的 %r
# s1 = '我叫%s, 我是%r' % ('alex', 'sb')
# print(s1)  # 返回 我叫alex, 我是'sb'


'''
数据集合
sorted：对所有可迭代的对象进行排序操作
enumerate:枚举，返回一个枚举对象
all：可迭代对象中，全都是True才是True
any：可迭代对象中，有一个True 就是True
'''
# 方法1
# l1 = [1, 2, 7, 6, 5, 4]
# l2 = sorted(l1)
# print(l2)  # 返回 [1, 2, 4, 5, 6, 7]

# 方法2: 以第元组的第二位排序
# l1 = [('alex', 3), ('太白', 1), ('wS', 2), ('wS', 4)]
# def func(x):
#     return x[1]
# new_l = sorted(l1, key=func, reverse=True)
# print(new_l)  # 返回 [('wS', 4), ('alex', 3), ('wS', 2), ('太白', 1)]

# 方法3:enumerate 1 默认枚举
# l1 = ['太白%s' % i for i in range(10)]
# for index in range(len(l1)):
#     print(index, l1[index])  # 返回 0 太白0  1 太白1 .... 9 太白9

# 方法4:enumerate 2 设置起始值枚举
# l1 = ['太白%s' % i for i in range(10)]
# for index, i in enumerate(l1, 10):
#     print(index, i)  # 指定起始值返回,  10 太白0 11 太白1 ..... 19 太白9

# 方法5: all 和 any
# print(all([1, 2, True, 100]))  # 返回 True
# print(any(['', 0]))   # 返回 False


'''
zip  拉链方法, 返回迭代器,以最小的可迭代元素为准
'''
# l1 = [1, 2, 3, 6, 7, 8, 9]
# l2 = ['a', 'b', 'c', 5]
# l3 = ('*', '**', (1, 2, 3))
#
# print(zip(l1, l2, l3))  # 返回 <zip object at 0x0000028F412A3408>
# for i in zip(l1, l2, l3):
#     print(i)  # 返回 (1, 'a', '*')
#               #      (2, 'b', '**')
#               #      (3, 'c', (1, 2, 3))


'''
filter 返回迭代器,过滤, 类比成列表推导式的筛选模式
'''
# l1 = [i for i in range(10) if i % 2 ==0]
# print(l1)

# l1 = [1, 2, 3, 4, 5, 6]
# def func(x): return x % 2 == 0
# obj1 = filter(func, l1)
# print(list(obj1))

'''
map 返回迭代器, 类比成列表推导式的循环模式
'''
# 返回列表的平方
# l1 = [1, 2, 3, 4, 5, 6]
# # def func(x): return x ** 2
# # print(list(map(func, l1)))


