#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max(x, y):
    return x if x>y else y #这里是三目运算符，相当于java的：x>y?x:y

print(max(3, 5)) # 5
print(max(7, 2)) # 7

# 关于参数传递：
# 值传递：number, string, tuple, 复制一份到函数内部，修改不会影响原值
# 引用传递：list, dict, set，直接传递地址，修改会影响原值
a, b = 3, 5
def sum_square(x, y):
    x, y = x**2 , y**2
    return x+y
print(f"{sum_square(a, b)=}，{a=},{b=}")

list1 = [1, 2, 3]
def reverse(list):
    list.reverse()
    return list
print(f"{reverse(list1)=}，{list1=}")

def reverse_new(list):
    result = list.copy()
    result.reverse()
    return result
print(f"{reverse_new(list1)=}，{list1=}")

'''
    参数分类：
    位置参数：按照位置顺序传入，必须传入指定数量的参数，否则会报错
    关键字参数：按照参数名传入，可以传入任意数量的参数，不指定参数名则按顺序传入
    默认参数：如果函数定义时指定了默认值，则可以不传入该参数，否则必须传入
    变长参数：*args，可以传入任意数量的参数，会以元组形式传入，可以用在不确定参数数量的情况下
    命名关键字参数：**kwargs，可以传入任意数量的关键字参数，会以字典形式传入，可以用在不确定参数数量的情况下
'''

def sub_square(x,y):
    return x**2 - y**2

print(f"{sub_square(3,2)=}") # 位置参数:两个参数必须按顺序传递
print(f"{sub_square(y=2,x=3)=}") # 关键字参数:可以不按顺序传入

def person_info(age, name = 'somebody'):  # 定义时可以指定默认值，调用时可以不传入，也可以传入。定义时，有默认值的参数必须在后面
    print(f"name is {name}, age is {age}")

person_info(age=25) # 调用时只传入age参数，name参数使用默认值

# 一个*是边长参数，必须放到最后一个位置参数之后，并且变长参数是元组形式
def add_numbers(*values): 
    result = 0 
    for v in values:
        result += v
    return result

print(f"{add_numbers(1,2,3,4,5)=}") # 15

# 两个**是命名关键字参数，必须放到最后一个位置参数之后，并且命名关键字参数是字典形式
def person_info_extra(name, age, **ext):  
    print(f"name is {name}, age is {age}", end=', ')
    ext_len = len(ext)
    for k, v in ext.items():
        if ext_len > 1:
            print(f"{k} is {v}", end=', ')
        elif ext_len == 1:
            print(f"{k} is {v}.")
        ext_len -= 1

person_info_extra(name='zack', age=25, city='Beijing', job='Engineer') # 调用时传入所有参数，包括命名关键字参数

# 必须使用关键字参数才能传入命名关键字参数，否则会报错
person_info_extra(25, name='zack', city='Beijing', job='Engineer') # 错误，必须使用关键字参数

# 通过参数*后的变量名来指定必须使用关键字参数
def f(a,b,*,c,d):
    print(f"{a=},{b=},{c=},{d=}")

f(1,2,c=3,d=4) # 正确，使用关键字参数
f(1,2,3,4) # 错误，缺少关键字参数c,d

# 通过参数/后的变量名来指定必须使用位置参数
def f(a,b,/,c,d,*,e,f):
    print(f"{a=},{b=},{c=},{d=},{e=},{f=}")

f(1,2,c=3,d=4,e=5,f=6) # 正确，使用位置参数和关键字参数
f(1,2,3,4,e=5,f=6) # 正确，使用位置参数
f(1,2,3,4,5,6) # 错误，缺少关键字参数e,f
f(a=1,b=2,c=3,d=4,e=5,f=6) # 错误，不能使用关键字参数