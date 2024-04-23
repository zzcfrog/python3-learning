#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用yield关键字声明的变量是一个生成器，不可以直接调用，可以通过next()函数来获取下一个值，也可通过for循环来迭代。
# 如果函数中使用了yield关键字，那么函数就变成了一个生成器，每次调用next()函数，函数会返回yield关键字后面的值，并暂停执行，直到下一次调用next()函数。

def my_generator(n):
    for i in range(n):
        yield i*i

# 调用生成器
g = my_generator(5)
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 4
print(next(g))  # 9
print(next(g))  # 16


# 也可以使用for循环来迭代生成器
for i in my_generator(5):
    print(i)     # 0 1 4 9 16

# 注意：生成器只能迭代一次，第二次迭代时，会抛出StopIteration异常。
