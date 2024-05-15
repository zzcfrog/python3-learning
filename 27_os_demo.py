#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 获取当前路径
print(os.getcwd())

# 获取当前目录下的文件和目录
print(os.listdir())

# 获取当前目录下所有文件
print(os.listdir(os.getcwd()))

# 获取当前目录下所有目录
print(os.listdir(os.getcwd()))

# 创建目录
os.mkdir("test")

# 删除目录
os.rmdir("test")

# 重命名文件或目录
os.rename("test.txt", "test.py")

# 移动文件或目录
os.rename("test.py", "test")

# 获取文件大小
print(os.path.getsize("test.py"))

# 获取文件修改时间
print(os.path.getmtime("test.py"))

# 获取文件创建时间
print(os.path.getctime("test.py"))

# 判断文件是否存在
print(os.path.exists("test.py"))

# 判断是否为文件
print(os.path.isfile("test.py"))

# 判断是否为目录
print(os.path.isdir("test"))