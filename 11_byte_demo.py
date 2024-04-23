#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# byte用于处理二进制数据，可以存储任何二进制数据，比如图片、视频、音频、压缩文件等。
# 字节数组bytearray和字节串bytes的区别在于，字节数组可以修改，而字节串不能修改。
# 字节存储的是整数，范围是0-255

# 定义一个字节数组
b = bytearray(b'hello world')

# 还可以更简化的定义
b = b'hello world'

# 打印字节数组
print(b)

# 也可以这样定义
b = bytes('你好世界', encoding = 'utf-8') #第一个参数是字节数组，第二个参数是编码方式

# 打印字节数组
print(b)

# 字节数组也可以用索引访问单个字节
print(b[0]) # 输出 b'h'


# 字节数组也可以用切片操作访问一部分字节
print(b[0:5]) # 输出 b'hello'

# 字节数组也可以用加法操作拼接字节数组
b2 = b' world'
b3 = b + b2