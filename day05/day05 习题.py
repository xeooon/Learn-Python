# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""
"""
标题 : 24期周末班 - day05 - 习题
作者 : 张志强
QQ号 : 1344683865
微信 : qingniaoxiaoqiang
邮箱 : Xeon@xeon.org.cn
"""


# ###################################### 练习题1 #######################################


'''
1,完成下列功能:
  1.1创建一个人类Person,再类中创建3个静态变量(静态字段)
    animal = '高级动物'
    soul = '有灵魂'
    language = '语言'
  1.2在类中定义三个方法,吃饭,睡觉,工作.
  1.3在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄, 身高.
  1.4实例化四个人类对象:
    第一个人类对象p1属性为:中国,alex,未知,42,175.
    第二个人类对象p2属性为:美国,武大,男,35,160.
    第三个人类对象p3属性为:你自己定义.
    第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3的身高.
  1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
  1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
  1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
  1.8 通过p1对象找到Person的静态变量 animal
  1.9 通过p2对象找到Person的静态变量 soul
  2.0 通过p3对象找到Person的静态变量 language
'''
# class Person1:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def life(self):
#         eat = '吃饭'
#         sleep = '睡觉'
#         work = '工作'
#         print('%s在%s' % (self.name, eat))
#
#     def __init__(self, country, name, sex, age, hight):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.hight = hight
#
# p1 = Person1('中国', 'alex', '未知', 42, 175)
# p2 = Person1('美国', '武大', '男', 35, 160)
# p3 = Person1('中国', 'xeon', '男', 23, 183)
# p4 = Person1(p1.country, p2.name, p3.sex, p2.age, p3.hight)
#
# Person1.life(p1)
# Person1.life(p2)
# Person1.life(p3)
#
# print(p1.animal)
# print(p2.soul)
# print(p3.language)


'''
2,通过自己创建类,实例化对象
  在终端输出如下信息
  小明，10岁，男，上山去砍柴
  小明，10岁，男，开车去东北
  小明，10岁，男，最爱大保健
  老李，90岁，男，上山去砍柴
  老李，90岁，男，开车去东北
  老李，90岁，男，最爱大保健
  老张…
'''
# class Person2:
#     def __init__(self, name, age, sex, hobby):
#         print(name, age, sex, hobby)
#
# p1 = Person2('小名', 10, '男', '上山去砍柴')
# p2 = Person2('老李', 90, '男', '上山去砍柴')


'''
3,模拟英雄联盟写一个游戏人物的类（升级题）.
  要求:
  (1)创建一个 Game_role的类.
  (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
  (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
      例: 实例化一个对象 盖伦,ad为10, hp为100
      实例化另个一个对象 剑豪 ad为20, hp为80
      盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.
'''
# class Game_role:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self, role):
#         role.hp -= self.ad  # 被打者hp = 被打者hp - 攻击者ad
#         print('%s攻击%s, %s掉了%s血, 还剩%s血.' % (self.name, role.name, role.name, self.ad, role.hp))
#
# p1 = Game_role('盖伦', 10, 100)
# p2 = Game_role('剑豪', 20, 80)
#
# p1.attack(p2)


'''
4,默写内容:
  创建一个人类,定义三个静态变量,在构造方法中封装3个属性.然后实例化一个对象,
  对象调用自己的属性,对象调用类的静态方法,对象调用类中的方法.
  默写一下实例化一个对象，具体经历了哪些阶段。
'''
# class Person4:
#     mind = '有思想'
#     animal = '高级动物'
#     language = '文字语言'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# p1 = Person4('王二麻子', 22, '男')
#
# print(p1.__dict__)  # 对象调用自己的属性
# print(p1.mind)  # 对象调用类的静态方法
# print(p1.name)  # 对象调用类中的方法


# ###################################### 练习题2 #######################################


