#! /usr/bin/env python
# -*- encoding:utf-8 -*-
"""
标题 : 24期周末班 - day02 - 习题和作业
作者 : 张志强
QQ号 : 1344683865
微信 : qingniaoxiaoqiang
邮箱 : Xeon@xeon.org.cn
"""

# ###################################### 练习题 #######################################


'''
1、有变量name = "aleX leNb" 完成如下操作：
name = "aleX leNb"
'''
# name = "aleX leNb"

# ---> 01) 移除 name 变量对应的值两边的空格,并输出处理结果
# name = " aleX leNb "
# print(name.strip())

# ---> 02) 移除name变量左边的"al"并输出处理结果
# name = "aleX leNb"
# print(name.lstrip('al'))

# ---> 03) 移除name变量右面的"Nb",并输出处理结果
# name = "aleX leNb"
# print(name.rstrip('Nb'))

# ---> 04) 移除name变量开头的a"与最后的"b",并输出处理结果
# name = "aleX leNb"
# print(name.strip('ab'))

# ---> 05) 判断 name 变量是否以 "al" 开头,并输出结果
# name = "aleX leNb"
# print(name.startswith('al'))

# ---> 06) 判断name变量是否以"Nb"结尾,并输出结果
# name = "aleX leNb"
# print(name.endswith('Nb'))

# ---> 07) 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# name = 'aleX leNb'
# print(name.replace('l', 'p'))

# ---> 08) 将name变量对应的值中的第一个"l"替换成"p",并输出结果
# name = 'aleX leNb'
# print(name.replace('l', 'p', 1))

# ---> 09) 将 name 变量对应的值根据所有的"l" 分割,并输出结果。
# name = 'aleX leNb'
# name2 = name.split('l')
# print(name2)

# ---> 10) 将name变量对应的值根据第一个"l"分割,并输出结果。
# name = 'aleX leNb'
# name2 = name.split('l', 1)
# print(name2)

# ---> 11) 将 name 变量对应的值变大写,并输出结果
# name = 'aleX leNb'
# print(name.upper())

# ---> 12) 将 name 变量对应的值变小写,并输出结果
# name = 'aleX leNb'
# print(name.lower())

# ---> 13) 将name变量对应的值首字母"a"大写,并输出结果
# 方法1：
# name = 'aleX leNb'
# name_2 = name.replace(name[0], name[0].upper())
# print(name_2)


# 方法2：
# name = 'aleX leNb'
# for i in name:
#     if i == name[0]:
#         name_2 = name[0].upper() + name[1:-1]
#         print(name_2)


# ---> 14) 判断name变量对应的值字母"l"出现几次，并输出结果
# name = 'aleX leNb'
# print(name.count('l'))

# ---> 15) 如果判断name变量对应的值前四位"l"出现几次,并输出结果
# name = 'aleX leNb'
# print(name.count('l', 0, 5))

# ---> 16) 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
# name = "aleX leNb"
# print(name.index('N'))
# #print(name.index('找不到报错'))

# ---> 17) 从name变量对应的值中找到"N"对应的索引(如果找不到则返回‐1)输出结果
# name = "aleX leNb"
# print(name.find('N'))
# # print(name.find('找不到返回-1'))

# ---> 18) 从name变量对应的值中找到"X le"对应的索引,并输出结果
# name = "aleX leNb"
# s = 'X le'
# for i in s:
#     if i in name:
#         print(name.find(i, 3))

# ---> 19) 请输出 name 变量对应的值的第 2 个字符?
# name = "aleX leNb"
# print(name[2])

# ---> 20) 请输出 name 变量对应的值的前 3 个字符?
# name = "aleX leNb"
# print(name[:3])

# ---> 21) 请输出 name 变量对应的值的后 2 个字符?
# name = "aleX leNb"
# print(name[-2:])

# ---> 22) 请输出 name 变量对应的值中 "e" 所在索引位置?
# name = "aleX leNb"
# n = (name.find('e'))
# print((name.find('e')), name.find('e', n+1))


