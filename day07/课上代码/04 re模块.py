# re模块
# 正则表达式

# 按照你的一定规则去操作字符串得到你想要的结果。

import re
# \w	匹配字母（包含中文）或数字或下划线
# \W	匹配非字母（包含中文）或数字或下划线
# print(re.findall('\w\w','太白alex  123 _ *'))
# print(re.findall('\W','太白alex  123 _ *'))

# \s	匹配任意的空白符
# \S	匹配任意非空白符
# print(re.findall('\s','太白  123*\t\n'))  # [' ', ' ', '\t', '\n']
# print(re.findall('\S','太白  123*\t\n'))  # ['太', '白', '1', '2', '3', '*']

# \d	匹配数字
# \D	匹配非数字
# print(re.findall('\d','太白  123*')) # ['1', '2', '3']
# print(re.findall('\D','太白  123*')) # ['太', '白', ' ', ' ', '*']

# \A	从字符串开头匹配  # 只匹配开头  相当于startswith
# ^	匹配字符串的开始  只匹配开头  相当于startswith
# print(re.findall(r'\A太白','** 太白 太白 123*'))
# print(re.findall(r'^太白','太白 太白 123*'))

# \z	匹配字符串的结束，如果是换行，只匹配到换行前的结果
# \Z	匹配字符串的结束
# print(re.findall('太白\z','** 太白 太白'))
# print(re.findall('666\Z','hello 太白金星 *-_-* \n666'))  # ['666']
# print(re.findall('666\z','hello 太白金星 *-_-* \n666'))  # []

# \n	匹配一个换行符
# \t	匹配一个制表符
# print(re.findall('\n','** 太白 太白 \n123'))  # ['\n']
# print(re.findall('\t','** 太白 太白 \n123\t\t'))  # ['\t', '\t']

# $ 匹配一个字符串的结尾
# print(re.findall('123$','** 太白 太白 123 '))



# 重复匹配

# . ? * + {m,n} .* .*?

# . 任意字符   re.DOTALL 可以匹配换行符
# print(re.findall('a.b', 'ab aab abb a*b a6b a b aaaab'))
# print(re.findall('a.b', 'ab aab abb a*b a6b a3b a\nb',re.DOTALL))

# ? 匹配0个或者1个由左边字符定义的片段。 贪婪匹配
# print(re.findall('a?b', 'aab'))  # ['ab']
# print(re.findall('a?b', 'ab aab abb a*b'))  # ['ab', 'ab', 'ab', 'b', 'b']

# *匹配0个或者多个左边字符表达式。 满足贪婪匹配 @@
# print(re.findall('a*b', 'ab aab aaaaaaaaaab abbb'))

# + 匹配1个或者多个左边字符。 满足贪婪匹配
# print(re.findall('a+b', 'ab aab aaab abbb'))


# {m,n}  匹配m个至n个左边字符表达式。 满足贪婪匹配  @@
# print(re.findall('a{2,4}b', 'ab aab aaaab abbb'))


# 纯贪模式 .* 一般不用
# print(re.findall('a.*b', 'ea*b ab aab aaaaaaaaaab abbb'))  、
#  ['a*b ab aab aaaaaaaaaab abbb']

# 贪婪模式 .*?   .* 纯贪  ? 作为限制 满足我就取出
# .*? 常用模式
# print(re.findall('a.*?b', 'a*b ab aab aaaaaaaaaab abbb'))
# ['a*b', 'ab', 'aab', 'aaaaaaaaaab', 'ab']


# [] 代表一个字符  # erw 任意选一个
# print(re.findall('a[erw][erw]b', 'ab aab aeb arb arwb arewb'))
# str1 = 'a1b a2b a3b aab aeb a9b'
# str2 = 'a1b aTb a3b aAb aeb a_b ayb'
# str3 = 'a1b aTb a3b a-b a%b a!b a&b'
# print(re.findall('a[0-9]b',str1))  # ['a1b', 'a2b', 'a3b', 'a9b']
# print(re.findall('a[a-z]b',str2))  # ['aab', 'aeb', 'ayb']
# print(re.findall('a[a-z,A-Z]b', str2))
# print(re.findall('a[-!&]b', str3))  # [] 想匹配- 一定要放到最前面
# print(re.findall('a[^0-9]b', str3))  # ^ 中括号代表取反

# 练习：'alex_sb ale123_sb wu12sir_sb wusir_sb ritian_sb'


