# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""


'''
一，文件操作基本流程
'''
# # 打开文件,得到文件句柄并赋值给一个变量
# f = open('a.txt',encoding='utf-8')  # 默认打开模式就为r
#
# data = f.read()  # 通过文件句柄文件进行操作
#
# f.close()  # 关闭文件


'''
关闭文件的注意事项
'''

# f.close()  # 回收操作系统打开的文件
# del f  # 回收应用程序的变量

# with open('a.txt', encoding='utf-8', mode='r') as f1:
#     data = f1.read()
#     f1.write(data)

'''
文件操作方法
'''

# #1. 打开文件的模式有(默认为文本模式)：
# r ，只读模式【默认模式，文件必须存在，不存在则抛出异常】
# w，只写模式【不可读；不存在则创建；存在则清空内容】
# a， 只追加写模式【不可读；不存在则创建；存在则只追加内容】
#
# #2. 对于非文本文件，我们只能使用b模式，"b"表示以字节的方式操作（而所有文件也都是以字节的形式存储的，使用这种模式无需考虑文本文件的字符编码、图片文件的jgp格式、视频文件的avi格式）
# rb
# wb
# ab
# 注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型，不能指定编码
#
# #3,‘+’模式（就是增加了一个功能）
# r+， 读写【可读，可写】
# w+，写读【可写，可读】
# a+， 写读【可写，可读】
#
# #4，以bytes类型操作的读写，写读，写读模式
# r+b， 读写【可读，可写】
# w+b，写读【可写，可读】
# a+b， 写读【可写，可读
#
# read（3）：
#
# 　　1. 文件打开方式为文本模式时，代表读取3个字符
#
# 　　2. 文件打开方式为b模式时，代表读取3个字节
#
# 其余的文件内光标移动都是以字节为单位的如：seek，tell，truncate
#
# 注意：
#
# 　　1. seek有三种移动方式0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的
#
# 　　2. truncate是截断文件，所以文件的打开方式必须可写，但是不能用w或w+等方式打开，因为那样直接清空文件了，所以truncate要在r+或a或a+等模式下测试效果。


'''
文件的修改
'''
# 方法1:
# 将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，
# 修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）
# import os
# with open('a.txt', encoding='utf-8',mode='r') as read_f, \
#         open('a.txt.bak', encoding='utf-8', mode='w') as write_f:
#     data = read_f.read()  # 全部读入内存,如果文件很大,会很卡
#     data = data.replace('alex', 'SB')  # 在内存中完成修改
#
#     write_f.write(data)  # 一次性写入新文件
# os.remove('a.txt')  # 删除原文件
# os.rename('a.txt.bak', 'a.txt')  # 将新建的文件,重命名为原文件


# 方法2:将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件
# import os
# with open('a.txt', encoding='utf-8', mode='r') as  read_f, \
#     open('a.txt.bak', encoding='utf-8',mode='w') as write_f:
#     for line in read_f:
#         line = line.replace('SB', 'alex')
#         write_f.write(line)
# os.remove('a.txt')
# os.rename('a.txt.bak','a.txt')
