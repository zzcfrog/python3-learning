#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for循环的基本Pattern
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>

team = ['Alice', 'Bob', 'Charlie']
for member in team:
    print(member, end=" ")
else:
    print('\n\tAll members have been printed.')

word = 'hello'
for letter in word: # word也可遍历，因为string也是sequence
    print(letter, end=" ")
print('\n\tAll letters have been printed.')

for i in range(3, 10): # 遍历3到9的数字，不包括10
    print(i,end=' ')
else:
    print('\n\tAll numbers have been printed.')


'''
    range()函数
    
    range(stop)：从0开始，到stop-1结束，步长为1
    range(start, stop)：从start开始，到stop-1结束，步长为1
    range(start, stop, step)：从start开始，到stop-1结束，步长为step

    例：
    range(5)：0 1 2 3 4
    range(2, 5)：2 3 4
    range(2, 10, 3)：2 5 8
    range(10, 2, -1)：10 9 8 7 6 5 4 3 2
'''