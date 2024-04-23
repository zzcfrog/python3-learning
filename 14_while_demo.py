#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# while循环的基本pattern
#while <expression>:
#     <statements>
# else:
#     <statements>

a = 1
while a <= 10:
    print(a)
    a += a
else: # 这个else语句其实是多余的，while执行完毕后，会自动执行else语句，和执行接下来的语句没有区别
    print("The loop is over")