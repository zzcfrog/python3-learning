#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 11
b= 2.0

print(a + b, type(a + b)) # 13.0 <class 'float'>
print(a - b, type(a - b)) # 9.0 <class 'float'>
print(a * b, type(a * b)) # 22.0 <class 'float'>
print(a ** b, type(a ** b)) # 121.0 <class 'float'>
print(a / b, type(a / b)) # 5.5 <class 'float'>
print(a // b, type(a // b)) # 5 <class 'int'>
print(a % b, type(a % b)) # 1.0 <class 'float'>

# 比较运算符
print("a==b:", a == b )
print("a!=b:", a!= b )
print("a>b:", a > b )
print("a<b:", a < b )
print("a>=b:", a >= b )
print("a<=b:", a <= b )

# 逻辑运算符
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# 赋值运算符
a += b
print("a += b:", a)
a -= b
print("a -= b:", a)
a *= b
print("a *= b:", a)
a **= b
print("a **= b:", a)
a /= b
print("a /= b:", a)
a //= b
print("a //= b:", a)
a %= b
print("a %= b:", a)

# 成员运算符
print("1 in [1, 2, 3]:", 1 in [1, 2, 3])
print("4 not in [1, 2, 3]:", 4 not in [1, 2, 3])

a = int(a)
b = int(b)
print("a=%d,b=%d" % (a, b))
# 身份运算符    
print("a is b:", a is b) # 等价于id(a) == id(b)
print("a is not b:", a is not b) # 等价于id(a) != id(b)

# 位运算符
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 2:", a << 2)
print("a >> 2:", a >> 2)

# 运算符优先级
# 1. 圆括号 ()
# 2. 乘除法 **
# 3. 加减法
# 4. 位移运算符 << >>
# 5. 比较运算符 < > <= >= ==!=
# 6. 位运算符 & | ^ ~
# 7. 逻辑运算符 and or not
# 8. 成员运算符 in not in
# 9. 身份运算符 is is not   

# python3.5之后支持的运算符
# 1. 矩阵乘法 @

#python3.8之后支持的运算符
# 1. 海象运算符 := 表示赋值并返回变量的值
# 传统写法
a = 1
if a > 0:
    print(a)

# 新写法
if (a := 1) > 0:
    print(a)


