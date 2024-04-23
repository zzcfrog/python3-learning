#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
列表推导式所谓推导式，就是用一种更简洁的方式来根据现有的序列创建新的序列。
'''

# List comprehension, 列表推导式: 
# 语法： [expression for item in iterable if condition]
# 可以理解为：expression是java lambda中的map, condition是java lambda中的filter
list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1]
print(f"{list2=}")   # [2, 4, 6, 8, 10]

# 条件筛选：
list3 = [x for x in list1 if x % 2 == 0]
print(f"{list3=}")   # [2, 4]

# 多值列表推导式：
list4 = [[x, y] for x in range(3) for y in range(2)]
print(f"{list4=}")   # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]

list5 = [[x, y] for x in range(3) if x % 2 == 0 for y in range(2) if y % 2 == 0]
print(f"{list5=}")  # [[0, 0], [0, 2]]

# 嵌套列表推导式：
list6 = [[x, y*2] for x in range(3) for y in [x**2 for x in range(2,4)]]
print(f"{list6=}")  # [[0, 4], [0, 9], [1, 4], [1, 9], [2, 4], [2, 9]]

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 元组推导式：
# 语法： (expression for item in iterable if condition)
# 可以理解为：expression是java lambda中的map, condition是java lambda中的filter
tuple1 = tuple(x*2 for x in range(5))
print(f"{tuple1=}")   # (0, 2, 4, 6, 8)

# 条件筛选：
tuple2 = tuple(x for x in range(5) if x % 2 == 0)
print(f"{tuple2=}")   # (0, 2, 4)

# 多值元组推导式：
tuple3 = tuple((x, y) for x in range(3) for y in range(2))
print(f"{tuple3=}")   # ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1))

tuple4 = tuple((x, y) for x in range(3) if x % 2 == 0 for y in range(2) if y % 2 == 0)
print(f"{tuple4=}")  # ((0, 0), (0, 2))

# 嵌套元组推导式：
tuple5 = tuple((x, y*2) for x in range(3) for y in (x**2 for x in range(2,4)))
print(f"{tuple5=}")  # ((0, 4), (0, 9), (1, 4), (1, 9), (2, 4), (2, 9))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 字典推导式：
# 语法： {key_expression:value_expression for item in iterable if condition}
# 可以理解为：key_expression和value_expression的键值对是java lambda中的map, condition是java lambda中的filter
dict1 = {x:x**2 for x in range(5)}
print(f"{dict1=}")   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


dict2 = {x:y for x in range(3) for y in range(3)}
print(f"{dict2=}")   # {0: 2, 1: 2, 2: 2} 由于key不能重复，所以只有一个值

dict3 = {x:y for x in range(3) if x % 2 == 0 for y in range(2) if y % 2 == 0}
print(f"{dict3=}")   # {0: 2, 1: 2, 2: 2}

# 嵌套字典推导式：
dict4 = {x:y*2 for x in range(3) for y in {x**2:x**3 for x in range(2,4)}}
print(f"{dict4=}")   # {0: 18, 1: 18, 2: 18}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 集合推导式：
# 语法： {expression for item in iterable if condition}
# 可以理解为：expression是java lambda中的map, condition是java lambda中的filter
set1 = {x**2 for x in range(5)}
print(f"{set1=}")   # {0, 1, 4, 9, 16}

set2 = {x//2 for x in range(1,6)}
print(f"{set2=}")   # {0, 1, 2}

set3 = {x for x in range(3) if x % 2 == 0}
print(f"{set3=}")   # {0, 2}

set4 = {x for x in range(3) for y in range(2) if y % 2 == 0}
print(f"{set4=}")   # {0, 1, 2}

# 嵌套集合推导式：
set5 = {x*y for x in range(2,4) for y in range(2,4)}
print(f"{set5=}")   # {9, 4, 6}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 生成器推导式：
# 语法： (expression for item in iterable if condition)
# 特别注意：生成器推导式使用的是()而不是[]，因为[]是用来表示列表的，而()是用来表示元组的。
gen_list = (x for x in list1)
print(f"{gen_list=}")   # <generator object <genexpr> at 0x10a3d9d90>

# 不能使用print()打印生成器，只能使用next()方法来获取生成器的下一个值。
print(next(gen_list))   # 1
print(next(gen_list))   # 2
print(next(gen_list))   # 3
print(next(gen_list))   # 4
print(next(gen_list))   # 5

print(type(gen_list))

