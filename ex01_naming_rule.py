#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 变量命名最佳实践
# 1. 见名思意，变量名应该能够准确反映变量的含义。
# 2. 变量名应该简短，尽量避免使用拼音、缩写、数字等无意义的字符。
# 3. 变量名应该有意义，不要使用无意义的单词。
# 4. 变量名应该避免使用与关键字、系统保留字冲突的名称。
# 5. 变量名应该使用_连接多个单词。
# 6. 常量名全部使用大写字母，单词间用下划线分隔。

# 实例
# 变量名
age = 25
name = "John Doe"
is_active = True
# 常量名：
MAX_AGE = 120

# 函数命名最佳实践
# 1. 函数名应该能够准确反映函数的功能。
# 2. 函数名应该简短，尽量避免使用拼音、缩写、数字等无意义的字符。
# 3. 函数名应该有意义，不要使用无意义的单词。
# 4. 函数名应该避免使用与关键字、系统保留字冲突的名称。
# 5. 函数名应该使用_连接多个单词。

def calc_sum(a,b):
    return a+b

# 类命名最佳实践
# 1. 类名应该能够准确反映类的功能。
# 2. 类名应该简短，尽量避免使用拼音、缩写、数字等无意义的字符。 
# 3. 类名应该有意义，不要使用无意义的单词。
# 4. 类名应该避免使用与关键字、系统保留字冲突的名称。
# 5. 类名应该使用驼峰命名法。

class MyClass:
    pass

# 模块命名最佳实践
# 1. 模块名应该能够准确反映模块的功能。
# 2. 模块名应该简短，尽量避免使用拼音、缩写、数字等无意义的字符。
# 3. 模块名应该有意义，不要使用无意义的单词。
# 4. 模块名应该避免使用与关键字、系统保留字冲突的名称。
# 5. 模块名应该使用小写字母，单词间用下划线分隔。

import my_module

# 函数装饰器命名最佳实践
# 1. 装饰器名应该能够准确反映装饰器的功能。
# 2. 装饰器名应该简短，尽量避免使用拼音、缩写、数字等无意义的字符。
# 3. 装饰器名应该有意义，不要使用无意义的单词。
# 4. 装饰器名应该避免使用与关键字、系统保留字冲突的名称。
# 5. 装饰器名应该使用下划线连接多个单词。


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # do something
        return func(*args, **kwargs)
    return wrapper

# 类方法装饰器命名最佳实践
# 1. 装饰器名应该能够准确反映装饰器的功能。
# 2. 装饰器名应该简短，尽量避免使用拼音、缩写、数字等无意义的字符。
# 3. 装饰器名应该有意义，不要使用无意义的单词。
# 4. 装饰器名应该避免使用与关键字、系统保留字冲突的名称。
# 5. 装饰器名应该使用下划线连接多个单词。


class MyClass2:
    def my_decorator(cls, func):
        def wrapper(*args, **kwargs):
            # do something
            return func(*args, **kwargs)
        return wrapper
    
# 类装饰器命名最佳实践
# 1. 装饰器名应该能够准确反映装饰器的功能。
# 2. 装饰器名应该简短，尽量避免使用拼音、缩写、数字等无意义的字符。          
# 3. 装饰器名应该有意义，不要使用无意义的单词。
# 4. 装饰器名应该避免使用与关键字、系统保留字冲突的名称。
# 5. 装饰器名应该使用驼峰命名法。

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # do something
        return self.func(*args, **kwargs)    

