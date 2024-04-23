#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串的定义
s = "Hello, world!"

# 也可以用str()函数将其他类型转换为字符串
s = str(123) # 输出"123"

# 转义字符，比如\n表示换行，\t表示制表符，\r表示回车，\b表示退格，\f表示换页，\"表示双引号，\'表示单引号。"\\"表示反斜杠。
print("Hello, \"world\"!")

# 字符串不想被转义时，可以用r''表示原始字符串，即所有的字符串都是直接输出，不进行转义。
print(r'Hello, "world"!\n')

# 字符串可以用+运算符连接，也可以用*运算符重复。
s = "hello" + "world"
print(s)

s = "hello" * 3
print(s)

# 字符串的格式化，用%运算符，可以将字符串中的占位符替换为变量的值。
name = "Alice"
age = 25
s = "My name is %s, and I am %d years old." % (name, age)
print(s)

# 占位符可以用序号指定，也可以用关键字指定。
s = "My name is %(name)s, and I am %(age)d years old." % {"name": "Alice", "age": 25}
print(s)

# 占位符类别：
# %s 字符串（字符串）
# %d 整数（整数）
# %f 浮点数（浮点数）
# %x 十六进制整数（整数）
# %o 八进制整数（整数）
# %e 指数记数法（浮点数）
# %g 自动选择合适的格式（浮点数：%f或%e）   

# 字符串操作
word = "hello, world"
print(word.upper()) # 转换为大写
print(word.lower()) # 转换为小写
print(word.capitalize()) # 首字母大写
print(word.title()) # 每个单词的首字母大写
print(word.strip()) # 去掉两端空格
print(word.lstrip()) # 去掉左侧空格
print(word.rstrip()) # 去掉右侧空格
print(word.replace("，", "！")) # 替换
print(word.split(",")) # 以指定字符分割字符串，返回列表
print(" ".join(word)) # 以指定字符连接字符串，返回字符串



# 字符串的基本函数
world = "hello, world"
# 输出字符串长度
print(len(world))
# 输出字符串中某个字符出现的次数
print(world.count("l"))
# 输出字符串是否以某个字符开头
print(world.startswith("he"))
# 输出字符串是否以某个字符结尾
print(world.endswith("ld"))
# 输出字符串是否包含某个子串，如果包含，返回子串的第一个索引；否则返回-1
print(world.find("l"))
# 输出字符串是否全部由字母组成
print(world.isalpha())
# 输出字符串是否全部由数字组成
print(world.isdigit())
# 输出字符串是否全部由字母或数字组成
print(world.isalnum())
# 输出字符串是否全部由大写字母组成
print(world.isupper())
# 输出字符串是否全部由小写字母组成
print(world.islower())
# 输出字符串是否以大写字母开头
print(world.istitle())

# 字符串的数组化操作
world = "hello, world"
# 输出第一个字符
print(world[0])
# 输出最后一个字符
print(world[-1])
# 输出从第2个开始到第5个的字符（从0开始计数，包含1，不包含5）
print(world[1:5])
# 输出从第2个开始到最后的字符
print(world[1:])
# 输出从第2个开始到倒数第2个的字符
print(world[1:-1])
# 输出从第2个开始到倒数第2个的字符，每隔2个取一个
print(world[1:-1:2])
# 输出从第2个开始到最后的字符，每隔2个取一个
print(world[1::2])
# 输出从最后一个开始到第2个的字符
print(world[-2:-5:-1])

# 不换行输出字符串，使用end指定结束符
print("Hello, world", end="")
print("!")

'''特别关注：f-string（Python 3.6+）'''
# 3.6版本引入了f-string，可以直接在字符串中嵌入变量，不需要使用format函数。
name = "Alice"
age = 25
s = f"My name is {name}, and I am {age} years old."
print(s)     # 输出：My name is Alice, and I am 25 years old.

# f-string的=语法,可以指定变量名,并在输出时显示变量名
print(f"Hello, {name=}")  # 输出：Hello, name='Alice'
print(f"Hello, {age=}")   # 输出：Hello, age=25