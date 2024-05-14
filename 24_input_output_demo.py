#！/usr/bin/env python3
# -*- coding: utf-8 -*-

s = "hello  world"
print(s)
print(str(s))
print(repr(s))

# :格式化占位填充
a = 1
b = 10
c = 100
print("{}".format(a)) 
print("{0:4d}".format(b)) #也可写成"{:4d}"表示第一个参数  4d表示占位符的宽度为4，
print("{0:0>4d}".format(c)) #:0>4d表示占位符的宽度为4，冒号后的0表示用0填充，>表示右对齐，4d表示占位符的宽度为4
print("{0:0<4d}".format(c)) #:0<4d表示占位符的宽度为4，冒号后的0表示用0填充，<表示左对齐，4d表示占位符的宽度为4
print("{0:^4d}".format(b))  #:0^4d表示占位符的宽度为4，冒号后的0表示用0填充，^表示居中对齐，4d表示占位符的宽度为4

# 多个值填充
print("冒号格式化:{0:4d}|{1:4d}|{2:4d}".format(a, b, c))
#多个值使用[]访问
s = [a, b, c]
print("字符串数组格式化:{0[0]:4d}|{0[1]:4d}|{0[2]:4d}".format(s))

#rjust()多个值右对齐
print("str.rjust()格式化:", end='')
print(str(a).rjust(4), str(b).rjust(4), str(c).rjust(4), sep='|')

#zfill()多个值左补0
print("str.rjust()格式化:",str(a).zfill(4), str(b).zfill(4), str(c).zfill(4), sep='|')

#读入
str = input("请输入字符串:")
print("输入的字符串是:", str)