'''
1，暴力摩托程序（完成下列需求）：
1.1创建三个游戏人物，分别是：
•	苍井井，女，18，攻击力ad为20，血量200
•	东尼木木，男，20，攻击力ad为30，血量150
•	波多多，女，19，攻击力ad为50，血量80

1.2创建三个游戏武器，分别是：
•	平底锅，ad为20
•	斧子，ad为50
•	双节棍，ad为65

1.3 创建三个游戏摩托车，分别是：
•	小踏板，速度60迈
•	雅马哈，速度80迈
•	宝马，速度120迈。
完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：
（1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
（2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
（3）波多多骑着雅马哈开着80迈的车行驶在赛道上。
（4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
（5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。
（6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
（7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。
（8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。（选做）
（9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。（选做）
'''
# class Game_Role:  # 游戏属性类
#     def __init__(self, name, sex, age, ad, hp):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.ad = ad
#         self.hp = hp
#
#     def tool(self, too):  # 封装打人及开车的动态属性
#         self.too = too
#
#     def attack(self, role):  # 赤手空拳动态属性
#         role.hp = role.hp - self.ad  # 被打者hp = 被打者hp - 攻击者的ad
#         print('%s赤手空拳打了%s%s血, %s还剩%s血.' % (self.name, role.name, self.ad, role.name, role.hp))
#
# class Weapon:  # 武器类
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#     def too_fight(self, role1, role2):  # 谁用工具打人的动态属性
#         self.role1 = role1
#         self.role2 = role2
#         role2.hp = role2.hp - (role1.ad + self.ad)  # 被打者hp = 被打者hp - (攻击者的ad + 攻击者的工具ad)
#         print('%s利用%s打了%s一%s, %s还剩%s血.' % (role1.name, self.name, role2.name, self.name, role2.name, role2.hp))
#
# class Vehicle:  # 交通工具类
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def too_driver(self, role):  # 谁开车的动态属性
#         print('%s骑着%s, 开着%s迈的车行驶在赛道上.' % (role.name, self.name, self.speed))
#
# g1 = Game_Role('苍井井', '女', 18, 20, 200)  # 苍井井，女，18，攻击力ad为20，血量200
# g2 = Game_Role('东尼木木', '男', 20, 30, 150)  # 东尼木木，男，20，攻击力ad为30，血量150
# g3 = Game_Role('波多多', '女', 19, 50, 80)  # 波多多，女，19，攻击力ad为50，血量80
#
# w1 = Weapon('平底锅', 20)  # 平底锅，ad为20
# w2 = Weapon('斧子', 50)  # 斧子，ad为50
# w3 = Weapon('双节棍', 65)  # 双节棍，ad为65
#
# v1 = Vehicle('小踏板', 60)  # 小踏板，速度60迈
# v2 = Vehicle('雅马哈', 80)  # 雅马哈，速度80迈
# v3 = Vehicle('宝马', 120)  # 宝马，速度120迈
#
# g1.tool(v1)
# g1.too.too_driver(g1)  # 苍井井骑着小踏板, 开着60迈的车行驶在赛道上.
#
# g2.tool(v3)
# g2.too.too_driver(g2)  # 东尼木木骑着宝马, 开着120迈的车行驶在赛道上.
#
# g3.tool(v2)
# g3.too.too_driver(g3)  # 波多多骑着雅马哈, 开着80迈的车行驶在赛道上.
#
# g1.attack(g3)  # 苍井井赤手空拳打了波多多20血, 波多多还剩60血.
# g2.attack(g3)  # 东尼木木赤手空拳打了波多多30血, 波多多还剩30血.
#
# g3.tool(w1)
# g3.too.too_fight(g3, g1)  # 波多多利用平底锅打了苍井井一平底锅, 苍井井还剩130血
#
# g3.tool(w2)
# g3.too.too_fight(g3, g2)  # 波多多利用斧子打了东尼木木一斧子, 东尼木木还剩50血


