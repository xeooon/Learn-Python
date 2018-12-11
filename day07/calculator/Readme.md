### 作者

    标题 : 24期周末班 - day07 - 计算器作业
    作者 : 张志强
    QQ号 : 1344683865
    微信 : qingniaoxiaoqiang
    邮箱 : Xeon@xeon.org.cn

## Calculator

[![Python3](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)](https://www.python.org/)

作业需求: 实现加减乘除及拓号优先级解析

    用户输入 
    1 - 2 * ((60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
    等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式
    
注意：

    不能调用eval等类似功能偷懒实现

踩分点:

    练习题：30
    基本实现：50 
    代码写的清晰、健壮、可扩展：10


### 功能

    此计算器只识别加法、减法、乘法、除法、括号、0-9的运算。

### 使用

    如果想计算其他的，请编辑/calculator/bin/start.py文件，取消注释用户输入calculate_input。
    ➜  day07 cd calculator
    ➜  calculator ll
    total 144
    -rw-r--r--  1 xeon  staff   1.6K 11 28 13:20 Readme.md
    -rw-r--r--  1 xeon  staff   103B 11 28 14:11 __init__.py
    drwxr-xr-x  4 xeon  staff   128B 11 28 14:12 bin
    drwxr-xr-x  5 xeon  staff   160B 11 28 14:15 conf
    drwxr-xr-x  5 xeon  staff   160B 11 28 14:12 core
    drwxr-xr-x  5 xeon  staff   160B 11 28 14:12 lib
    drwxr-xr-x  4 xeon  staff   128B 11 28 13:40 log
    -rwxr-xr-x  1 xeon  staff    64K 11 20  2016 流程图.png
    ➜  calculator python3 ./bin/start.py
    ============================================================
    欢迎使用计算器:
    此计算器只支持此[0-9, +, -, *, /, (, )]范围的元素
    ============================================================
    
    最终结果为: 2776672.6952380957

### 项目骨架

    .
    └── calculator             // 项目所在根目录
       ├── bin                 // 命令目录
       │   └── start.py        // 启动文件
       ├── conf                // 配置目录
       │   └── settings.py     // 配置文件
       ├── core                // 核心逻辑目录
       │   └── src.py          // 逻辑文件
       ├── lib                 // 公共组建
       │   └── commom.py       // 公共模块方法
       ├── log                 // 日志目录
       │   └── exec.log        // 执行函数的日志
       └── Readme.md           // 配置目录
