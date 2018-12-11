# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
import subprocess
# 执行系统命令模块

obj = subprocess.Popen('whoami',
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

ret = obj.stdout.read().decode('utf-8')
ret1 = obj.stderr.read().decode('utf-8')

print(ret)
print(ret1)


# shell: 命令解释器，相当于调用cmd 执行指定的命令。
# stdout:正确结果丢到管道中。
# stderr:错了丢到另一个管道中。
# windows操作系统的默认编码是gbk编码。
