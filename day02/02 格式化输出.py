# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn

# 格式化输出
# % 占位符
# 数据类型: s:字符串  d:整数  f:浮点数  r:内置函数会讲到
# 方法1：
# name = input('姓名:')
# age = int(input('年龄:'))
# job = input('工作:')
# hobby = input('爱好:')
# msg = """
# -----------------------------
# name  : %s
# age   : %d
# job   : %s
# hobby : %s
# -----------------------------
# """ % (name, age, job, hobby)
# print(msg)

# 方法2:
# dic = {'name': 'xeon', 'age': 23, 'job': 'IT', 'hobby': '骑行'}
# msg = """
# -----------------------------
# name  : %(name)s
# age   : %(age)d
# job   : %(job)s
# hobby : %(hobby)s
# -----------------------------
# """ % dic
# print(msg)

# 方法3:
# 在格式化输出中,只想单纯的表示%(百分号), 那么要写%%(两个百分号)
# msg = '我叫%s, 今年%d, 学习进度5%%' % ('XEON', 18)
# print(msg)

# 总结:
# 如果你想制作一个字符串类的模版, 或者是想让字符串某些位置,变成动态输入,此时你要想到字符串拼接或者格式化输出.