'''
2、有字符串s = "123a4b5c"
'''
# s = "123a4b5c"
# ---> 01) 通过对s切片形成新的字符串s1,s1 = "123"
# s = "123a4b5c"
# print(s[:3])

# ---> 02) 通过对s切片形成新的字符串s2,s2 = "a4b"
# s = "123a4b5c"
# print(s[3:6])

# ---> 03) 通过对s切片形成新的字符串s3,s3 = "1345"
# s = "123a4b5c"
# print(s[:-1:2])
# print(s[:7:2])

# ---> 04) 通过对s切片形成字符串s4,s4 = "2ab"
# s = "123a4b5c"
# print(s[1:6:2])
# print(s[1:-1:2])

# ---> 05) 通过对s切片形成字符串s5,s5 = "c"
# s = "123a4b5c"
# s5 = s[-1]
# print(s5)

# ---> 06) 通过对s切片形成字符串s6,s6 = "ba2"
# s = "123a4b5c"
# s6 = s[-3:-8:-2]
# print(s6)


'''
3、使用while或for循环分别打印字符串s="asdfer"中每个元素。
'''
# s = 'asdfer'
# for i in s:
#     print(i)


'''
4、使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
'''
# 方法1：
# s = "asdfer"
# for i in s:
#     print(s)

# 方法2：
# s = "asdfer"
# [print(s) for i in s]


'''
5、使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
'''
# s = "abcdefg"
# for i in s:
#     print(i+'sb')


'''
6、使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
'''
# s = "321"
# for i in s:
#     if i == s[0]:
#         print('倒计时%s秒.' % i)
#     if i == s[1]:
#         print('倒计时%s秒.' % i)
#     if i == s[2]:
#         print('倒计时%s秒,出发!' % i)

'''
7、实现一个整数加法计算器(两个数相加)：
如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
'''
# content = input("请输入整数计算的内容,例如5+9\n>> ").split('+')
# a = int(content[0])
# b = int(content[-1])
# print('>>', a+b)


'''
8、升级题：实现一个整数加法计算器（多个数相加）：
如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
'''
# content = input("请输入计算的内容(整数相加),例如1+..+20.\n>> ").split('+')
# sum = 0
# for i in content:
#     if i == '':
#         continue
#     sum += int(i)
# print('>>', sum)


'''
9、计算用户输入的内容中有几个整数（以个位数为单位）。
如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla
'''
# content = list(input("请输入内容:").strip())
# lis_int = []
# for i in content:
#     if (i.isdigit()):
#         lis_int.append(i)
# print(len(lis_int))


'''
10、写代码，完成下列需求：
用户可持续输入（用while循环），用户使用的情况：
输入A，则显示走大路回家，然后在让用户进一步选择：
是选择公交车，还是步行？选择公交车，显示10分钟到家，并退出整个程序。
选择步行，显示20分钟到家，并退出整个程序。
输入B，则显示走小路回家，并退出整个程序。
输入C，则显示绕道回家，然后在让用户进一步选择：是选择游戏厅玩会，还是网吧？
选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
'''
# flag = True
# while flag:
#     home = input("""请选择回家的方式:\nA 大路回家\nB 小路回家\nC 绕道回家\nD 不回家了\n>>>""").strip().upper()
#     if home == 'A':
#         A1 = input('A1 公交车? A2 步行?\n>>').strip().upper()
#         if A1 == '公交车' or A1 == 'A1':
#             print('坐公交10分钟到家.')
#             flag = False
#         else:
#             print('步行20分钟到家.')
#             flag = False
#     elif home == 'B':
#         print('走小路回家.')
#         flag = False
#     elif home == 'C':
#         C1 = input('C1 游戏厅? C2 网吧?\n>>').strip().upper()
#         if C1 == '游戏厅' or C1 == 'C1':
#             print('一个半小时到家，爸爸在家，拿棍等你.\n')
#         else:
#             print('两个小时到家，妈妈已做好了战斗准备.\n')
#         continue
#     else:
#         print('一路走好!')
#         break