'''
2，定义一个类，计算圆的周长和面积。
'''
# from math import pi
# class Circle:  # 定义园形类
#     def __init__(self, radius):  # 半径方法
#         self.radius = radius
#
#     def area(self):  # 面积方法
#          return pi * self.radius * self.radius
#
#     def perimeter(self):  # 周长方法
#         return 2 * pi *self.radius
#
# circle = Circle(4)  # 实例化一个圆
# area1 = circle.area()  # 计算圆面积
# per1 = circle.perimeter()  # 计算圆周长
# print('周长为%s, 面积为%s, ' % (per1, area1))  # 打印圆周长和面积

'''
3，定义一个圆环类，计算圆环的周长和面积（升级题）。
'''
# 圆环是由两个圆组成的，圆环的面积是外面圆的面积减去内部圆的面积。圆环的周长是内部圆的周长加上外部圆的周长。
# 这个时候，我们就首先实现一个圆形类，计算一个圆的周长和面积。然后在"环形类"中组合圆形的实例作为自己的属性来用
# from math import pi
# class Circle:
#     '''
#     定义了一个圆形类；
#     提供计算面积(area)和周长(perimeter)的方法
#     '''
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#          return pi * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * pi *self.radius
#
# class Ring:
#     '''
#     定义了一个圆环类
#     提供圆环的面积和周长的方法
#     '''
#     def __init__(self,radius_outside, radius_inside):
#         self.outsid_circle = Circle(radius_outside)
#         self.inside_circle = Circle(radius_inside)
#
#     def area(self):
#         return self.outsid_circle.area() - self.inside_circle.area()
#
#     def perimeter(self):
#         return self.outsid_circle.perimeter() + self.inside_circle.perimeter()
#
# ring = Ring(8, 4)  # 实例化一个环形
# print(ring.perimeter())  # 计算环形的周长
# print(ring.area())  # 计算环形的面积


'''
4，默写内容:
  创建两个类，让一个类的对象的属性为另一个类的对象。
'''
# 方法1:
# class Buy_Role:
#     def __init__(self, name):
#         self.name = name
#
#     def buy(self, role):
#         self.role = role
#
# class Buy_Who:
#     def __init__(self, shopname, colour):
#         self.shopname = shopname
#         self.colour = colour
#
#     def role_taobao(self, role1):
#         self.role1 = role1
#         print('%s购买了一款%s的%s' % (role1.name, self.colour, self.shopname))
#
# a1 = Buy_Role('xeon')
# b1 = Buy_Who('MacBookPro', '灰色')
#
# a1.buy(b1)
# a1.role.role_taobao(a1)

# 方法2:
# class Ren:
#     '''人类'''
#     def __init__(self, shengri):
#         self.shengri = shengri
#
# class Riqi:
#     '''日期类'''
#     def __init__(self, nian, yue, ri):
#         self.nian = nian
#         self.yue = yue
#         self.ri = ri
#
# riqi = Riqi(2000,10,10)
# ren = Ren(riqi)
# print(ren.shengri.nian)
# print(ren.shengri.yue)
# print(ren.shengri.ri)


# ###################################### 练习题3 #######################################


'''
一，简答题
1，面向对象的三大特性是什么？
'''
# 继承: 面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容。
# 多态: Pyhon不支持Java和C#这一类强类型语言中多态的写法，但是原生多态，其Python崇尚"鸭子类型"。
# 封装: 面向对象中的内容封装到某个地方，以后再去调用被封装在某处的内容


'''
2，什么是面向对象的新式类？什么是经典类？
'''
# 经典类: 不继承object的类
#     ython2.x:经典类 和新式类(object) 共存
#
# 新式类(查询效率高)
#     python3.x 默认继承object,全部是新式类


'''
3，面向对象为什么要有继承？继承的好处是什么？
'''
# 1.节省代码 2.提高效率 3.让类之间产生关联


'''
4，面向对象中super的作用。
'''
# 自动将self传给父类的self,self是对象本身


