#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pickle是一个用于序列化和反序列化Python对象结构的模块。
# 它可以将任意对象序列化成一个字节序列，并在需要的时候将其还原。

import pickle

f = open('pikle_test.b', 'wb') #二进制打开
data_map = {'a':[1,2.0,3+1j],
            'b':("a","b","c"),
            'c':None}
pickle.dump(data_map, f) #序列化
f.close()

f = open('pikle_test.b', 'rb') #二进制打开
data_map = pickle.load(f) #反序列化
print(data_map)
f.close()
