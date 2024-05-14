#!/usr/bin/env python3

# 导入整个模块
import math

#导入模块中的某个函数
from math import sqrt

#导入模块中的多个函数
from math import sin, cos, tan

#导入模块中的所有函数
from math import *

#from 包名.模块名 import 函数名 可直接使用函数名
from module.fibo import fibonacci
#from 包名 import 模块名 需要使用模块名.函数名
from module import fibo
#import 包名.模块名 导入整个模块需要使用全限定名
import module.fibo
#import 包名.模块名 as 别名 导入整个模块并给其别名
import module.fibo as fibo_alias

print(f"{fibonacci(10)=}") # 直接使用函数名
print(f"{fibo.fibonacci(10)=}") # 使用模块名.函数名
print(f"{module.fibo.fibonacci(10)=}") # 使用全限定名
print(f"{fibo_alias.fibonacci(10)=}") # 使用别名.函数名
print(pi)
print(sqrt(2))
print(sin(math.pi/2))