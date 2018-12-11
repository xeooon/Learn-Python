# sys
import sys
# print(sys.path)
# sys.exit()  # 终止程序
# print(666)
# print(sys.version)
# print(sys.platform)  # 返回windows系统名称
# print(sys.modules)  # 解释器自动加载到内存的模块和包

# os
import os
# print(os.getcwd())  # 获取当前工作目录
# os.makedirs('文件夹a/文件夹b/文件夹c')  # 可生成多层递归目录
# os.removedirs('文件夹a/文件夹b/文件夹c')  # 递归删除空目录
# os.remove(r'D:\24期周末班\day07\文件夹a\文件夹b\b') # 删除文件
# os.rename(r"D:\24期周末班\day07\文件夹a\文件夹b\a1","狗哥")  #重命名文件/目录
# print(os.stat('狗哥'))
# print(os.path.abspath('狗哥'))
# print(__file__)  # 本文件绝对路径
# print(os.path.split(__file__))  # 将path分割成目录和文件名二元组返回
# print(os.path.dirname(__file__))  #  返回path的目录。其实就是os.path.split(path)的第一个元素
# print(os.path.basename(__file__)) # 文件名
# print(os.path.exists('狗哥'))
# print(os.path.dirname(r'D:\24期周末班\day07\狗哥'))
# print(os.path.basename(r'D:\24期周末班\day07\狗哥'))
# print(os.path.join(r'D:\24期周末班\day07', '狗哥'))

# time
import time
# 时间存在形式： 时间戳
# print(time.time())

# 格式化时间 咱们能看懂的时间 format time
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y{}%m{}%d{} %H:%M:%S').format('年', '月', '日'))

# 结构化时间
# print(time.localtime())


# 时间戳 ---> 格式化时间
# 1 先转化成结构化时间
# t = time.time()
# st = time.localtime(t)
# # print(st)
# # print(st.tm_year,st.tm_hour)
# # print(st[0])
# # 2转化成格式化时间
# ft = time.strftime('%Y-%m-%d',st)
# print(ft)