# 分组 () 制造了一个模板(.*?)_sb
# print(re.findall('(.*?)_sb', 'alex_sb wusir_sb 日天_sb'))

# print(re.findall('http.*?com','<a href="http://www.baidu.com">点击</a><a href="http://www.baidu2.com">登录</a>'))

# print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>'))

# | 左边右边都可以

# print(re.findall('alex|太白|wusir', 'alex太白wusiraleeeex太太白odlb'))  # ['alex', '太白', 'wusir', '太白']

# print(re.findall('compan(ies|y)','Too many companies have gone bankrupt, and the next one is my company'))  # ['ies', 'y']
# 但是我想将 companies  company ?: 对分组进行一个应用，全部都取出来
# print(re.findall('compan(?:ies|y)','Too many companies have gone bankrupt, and the next one is my company'))

# re模块的操作方法
# findall 找到全部
# print(re.findall('a.b', 'abaabb'))

# search 相当于 in

# print(re.search('sb|alex', 'alex sb sb barry 日天'))  # <_sre.SRE_Match object; span=(0, 4), match='alex'>
# print(re.search('aaa', 'alex sb sb barry 日天'))  # <_sre.SRE_Match object; span=(0, 4), match='alex'>
# print(re.search('sb|alex', ' 666 sb alex sb barry 日天').group())
# '''1 + 2*(3/5) + 2**3 - (2/3 + 3*(4-2))'''

# match 匹配的就是开始
# print(re.match('aaa', 'aaa sb sb barry 日天'))  # <_sre.SRE_Match object; span=(0, 3), match='aaa'>
# print(re.match('aaa', 'aa sb sb barry 日天'))  # None
# print(re.findall('^aaa', 'aa sb sb barry 日天'))  # []

# split  ***
# s1 = 'alex wusir 日天 太白'
# s1 = 'alex wusir,日天;太白|二狗'
# # print(s1.split())
# # 对字符串按照不同分隔符进行分割
# print(re.split(' |,|;|\|',s1))
# print(re.sub('barry', '太白', 'barry是最好的讲师，barry就是一个普通老师，请不要将barry当男神对待。'))
# print(re.sub('(alex)( )(is)( )(sb)', r'\5\2\3\4\1', r'alex is sb'))
# 将字符串的第一个与最后一个单词！互换位置
# print(re.sub('([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)', r'\5\2\3\4\1', r'alex     is 1232 sb'))

# print(re.findall('[a-zA-Z]+', 'alex1wusir3 12321'))

# obj = re.compile('\d{2}')
#
# print(obj.search('abc123eeee').group())
# print(obj.findall('abc123eeee'))

# ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
# print(ret)  # <callable_iterator object at 0x10195f940>
# print(next(ret).group())  #查看第一个结果
# print(next(ret).group())  #查看第二个结果
# print([i.group() for i in ret])  #查看剩余的左右结果







# 1，"1-2*(60+(-40.35/5)-(-4*3))"
s1 = "1-2*(60+(-40.35/5)-(-4*3))"
    
    # 1.1 匹配所有的整数  (pass)
    
# print(re.findall('\d+',s1))
# print(re.findall('\d+(?:\.?\d+)?',s1))

    # 1.2 匹配所有的数字（包含小数）
    # 60 0.1232434354
# print(re.findall('\d+\.?\d*', s1))


    # 1.3 匹配所有的数字 ['1', '-2', '60', '-40.35', '5', '-4', '3']
# print(re.findall('-?\d+\.?\d*', s1))

s1 = '''
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7459977.html" target="_blank">python基础一</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7562422.html" target="_blank">python基础二</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/9439483.html" target="_blank">Python最详细，最深入的代码块小数据池剖析</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7738630.html" target="_blank">python集合,深浅copy</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8183203.html" target="_blank">python文件操作</a></p>
<h4 style="background-color: #f08080;">python函数部分</h4>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8241942.html" target="_blank">python函数初识</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8259929.html" target="_blank">python函数进阶</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8305011.html" target="_blank">python装饰器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423526.html" target="_blank">python迭代器,生成器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423937.html" target="_blank">python内置函数,匿名函数</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8743408.html" target="_blank">python递归函数</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/8743595.html" target="_blank">python二分查找算法</a></p>

'''
# 1,找到所有的p标签
print(re.findall('<p>.*?</p>', s1))
