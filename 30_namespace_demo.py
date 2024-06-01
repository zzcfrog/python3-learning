#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 命名空间：# 命名空间的层次结构
# 命名空间的层次结构是指命名空间的嵌套结构。
# 命名空间的层次结构可以帮助我们更好地组织代码，并避免命名冲突。
# 命名空间是一组变量、函数和其他名称的集合，这些名称在程序执行期间可以被访问和使用。
# 命名空间的作用是避免名称冲突，并提供一种结构化的方式来组织代码。
# 命名空间的实现方式有两种：
# 1. 字典：Python使用字典来实现命名空间。
# 2. 作用域：Python使用作用域来实现命名空间。

# 字典实现命名空间
# 字典是一种可变的容器，可以存储任意类型的值。
# 字典的键必须是唯一的，值可以是任意类型。
# 字典的实现方式是：
# 1. 内置字典：包含所有的内置名称。
# 2. 全局字典：包含所有的全局名称。
# 3. 局部字典：包含所有的局部名称。

# 作用域实现命名空间
# 作用域是一套规则，用于确定变量的作用范围。
# 作用域的实现方式是：
# 1. 内置作用域：包含所有的内置名称。
# 2. 全局作用域：包含所有的全局名称。
# 3. 局部作用域：包含所有的局部名称。

# python的查找顺序：局部的命名空间 -> 全局命名空间 -> 内置命名空间

a = 1
def dontAfffectGlobal():
    a = 2 # 如果不声明global，可以直接赋值，但不影响全局变量
    a = a * 2
    print(a)

dontAfffectGlobal()
print(a) # 如果在局部作用域中不加global，不影响全局变量

def affectGlobal():
    global a
    a = 3 # 如果声明global，可以直接赋值，会影响全局变量
    a = a * 2
    print(a)

affectGlobal()
print(a) # 如果在局部作用域中加global，会影响全局变量

#
a = 1
def nonLocalScope():
    a = 2
    def inner():
        nonlocal a
        a = 3
        print(a) # 输出2
    inner()
    print(a) # 输出3
        

nonLocalScope()
print(a) # 输出1