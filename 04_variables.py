#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python不需要声明变量类型，变量类型由值来决定

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "John"  # 字符串变量

print(counter)
print(miles)
print(name)

# 多变量赋值
a,b,c = 1, 2.0, "john"
a = b = c = 100

# python3 中有六个标准的数据类型：
# - 不可变 Number（数字）：int（只用这一种整数类型，没用long）、float、complex
# - 不可变 String（字符串）
# - 不可变 Tuple（元组）
# - 可变 List（列表）
# - 可变 Set（集合）
# - 可变 Dictionary（字典）
a = 100  # 整型变量
b = 3.14  # 浮点型变量
c = 1 + 2j  # 复数型变量
d = "hello"  # 字符串变量
e = True  # 布尔型变量

# 判断类型的函数
# type()不判断子类
# isinstance()判断子类
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>

class A: pass
class B(A): pass

print(isinstance(B(), A))  # True
print(isinstance(B(), B))  # True
print(isinstance(A(), B))  # False  
print(type(A()) == A)  # True
print(type(B()) == B)  # True
print(type(B()) == A)  # False

# Python中，bool是int的子类，所以True和False也是整型变量。
print(True == 1)  # True
print(False == 0)  # True

# del语句删除变量
del c, d, e
print(c)  # NameError: name 'c' is not defined
