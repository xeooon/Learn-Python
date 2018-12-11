# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

'''
datetime模块
'''
# import datetime
# print('当前时间', datetime.datetime.now())
#
# # 只能调整的字段：weeks days hours minutes seconds
# print('当前时间的三周后', datetime.datetime.now() + datetime.timedelta(weeks=3))
# print('当前时间的三周前', datetime.datetime.now() + datetime.timedelta(weeks=-3))
# print('当前时间的三天前', datetime.datetime.now() + datetime.timedelta(days=-3))
# print('当前时间的三天后', datetime.datetime.now() + datetime.timedelta(days=3))
# print('当前时间的5小时前', datetime.datetime.now() + datetime.timedelta(hours=5))
# print('当前时间的5小时后', datetime.datetime.now() + datetime.timedelta(hours=-5))
# print('当前时间的15分钟前', datetime.datetime.now() + datetime.timedelta(minutes=-15))
# print('当前时间的15分钟后', datetime.datetime.now() + datetime.timedelta(minutes=15))
# print('当前时间的70秒前', datetime.datetime.now() + datetime.timedelta(seconds=-70))
# print('当前时间的70秒后', datetime.datetime.now() + datetime.timedelta(seconds=70))
#
#
# # 可直接调整到指定的 年 月 日 时 分 秒 等
# current_time = datetime.datetime.now()
#
# print('直接调整到1977年的当前时间',current_time.replace(year=1977))
# print('直接调整到1月份的当前时间', current_time.replace(month=1))
# print(current_time.replace(year=1989,month=4,day=25))  # 1989-04-25 18:49:05.898601
#
# # 将时间戳转化成时间
# print(datetime.date.fromtimestamp(1232132131))  # 2009-01-17


'''
shutil模块
高级的 文件、文件夹、压缩包 处理模块
'''
import shutil

# shutil.copyfileobj(fsrc, fdst[, length])
# 将文件内容拷贝到另一个文件中
# shutil.copyfileobj(open('shutil1', encoding='utf-8'), open('shutil2',encoding='utf-8', mode='w'))


# shutil.copyfile(src, dst)
# 拷贝文件
# shutil.copyfile('a1.log','abc.txt')  # 赋值重命名一个文件,目标文件，无需存在


# shutil.make_archive(base_name, format,...)
# 文件的打包
# import shutil
# import time
# ret = shutil.make_archive("blog_bak%s" %(time.strftime('%Y-%m-%d')), 'gztar', root_dir='blog')


# shutil.copymode(src, dst)
# 仅拷贝权限。内容、组、用户均不变
# shutil.copymode('f1.log', 'f2.log') #目标文件必须存在


# shutil.copystat(src, dst)
# 仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
# shutil.copystat('f1.log', 'f2.log') #目标文件必须存在


# shutil.copy(src, dst)
# 拷贝文件和权限
# import shutil
# shutil.copy('f1.log', 'f2.log')


# shutil.copy2(src, dst)
# 拷贝文件和状态信息
# import shutil
# shutil.copy2('f1.log', 'f2.log')


# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ignore=None)
# 递归的去拷贝文件夹
# import shutil
# shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*')) #目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除


'''
shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的，详细：
'''
# tar的解压
# import os
# import tarfile  # zip与tar一致

# dir1 = os.path.dirname(__file__)
# file_name = 'blog_bak2018-12-03.tar.gz'
# dir_name_path = os.path.join(dir1, file_name)
# print(dir_name_path)
#
# t = tarfile.open(dir_name_path, 'r')
# t.extractall('blog2')
# t.close()

'''
zipfile压缩解压缩
'''
# import zipfile

# 压缩
# z = zipfile.ZipFile('laxi.zip', 'w')
# z.write('a.log')
# z.write('data.data')
# z.close()

# 解压
# z = zipfile.ZipFile('laxi.zip', 'r')
# z.extractall(path='.')
# z.close()


'''
tarfile压缩解压缩
'''
# import tarfile

# 压缩
# t=tarfile.open('/tmp/egon.tar','w')
# t.add('/test1/a.py',arcname='a.bak')
# t.add('/test1/b.py',arcname='b.bak')
# t.close()

# 解压
# t=tarfile.open('/tmp/egon.tar','r')
# t.extractall('/egon')
# t.close()




'''
xml模块
'''
# import xml.etree.ElementTree as ET
# tree = ET.parse('二狗.xml')
# root = tree.getroot()
# print(root)  # <Element 'data' at 0x000000000274D548>
# print([tag for tag in root])

# 查
# print(root.iter('year'))  # 查询所有的year标签。
# for i in root.iter('year'):
#     print(i)

#
# print(root.find('country')) # 找到第一个就返回


# print(root.findall('country'))  # 找到子标签所有的country

# 找寻标签属性以及内容
#
# year_list = [year for year in root.iter('year')]
# print(year_list[0].attrib)
# print(year_list[0].text)




'''
# collections 模块
'''
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# # print(p[0])
# print(p.x)