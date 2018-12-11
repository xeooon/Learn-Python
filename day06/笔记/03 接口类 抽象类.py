# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# __author__ = "Xeon"
# Email: Xeon@xeon.org.cn
""""""

# 接口类
# 统一支付方式: 归一化设计
# class QQpay:
#     def pay(self, money):
#         print('QQ支付了%s钱' % money)
#
# class Alipay:
#     def pay(self, money):
#         print('支付宝支付了%s钱' % money)
#
# def pay(obj, money):  # 归一化设计
#     obj.pay(money)
#
# a1 = QQpay()
# b1 = Alipay()
# pay(a1, 100)  # 返回 QQ支付了100钱
# pay(b1, 200)  # 返回 支付宝支付了200钱


# 接口类: 就是制定一个规则, 让其他人, 按照我的规则写代码, 约定俗成规范, 但是这个有人还不按这个执行
# class payment:
#     def pay(self, money):
#         pass
#
# class QQpay:
#     def pay(self, money):
#         print('QQ支付了%s钱' % money)
#
# class Alipay:
#     def pay(self, money):
#         print('支付宝支付了%s钱' % money)
#
# def pay(obj, money):  # 归一化设计
#     obj.pay(money)

# a1 = QQpay()
# b1 = Alipay()
# pay(a1, 100)  # 返回 QQ支付了100钱
# pay(b1, 200)  # 返回 支付宝支付了200钱



# 强制制定规范:
# from abc import ABCMeta, abstractmethod
# class payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self,money):
#          pass
# class QQpay(payment):
#     def pay(self, money):
#         print('QQ支付了%s钱' % money)
#
# class Alipay(payment):
#     def pay(self, money):
#         print('支付宝支付了%s钱' % money)
#
#
# class Wechat(payment):
#     def pay(self, money):
#         print('微信支付了%s钱' % money)
#
# def pay(obj, money):  # 归一化设计
#     obj.pay(money)
#
# w = Wechat()