'''
二，代码题(通过具体代码完成下列要求)：
1，
a,定义一个父类Animal，在构造方法中封装三个属性，姓名，性别，年龄，
  再给其添加一个eat的方法，方法中显示%s正在吃饭（%s是哪个对象调用此方法，显示哪个对象名字）。
b,定义两个基类Person,Dog，全部继承这个父类Animal.
c,Person类中，有构造方法，封装一个皮肤的属性，有eat方法，方法中显示人类正在吃饭。
d,Dog类中，有构造方法，封装一个毛色的属性，有eat方法，方法中显示狗狗正在吃饭。
上面这几个类创建完成之后，完成下列要求：
①：	实例化一个人类的对象，让其只封装皮肤属性。
②： 实例化一个人类的对象，让其封装姓名，性别，年龄，皮肤四个属性。
③： 实例化一个狗类的对象，让其只封装毛色属性。
④： 实例化一个狗类的对象，让其封装姓名，性别，年龄，毛色四个属性。
⑤： 实例化一个人类的对象，让其只执行父类的eat方法（可以对人类代码进行修改）。
⑥： 实例化一个狗类的对象，让其既执行父类的eat方法，又执行子类的eat方法。
'''
# class Animal:  # 父类Animal
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):  # eat方法
#         print('%s正在吃饭' % self.name)
#
# class Person(Animal):  # 基类Person
#     # 子类调用父类的方法, 父类中的self是子类的实例
#     def __init__(self, skin, name, age, sex):
#         self.skin = skin
#         super(Person, self).__init__(name, age, sex)
#
# class Dog(Animal):  # 基类Dog
#
#     def __init__(self, color, name, age, sex):
#         self.color = color
#
#         super(Dog, self).__init__(name, age, sex)
#
#     def eat(self):
#         super().eat()
#         print('汪汪汪')


# p1 = Person('黄色', '张三', '男', 10)
# p1.eat()

# d1 = Dog('长毛', '旺财', '公', 3)
# d1.eat()


'''
2，
class A:
    def func(self):
        print('in A')

class B:
    def func(self):
        print('in B')

class C(A,B):
    def func(self):
        print('in C')
可以改动上上面代码，完成下列需求：
对C类实例化一个对象产生一个c1，然后c1.func()
1, 让其执行C类中的func
2，让其执行A类中的func
3，让其执行B类中的func
4，让其既执行C类中的func，又执行A类中的func
5，让其既执行C类中的func，又执行B类中的func
'''
# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A, B):
#     def func(self):
#         print('in C')
#         super(C, self).func()
#
# print('# 既执行C类中的func，又执行A类中的func')
# c1 = C()
# c1.func()
#
# print('\n# 执行A类中的func')
# c2 = A()
# c2.func()
#
# print('\n# 执行B类中的func')
# c3 = B()
# c3.func()
#
# # print('\n# 执行C类中的func，又执行B类中的func')
# # c5 = C()
# # c5.func()


'''
3，下面代码执行结果是什么？为什么？
class Parent:
    def func(self):
        print('in Parent func')

    def __init__(self):
        self.func()

class Son(Parent):
    def func(self):
        print('in Son func')

son1 = Son()
'''
# class Parent:  # 类
#     def func(self):  # 动态属性
#         print('in Parent func')
#
#     def __init__(self):  # 动态属性
#         self.func()
#
# class Son(Parent):  # 类
#     def func(self):  # 动态属性
#         print('in Son func')
#
# son1 = Son()  # 结果为in Son func, 因为通过类执行了动态属性


'''
4，
class A:
    name = []

p1 = A()
p2 = A()
p1.name.append(1)
p1.name，p2.name，A.name 分别是什么？
p1.age = 12
p1.age，p2.age，A.age 分别又是什么？为什么？
'''
# class A:
#     name = []
#
# p1 = A()
# p2 = A()
# p1.name.append(1)
# # print(p1.name)  # p1.name是 [1], 因为是一个内存地址
# # print(p2.name)  # p2.name是 [1], 因为是一个内存地址
#
# p1.age = 12
# # print(p1.age)  # p1.age是12, 因为赋值了
# # print(p2.age)  # p2.age报错, 因为没有p2.age这个
