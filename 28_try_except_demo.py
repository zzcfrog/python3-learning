#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# try:
#     执行语句快
# except [XXXError as err]:
#     有异常 执行except语句块，相当于java的catch块，可以多个exception
# else:
#     无异常 执行else语句块
# finally:
#     无论是否有异常，都会执行finally语句块，一般用来释放资源，有的时候我们会使用with语句来自动释放资源，但有时候我们需要在finally块中做一些其他的操作，比如记录日志等。

try:
    a = 10 / 0
except ZeroDivisionError as err:
    print("Error:", err)
else:
    print("No error")
finally:
    print("Finally")

#用raise抛出异常，相当于java的throw语句


# 自定义异常，继承Exception
class MyError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
    def __str__(self):
        return f"MyError: {self.code=}, {self.message=}"
try:
    a = range(5)
    print(a[10])
except IndexError as err:
    print("raise Error:", err)
    raise MyError(100, err.__str__())
else:
    print("No error")
finally:
    print("Finally")