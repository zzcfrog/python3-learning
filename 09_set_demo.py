#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 有去重功能的集合
s = {1, 2, 3, 2, 4}
print(s)  # {1, 2, 3, 4}

'''特别注意'''
# set可以使用{}创建，也可以使用set()函数创建，但是如果传入的参数是可迭代对象，则会自动转换为set
s1 = set([1, 2, 3, 2, 4]) # 通过set()函数，使用数组创建
s2 = set((1, 2, 3, 2, 4)) # 通过set()函数，使用元组创建
s3 = set(range(1, 5)) # 通过set()函数，使用range创建
print(s,s1, s2, s3) # {1, 2, 3, 4} {1, 2, 3, 4} {1, 2, 3, 4} {1, 2, 3, 4}

# 添加元素
s.add(5)
print(s)  # {1, 2, 3, 4, 5}

# 删除元素
s.remove(2)
print(s)  # {1, 3, 4, 5}

s.discard(2)  # 若元素不存在，则不报错
print(s)  # {1, 3, 4, 5}


# 集合的遍历
for i in s:
    print(i)  # 1 3 4 5

# 集合的基本操作

s1 = {1, 2, 3}
s2 = {3, 4, 5}
# 1. 并集
s3 = s1.union(s2)
print(s3)  # {1, 2, 3, 4, 5}
print(s1 | s2)  # {1, 2, 3, 4, 5}

# 2. 交集
s3 = s1.intersection(s2)
print(s3)  # {3}
print(s1 & s2)  # {3}

# 3. 差集
s3 = s1.difference(s2)
print(s3)  # {1, 2}
print(s1 - s2)  # {1, 2}

# 4. 对称差集(异或集)
s3 = s1.symmetric_difference(s2)
print(s3)  # {1, 2, 4, 5}
print(s1 ^ s2)  # {1, 2, 4, 5}

# 5. 子集
print(s1.issubset(s2))  # False
print(s1 <= s2)  # False

# 6. 超集
print(s1.issuperset(s2))  # False
print(s1 >= s2)  # False


