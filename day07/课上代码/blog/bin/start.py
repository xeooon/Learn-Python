# import src  直接引用不行，src这个模块没在这三个当中
# 先从内存 ---> 内置模块（os,time sys..） ---> sys.path
import sys
import os
# sys.path.append(r'D:\24期周末班\day07\blog')
# print(__file__)  # 文件的当前目录
# print(os.path.dirname(os.path.dirname(__file__)))  # 获取到了项目根目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
from core import src




if __name__ == '__main__':
    src.run()