'''
11、写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
'''
# sum = 0
# for i in range(1, 100):
#     if i == 88:
#         continue
#     if i % 2 == 0:
#         sum -= i
#     if i % 2 == 1:
#         sum += i
# print(sum)


'''
16、制作趣味模板程序需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
如：敬爱可亲的xxx，最喜欢在xxx地方干xxx
'''
# name = input('请输入名字:').strip()
# site = input('请输入地点:').strip()
# hobby = input('请输入爱好:').strip()
# msg = '敬爱可亲的: %s,最喜欢在%s地方干%s' % (name, site, hobby)
# print(msg)


'''
17、等待用户输入内容，检测用户输入内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重
新输入”，并允许用户重新输入并打印。敏感字符：“小粉嫩”、“大铁锤”
'''
li = ['小粉嫩', '大铁锤']
# flag = True
# while flag:
#     inp = input('请输入内容\n>>>').strip()
#     for i in li:
#         if inp.find(i) >= 0:
#             print('存在敏感字符,请重新输入\n')
#             break
#     else:
#         print('\n输入内容为\n', inp)
#         flag = False


'''
18、写代码，有如下列表，按照要求实现每一个功能
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
'''
# ---> 01) 计算列表的长度并输出
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))

# ---> 02) 列表中追加元素"seven",并输出添加后的列表
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li.append("seven")
# print(li)

# ---> 03) 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li.insert(0, "Tony")
# print(li)

# ---> 04) 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li[2] = "Kelly"
# print(li)

# ---> 05) 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# l2 = [1, "a", 3, 4, "heart"]
# li.extend(l2)
# print(li)

# ---> 06) 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# s = "qwert"
# li.extend(s)
# print(li)

# ---> 07) 请给列表添加元素"eric",并输出添加后的列表
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li.append("eric")
# print(li)

# ---> 08) 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(li.pop(1))
# print(li)

# ---> 09) 请删除列表中的第2至4个元素，并输出删除元素后的列表
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# del li[2:5:2]
# print(li)

# ---> 10) 请将列表所有得元素反转，并输出反转后的列表
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li.reverse()
# print(li)

# ---> 11) 请计算出"alex"元素在列表li中出现的次数，并输出该次数。
# 方法1:
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(li.count("alex"))

# 方法2:
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# sum = 0
# for i in li:
#     if i == 'alex':
#         sum += 1
# print(sum)


'''
19、写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
'''
# ---> 01) 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l1 = li[0:3]
# print(l1)

# ---> 02) 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l2 = li[3:6]
# print(l2)

# ---> 03) 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l3 = li[::2]
# print(l3)

# ---> 04) 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l4 = li[1:6:2]
# print(l4)

# ---> 05) 通过对li列表的切片形成新的列表l5,l5 = ["c"]
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l5 = li[-1]
# print(l5)

# ---> 06) 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l6 = li[-3:-8:-2]
# print(l6)

'''
20、写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
'''
# ---> 01) 将列表lis中的"tt"变成大写（用两种方式）。
# 方法1:
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][0] = 'TT'
# print(lis)

# 方法2:
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)

# ---> 02) 将列表中的数字3变成字符串"100"（用两种方式）。
# 方法1:
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[1] = lis[3][2][1][1] = '100'
# print(lis)

# 方法2:
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[1] = int(lis[1]) + 97
# print(lis)

# ---> 03) 将列表中的字符串"1"变成数字101（用两种方式）。
# 方法1:
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][2] = 101
# print(lis)

# 方法2:
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[-3][-2][-1][-1] = 101
# print(lis)


'''
21、请用代码实现：
li = ["alex", "eric", "rain"]
利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
'''
# li = ["alex", "eric", "rain"]
# l1 = '_'.join(li)
# print(l1)


'''
22、利用for循环和range打印出下面列表的索引。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
'''
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)

'''
23、利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
'''
# li = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         li.append(i)
# print(li)


'''
24、利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
'''
# li = []
# for i in range(0, 51):
#     if i % 3 == 0:
#         li.append(i)
# print(li)


