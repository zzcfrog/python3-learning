#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器相当于java中的注解，可以给函数增加额外的功能，比如记录日志、性能测试、事务处理等。
# 装饰器本质是函数，可以理解为java中的aop的实现。
# 但它比java中的annotation实现更加简洁，而且可以应用到类、方法、函数上。

# 定义一个装饰器，它可以打印函数的执行时间
# 外层函数定义装饰器，内层函数定义被装饰的函数
import time
def timer(func):
    def origin_func(*args, **kwargs):
        start_time = time.time()
        print(f"{start_time=}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{result=}")
        print(f"{end_time - start_time=}")
        return result
    return origin_func

@timer
def sum(a, b):
    return a + b

sum(1, 2)

# 装饰器是可以带参数的
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
            return
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("world")

# 类装饰器
class Printer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with {args} and {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"{result=}")
        return result

@Printer
def add(a, b):
    return a + b

add(1, 2)