#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#lambda 是匿名函数，格式如下：
#lambda 参数列表 : 表达式

sum = lambda a,b : a+b
print(sum(1,2)) # Output: 3


#lambda 也可以作为函数参数传递
def multiply_n(n):
    return lambda a : a*n

times_3 = multiply_n(3)
times_5 = multiply_n(5)

print(times_3(2)) # Output: 6
print(times_5(2)) # Output: 10