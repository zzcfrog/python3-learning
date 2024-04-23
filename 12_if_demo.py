#!/usr/bin/env python3
# -*- coding: utf-8 -*-

inputs = input("Enter true or false: ")
correct = False
while not correct :
    #if-elif-else 代码块不用{},而是用缩进来表示代码块，同时冒号是必须的。
    if inputs == "true" : # if 后面可以不用加括号，直接写表达式；但为了可读性，还是加上括号
        correct = True
    elif (inputs == "false") : # 不同于java中的else if，python中用elif表示else if
        correct = True
    else :
        inputs = input("Invalid input, please reenter true or false: ")
        correct = False
print(fr"Your input is '{inputs}', Program ended.") # f-string 可以和r-string一起使用, fr开头的字符串等价于f-string，所以可以直接使用f开头
