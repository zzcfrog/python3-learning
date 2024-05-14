#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

#open()函数打开文件，并返回一个文件对象，可以对文件进行读写操作。
#文件对象有两个基本的方法：read()和write()。
#read()方法用于读取文件内容，返回字符串。
#write()方法用于向文件写入内容，参数为字符串。

#打开文件
f = open('./files/test.txt', 'w')
f.write('Hello, world!\n')
f.write('That\'s a nice day!\n')
f.close()

#读取文件

f = open('./files/test.txt', 'r')
content = f.read()
print("#read all content: \n", content)
f.close()

# 读取文件中的一行
f = open('./files/test.txt', 'r')
line1 = f.readline()
print("#read one line content: \n", line1)
f.close()

# 循环读取文件中的每一行
f = open('./files/test.txt', 'r')
s = f.readline()
line_num = 1
while s:
    print(f"#read line {line_num} content: {s}")
    line_num += 1
    s = f.readline()
f.close()

# 循环读文件的另一种方式
f = open('./files/test.txt', 'r')
for line in f:
    print(line, end='') #之所以end=''是因为本身line中包含\n
f.close()

# 循环读取的第三种方式
f = open('./files/test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end='') #之所以end=''是因为本身line中包含\n
f.close()

# open()函数的其他参数
# mode参数：
# 'r'：读模式，文件必须存在，否则报错。 指针在文件头部。
# 'w'：写模式，文件不存在，则创建，存在则覆盖。 指针在文件头部。
# 'a'：追加模式，文件不存在，则创建，存在则追加。 指针在文件尾部。
# 'r+'：读写模式，文件必须存在，否则报错。 指针在文件头部。
# 'w+'：读写模式，文件不存在，则创建，存在则覆盖。 指针在文件头部。
# 'a+'：读写模式，文件不存在，则创建，存在则追加。 指针在文件尾部。

# 'b'：二进制模式，用于读写二进制文件。 
# 't'：文本模式，用于读写文本文件。 默认就是文本模式。 
# '+'：可读写模式，可读可写。 
# 'U'：通用换行模式，适用于所有平台。 
# 'x'：独占模式，文件必须不存在，否则报错。 
# 'encoding'参数：指定文件编码。 
# 'errors'参数：指定错误处理方案。 
# 'newline'参数：指定换行符。 
# 'closefd'参数：指定是否关闭文件描述符。 
# 'opener'参数：指定打开文件函数。

# 为了更好的使用资源，应该在使用完文件后，及时关闭文件。可以使用with语句来自动关闭文件。
with open('./files/test.txt', 'r') as f:
    content = f.read()
    print("#read all content: \n", content)

f = open('./files/test.txt', 'a+')
f.write(f'appended content! {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
pos_pnt = f.tell() # 指针当前位置
print("#current position: ", pos_pnt)
f.seek(0) # 指针回到文件头部 
# 指针的移动可以使用seek(offset, whence) 
#whence=0表示从文件头部开始，1表示从当前位置开始，2表示从文件尾部开始。
# offset表示偏移量，正数表示向后移动，负数表示向前移动。
# 指针移动到文件尾部时，使用seek(0, 2)
# 指针移动到文件头部时，使用seek(0, 0)

print("#after appended content: \n", f.read())
f.close()
