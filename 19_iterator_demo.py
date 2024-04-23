#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyIterator:
    def __init__(self, start, end): # self代表类的当前实例化对象，必须在构造方法中第一个参数位置声明，self相当于java中的this关键字。
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration # raise 相当于java中的throw语句
        else:
            self.current += 1
            return self.current - 1


if __name__ == '__main__':
    my_iter = MyIterator(1, 5)
    for i in my_iter:
        print(i)     # output: 1 2 3 4 5

#迭代器有两个非常中要的方法:
#iter()方法: 该方法返回一个迭代器对象，该对象实现了__iter__()方法，该方法返回一个迭代器对象。
#next()方法: 该方法返回迭代器的下一个元素，如果没有下一个元素，则抛出StopIteration异常。
list1 = range(1, 4)
iter1 = iter(list1)
print(next(iter1))  # output: 1
print(next(iter1))  # output: 2
print(next(iter1))  # output: 3
print(next(iter1))  # output: StopIteration

