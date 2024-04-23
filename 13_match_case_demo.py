#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
都说_相当于java中的case default, 但实际上比defalut强大很多，可以匹配任意值，也可以忽略某些部分的匹配。他可以用在模式内的任何位置，包括函数参数、列表、字典、元组等。
比如:
case (1, _, 3)
case [1, _, 3]
case {1, _, 3}
case {'name': _, 'age': _}
'''

def print_number(value):
    match value:
        case 0:
            print("zero")
        case 1:
            print("one")
        case 2:
            print("two")
        case 3:
            print("three")
        case 4:
            print("four")
        case _:
            print("something else")

print_number(4)

# match-case是基于模式的匹配，可以匹配多种情况，并执行相应的语句。包含以下6种情况：
# 1. 匹配不同类型的常量值，如整数、浮点数、字符串等。
def check_constant(value):
    match value:
        case 0:
            print("匹配整数 0")
        case 3.14:
            print("匹配浮点数 3.14")
        case 'apple':
            print("匹配字符串 'apple'")
        case _:
            print("未匹配到任何模式")

check_constant(0)       # 输出：匹配整数 0
check_constant(3.14)    # 输出：匹配浮点数 3.14
check_constant('apple') # 输出：匹配字符串 'apple'
check_constant(True)    # 输出：未匹配到任何模式

# 2. 匹配特定结构的容器类型，如列表、字典、元组等。
def check_container(container):
    match container:
        case [1, 2, 3]:
            print("匹配列表 [1, 2, 3]")
        case {'name': 'John', 'age': 30}:
            print("匹配字典 {'name': 'John', 'age': 30}")
        case (x, y):
            print(f"匹配元组 ({x}, {y})")
        case _:
            print("未匹配到任何模式")

check_container([1, 2, 3])                          # 输出：匹配列表 [1, 2, 3]
check_container({'name': 'John', 'age': 30})        # 输出：匹配字典 {'name': 'John', 'age': 30}
check_container(('apple', 'banana'))                # 输出：匹配元组 ('apple', 'banana')
check_container([4, 5, 6])                          # 输出：未匹配到任何模式

# 3. 匹配自定义的数据类型，可以根据自定义类的属性进行匹配。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def check_custom_type(obj):
    match obj:
        case Person('Alice', 25):
            print("匹配 Person 对象，姓名为 Alice，年龄为 25")
        case Person(name='Bob', age=30):
            print("匹配 Person 对象，姓名为 Bob，年龄为 30")
        case _:
            print("未匹配到任何模式")

person1 = Person('Alice', 25)
person2 = Person('Bob', 30)
person3 = Person('Charlie', 35)

check_custom_type(person1)    # 输出：匹配 Person 对象，姓名为 Alice，年龄为 25
check_custom_type(person2)    # 输出：匹配 Person 对象，姓名为 Bob，年龄为 30
check_custom_type(person3)    # 输出：未匹配到任何模式

# 4. 匹配复杂的模式结构，如嵌套的容器、多层级的数据结构等。
def check_nested_structure(data):
    match data:
        case [1, [2, 3], 4]:
            print("匹配嵌套列表 [1, [2, 3], 4]")
        case {'name': 'John', 'info': {'age': 30, 'city': 'New York'}}:
            print("匹配嵌套字典 {'name': 'John', 'info': {'age': 30, 'city': 'New York'}}")
        case _:
            print("未匹配到任何模式")

check_nested_structure([1, [2, 3], 4])                                     # 输出：匹配嵌套列表 [1, [2, 3], 4]
check_nested_structure({'name': 'John', 'info': {'age': 30, 'city': 'NY'}}) # 输出：匹配嵌套字典 {'name': 'John', 'info': {'age': 30, 'city': 'New York'}}
check_nested_structure([1, 2, 3])                                          # 输出：未匹配到任何模式

# 5. 提取匹配模式中的变量值，进行后续的操作和处理。
def extract_variables(data):
    match data:
        case (x, y):
            print(f"匹配元组 ({x}, {y})")
            print(f"x 的值为 {x}")
            print(f"y 的值为 {y}")
        case _:
            print("未匹配到任何模式")

extract_variables((10, 20))    # 输出：
# 匹配元组 (10, 20)
# x 的值为 10
# y 的值为 20

extract_variables(('apple', 'banana'))    # 输出：
# 匹配元组 ('apple', 'banana')
# x 的值为 apple
# y 的值为 banana

extract_variables([1, 2, 3])    # 输出：未匹配到任何模式

# 6. 使用通配符 _ 匹配任意值或忽略某些部分的匹配。
def ignore_pattern(data):
    match data:
        case [1, _, 3]:
            print("匹配列表 [1, _, 3]，其中 _ 表示任意值")
        case {'name': _, 'age': _}:
            print("匹配字典 {'name': _, 'age': _}，其中 _ 表示任意值")
        case _:
            print("未匹配到任何模式")

ignore_pattern([1, 2, 3])                                      # 输出：匹配列表 [1, _, 3]，其中 _ 表示任意值
ignore_pattern({'name': 'John', 'age': 30, 'city': 'New York'}) # 输出：匹配字典 {'name': _, 'age': _}，其中 _ 表示任意值
ignore_pattern('apple')                                        # 输出：未匹配到任何模式

