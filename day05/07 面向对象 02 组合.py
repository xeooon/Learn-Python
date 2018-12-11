# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 对象与对象之间是不能互相访问的,彼此独立
# 对象可以访问类中的所有内容,但是类名不能访问对象中的内容
# 组合的作用：让类的对象与另一个类的对象发生关联，从而可以互相访问。


# 如下代码完成了这个动作:  盖伦 利用大宝剑 攻击 狗头, 狗头还剩余210血量.
class Game_Role:  # 游戏类
    area = '召唤师峡谷'

    def __init__(self, name, sex, ad, hp):  # 人物基础信息方法
        self.name = name
        self.sex = sex
        self.ad = ad
        self.hp = hp

    def equit_weapon(self, wea):  # 装备类
        self.wea = wea  # 组合: 对象中的属性是另一个类的对象

class Weapon:  # 武器类
    def __init__(self, name, ad):  # 武器方法
        self.name = name
        self.ad = ad

    def wea_attack(self, role1, role2):  # 执行打架方法 self=对象本身 role1=p1盖伦 role2=p2狗头
        role2.hp = role2.hp - self.ad
        print('%s 利用%s 攻击 %s, %s还剩余%s血量.' % (role1.name, self.name, role2.name, role2.name, role2.hp))

p1 = Game_Role('盖伦', 'man', 30, 500)
p2 = Game_Role('狗头', '公', 50, 250)

sword = Weapon('大宝剑', 40)
p1.equit_weapon(sword)  # 此方法就是给p1对象封装一个属性,属性值是sword对象
p1.wea.wea_attack(p1, p2)  # 通过p1.wea找到sword,然后在sword.wea_attack执行方法



print('\033[33;1m学生%s帐号创建成功.\033[0m' % 1)