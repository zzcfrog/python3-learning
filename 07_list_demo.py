#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import operator

letters = ['a', 'b', 'c', 'd', 'e']

print(letters)

print(letters[0]) # first element
print(letters[1:3]) # slice from index 1 to 3 (not including 3)
print(letters[1:]) # slice from index 1 to end
print(letters[:3]) # slice from start to index 3 (not including 3)
print(letters[-1]) # last element
print(letters[-2:]) # slice from second last element to end
print(letters[:-1]) # slice from start to second last element (not including last element)
print(letters[::2]) # slice every second element    
print(letters[::-1]) # reverse the list
print(letters[::-2]) # reverse every second element
print(len(letters)) # length of the list

letters[0] = 'A'
print(letters)


# 数组的方法
# append() 向列表中添加元素
# extend() 向列表中添加多个元素
# insert() 在指定位置插入元素
# remove() 删除指定元素        
# pop() 删除指定位置的元素，并返回该元素的值
# index() 返回指定元素的索引
# count() 返回指定元素在列表中出现的次数
# sort() 对列表进行排序
# reverse() 反转列表
# copy() 返回列表的浅拷贝
# clear() 清空列表

# 示例
numbers = [1, 3, 2, 4, 5]
numbers.append(6) # append 6 to the end of the list
print(numbers)        # [1, 3, 2, 4, 5, 6]

numbers.extend([7, 8, 9]) # extend the list with [7, 8, 9]
print(numbers)            # [1, 3, 2, 4, 5, 6, 7, 8, 9]

numbers.insert(2, 0) # insert 0 at index 2
print(numbers)        # [1, 3, 0, 2, 4, 5, 6, 7, 8, 9]  

numbers.remove(2) # remove the first occurrence of 2
print(numbers)    # [1, 3, 0, 4, 5, 6, 7, 8, 9]

numbers.pop(2) # remove and return the element at index 2 (which is 0)
print(numbers)  # [1, 3, 4, 5, 6, 7, 8, 9]

numbers.index(5) # return the index of the first occurrence of 5 (which is 4)
print(numbers.index(5))

numbers.count(5) # return the number of occurrences of 5 in the list (which is 1)
print(numbers.count(5))

numbers.sort() # sort the list in ascending order
print(numbers)   # [1, 3, 4, 5, 6, 7, 8, 9]

numbers.reverse() # reverse the list
print(numbers)     # [9, 8, 7, 6, 5, 4, 3, 1]

del numbers[-1] # remove the last element of the list
print(numbers)   # [9, 8, 7, 6, 5, 4, 3]

del numbers[2:5] # remove the elements from index 2 to 4 (not including 5)
print(f"{numbers=}")   # [9, 8, 5, 4, 3]

numbers_copy = numbers.copy() # create a shallow copy of the list
print(numbers_copy)          # [9, 8, 7, 6, 5, 4, 3, 1]

print(numbers == numbers_copy) # True
print(numbers is numbers_copy) # False
print(operator.eq(numbers, numbers_copy)) # True



numbers.clear() # clear the list
print(numbers)   # []