'''
25、利用for循环和range从100~1，倒序打印。
'''
# for i in range(100, 0, -1):
#     print(i)


'''
26、利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛
选，将能被4整除的数留下来。
'''
# li = []
# for i in range(100, 9, -1):
#     if i % 2 == 0:
#         li.append(i)
# for i in li:
#     if i % 4 == 0:
#         li.remove(i)
# print(li)


'''
26、利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
'''
# li = []
# for i in range(1, 31):
#     if i % 3 == 0:
#         i = '*'
#         li.append(i)
# print(li)


'''
27、查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添
加到一个新列表中,最后循环打印这个新列表。
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
'''
# 方法1:
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
# l1 = []
# for i in li:
#     i = i.strip()
#     if i.startswith('a') and i.startswith('A'):
#         l1.append(i)
#     if i.endswith('c'):
#         l1.append(i)
# print(l1)

# 方法2:
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
# l1 = []
# for i in li:
#     i = i.strip()
#     if i.startswith('a') and i.startswith('A') or i.endswith('c'):
#         l1.append(i)
# print(l1)


'''
28、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入
的内容没有敏感词汇，则直接添加到上述的列表中。
'''
# 方法1:
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# a = input('请输入评论:\n>>>').strip()
# b = []
# for i in li:
#     if i in a:
#         a = a.replace(i, '*' * len(i))
#         b.append(a)
#         break
# else:
#     b.append(a)
# print('评论结果为:\n>', b)

# 方法2:
# a = input('请输入:>')
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# new_li = []
# for s in li:
#     a = a.replace(s, '*'*len(s))
# print('您输入的字符为(已过滤敏感字符)：', a)
# new_li.append(a)
# print('不知道为什么要加入这个列表：', new_li)


'''
29、有如下变量（tu是个元祖），请实现要求的功能
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
'''
# ---> 01) 讲述元祖的特性
# a.元组是不可更改的
# b.元组的str, dict的内容是可以更改的
# c.元组的内容可以是:int, list, bool, str, tuple, dict

# ---> 02) 请问tu变量中的第一个元素 "alex" 是否可被修改？
# 不可以

# ---> 03) 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
# print('k2为列表数据类型,可更改', type(tu[1][2]['k2']))
# tu[1][2]['k2'].append('Seven')
# print(tu)

# ---> 04) 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
# print('k3为元组类型,不可更改', type(tu[1][2]['k3']))


'''
30、字典dic,dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
'''
# ---> 01) 请循环输出所有的key
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# for i in dic:
#     print(i)

# ---> 02) 请循环输出所有的value
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# for k, v in dic.items():
#     print(v)

# ---> 03) 请循环输出所有的key和value
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# for k, v in dic.items():
#     print(k, v)

# ---> 04) 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# dic.setdefault("k4", "v4")
# print(dic)

# ---> 05) 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# dic['k1'] = 'alex'
# print(dic)

# ---> 06) 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# dic['k3'].append(44)
# print(dic)

# ---> 07) 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# 方法1:
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# dic['k3'].insert(0, 18)
# print(dic)

# 方法2:
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# dic['k3'] = [18, 11, 22, 33]
# print(dic)


