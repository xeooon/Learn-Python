# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 文件路径:文件的路径
# 编码方式: gbk utf-8
# 执行动作：读 写 删 ....


# f1 = open('d:\哈哈.txt', encoding='utf-8', mode='r')
# content = f1.read()
# print(content, type(content))
# f1.close()


'''
open() 内置函数,操作文件
f1 文件句柄 f1,fh , file_handle
f1.close() 关闭

1.打开文件产生文件句柄,
2.对文件句柄进行相应的操作(读,写,追加,读写...)
3.关闭文件句柄.

'''

'''
导致错误的原因:
1.路径 \n, \\U, \t ,解决方式:路径前加r
2.\\UXXXXX escape , decode incode error 错误, 编码方式不一致
3.路径
    绝对路径: 从c,d,e盘等开始的路径
    相对路径: 当前的目录下,同一个文件夹

'''


'''
读(默认是r模式)
'''
# r
# 第一种read() 全部读取
# 第二种read(n) 按字符读取
# 第三种readline() 按行读取
# 第四种readlines() 按多行读取 返回一个列表,列表中的每个元素是原文件的一行
# 第五种for循环文件句柄
    # f1是一个可迭代对象(由多个元素组成),节省内存
    
# f1 = open('alex与sb', encoding='utf-8')
# for line in f1:
#     print(line.strip())
# f1.close()


# rb  处理,图片和视频
# f1 = open('美女1.jpg', mode='rb')
# content = f1.read()
# print(content)
# f2 = open('美女2.jpg', mode='wb')
# f1.close()
# f2.close()
#
# f1.close()


# r+ 先读后写(追加)

# r+b



'''
写
'''

# w
# 1.没有文件创建文件,写入内容
# 2.有文件先清空,后写入
# f1 = open('log1', encoding='utf-8', mode='w')
# f1.write('又好了')
# f1.close()

# read(n)
#     r模式,按照字符读取
#     rb模式,按照字节读取



# rb  处理,图片和视频
# wb
# f1 = open('美女.jpg', mode='rb')
# content = f1.read()
# print(content)
# f1.close()


# w+ 先写后读


#
#
#  w+b
#



'''
追加
'''
# a
# 1.没有文件创建文件,写入内容
# 2.有文件直接在后面追加
# f1 = open('log2', encoding='utf-8', mode='a')
# f1.write('喇叭坏了')
# f1.close()


#a+

# ab a+b




'''
文件操作的常用方法:
read() 读
readable() 是否可读
witeable() 是否可写

实际用途,断点续传.ftp作业
seek() 调整光标的位置,按照字节
tell() 告诉你光标的位置,按照字节
'''

f1 = open('alex与sb', encoding='utf-8')
content = f1.read(3)
print(f1.tell())
f1.close()

# f1 = open('alex与sb', encoding='utf-8')
# f1.seek(9)
# content = f1.read()
# print(content)
# f1.close()


'''
文件的改操作
    1.以读的模式打开原文件
    2.以写的模式打开一个新文件
    3.对原文件的内容进行修改,形成新内容,写入新文件
    4.删除原文件
    5.将新文件重命名为原文件

'''
# 方法1:
# import os
# with open('alex美文', encoding='utf-8') as  f1, \
#     open('alex美文.bak',encoding='utf-8', mode='w') as f2:
#     for line in f1:
#         new_line = line.replace('SB', 'alex')
#         f2.write(new_line)
# os.remove('alex美文')
# os.rename('alex美文.bak', 'alex美文')



# 方法2:
# import os
# with open('alex美文', encoding='utf-8', mode='r') as f1, \
#     open('alex美文.bak', encoding='utf-8', mode='w') as f2:
#     old_line = f1.read().replace('alex', 'SB')
#     new_line = f2.write(old_line)
# os.remove('alex美文')
# os.rename('alex美文.bak', 'alex美文')