'''
31、如下
'''
av_catalog = {
    "欧美": {"www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
           "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
           "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
           "x‐art.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]},
    "日韩": {"tokyo‐hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]},
    "大陆": {"1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]}
}

# ---> 01) 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'
# print('修改前:', av_catalog["欧美"]["www.youporn.com"])
# av_catalog["欧美"]["www.youporn.com"].insert(1, '量很大')
# print('修改后:', av_catalog["欧美"]["www.youporn.com"])

# ---> 02) 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# print('修改前:', av_catalog["欧美"]["x‐art.com"])
# av_catalog["欧美"]["x‐art.com"].pop()
# print('修改后:', av_catalog["欧美"]["x‐art.com"])

# ---> 03) 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# print('修改前:', av_catalog["日韩"]["tokyo‐hot"])
# av_catalog["日韩"]["tokyo‐hot"][1] = av_catalog["日韩"]["tokyo‐hot"][1].upper()
# print('修改后:', av_catalog["日韩"]["tokyo‐hot"])

# ---> 04) 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# print('修改前:', av_catalog["大陆"])
# av_catalog["大陆"].setdefault('1048', ['一天就封了'])
# print('修改后:', av_catalog["大陆"])

# ---> 05) 删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
# print('修改前:', av_catalog["欧美"])
# av_catalog["欧美"].pop("letmedothistoyou.com")
# print('修改后:', av_catalog["欧美"])

# ---> 06) 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# print('修改前:', av_catalog["大陆"])
# av_catalog["大陆"]["1024"][0] = av_catalog["大陆"]["1024"][0]+',可以爬下来'
# print('修改后:', av_catalog["大陆"])

'''
32、有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
'''
# s = "k:1|k1:2|k2:3|k3:4"
# dic = {}
# for i in s.split('|'):
#     k, v = (i.split(':'))
#     dic.setdefault(k, v)
# print(dic)


'''
33、元素分类
有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于
66 的值保存至第二个key的值中。
即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
'''
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {}
# for i in li:
#     if i < 66:
#         li_1 = dic.setdefault('k1', [])
#         li_1.append(i)
#     else:
#         li_2 = dic.setdefault('k2', [])
#         li_2.append(i)
# print(dic)


# ###################################### 作业 #######################################


'''
作业：购物车
    1. 用户先给自己的账户充钱：比如先充3000元。
    2. 页面显示 序号 + 商品名称 + 商品价格，如：
            1 电脑 1999
            2 鼠标 10
            …
            n 购物车结算
    3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
    4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，
    若充值的钱数充足，则可以直接购买。
    6. 用户输入Q或者q退出程序。
    7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
'''

# goods = {
#     '1': {'name': '手机', 'price': 1999},
#     '2': {'name': '电脑', 'price': 8000},
#     '3': {'name': '背包', 'price': 200},
#     '4': {'name': '鼠标', 'price': 50}
# }
#
# my = {
#     'account': 0,  # 充值金额
#     'shopping_cart': {},  # 已购买物品列表
#     'deal_list': {}  # 成交列表
# }
#
# while True:
#     money = input('请给账户充值金额(整数):').strip()
#     if money.isdigit():
#         my['account'] = int(money)
#         break
#     else:
#         print('充值失败,请重新充值:')
#
# while True:
#     print('商品列表'.center(26, '*'))
#     for i in goods:
#         print(i, goods[i]['name'], goods[i]['price'])
#
#     x = input('请选择商品序号 N结算退出 Q退出:')
#     if x in goods:  # 在我的商品列表里面
#         count = my['shopping_cart'].setdefault(x, 0)
#         my['shopping_cart'][x] = count + 1  # {'商品编号': 商品数量}
#
#     elif x.upper() == 'Q':  # 退出
#         break
#
#     elif x.upper() == 'N':  # 结算退出
#         num = 0
#         for i in my['shopping_cart']:
#             num += goods[i]['price'] * my['shopping_cart'][i]  # 商品价格 * 购买的数量
#         if num > my['account']:  # 金额不足
#             for i in my['shopping_cart']:
#                 print(i, goods[i]['name'], goods[i]['price'], my['shopping_cart'][i])  # 商品名称 商品价格 商品数量
#             xx = input('结算失败,请删除部分商品:')
#             if xx in my['shopping_cart']:  # 删除商品
#                 my['shopping_cart'].pop(xx)
#
#         else:  # 金额足够
#             print('已购商品'.center(26, '*'))
#             print('商品加入购物车成功')
#             for i in my['shopping_cart']:
#                 print(goods[i]['name'], goods[i]['price'], my['shopping_cart'][i])  # 商品名称 商品价格 商品数量
#             my['account'] -= num  # 扣钱
#             print('本次消费金额%s, 余额%s' % (num, my['account']))
#             break
#     else:
#         print('没有此商品,请重新输入:')
