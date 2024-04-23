#!/usr/bin/env python3

# Dictionary是无序键值对，相当于Java中的Map
dict = {}
dict['one'] = "This is one" # 添加键值对，键为'one'，值为'This is one'
dict[2] = "This is two" # 添加键值对，键为2，值为'This is two'

# 也可以这样初始化字典
dict = {'one': 'This is one', 2: 'This is two'}

# 还可以通过dict()函数，传入一个序列来初始化字典，序列的元素必须是键值对
dict = dict([('one', 'This is one'), (2, 'This is two')])

# 访问字典元素
# 通过key访问value
print(dict['one']) # 输出This is one 
print(dict[2]) # 输出This is two

print(dict.get('one')) # 输出This is one, 等价于dict['one']
print(dict.get(2)) # 输出This is two, 等价于dict[2]
print(dict.get('three', 'Not found')) # 输出Not found, 找不到键'three'时返回默认值'Not found'

# 遍历字典
for key in dict:
    print(key, dict[key]) # 输出键值对

for key, value in dict.items():
    print(key, value) # 输出键值对

print(len(dict)) # 输出字典的长度
print(dict.keys()) # 输出字典的键列表
print(dict.values()) # 输出字典的值列表

# 更新字典
dict['one'] = 'This is new one' # 更新键为'one'的值
dict[2] = 'This is new two' # 更新键为2的值
dict.update({'three': 'This is three'}) # 添加键值对，键为'three'，值为'This is three'

# 删除字典元素
del dict['one'] # 删除键为'one'的元素
dict.pop(2) # 删除键为2的元素，并返回对应的值
dict.popitem() # 删除字典中的最后一个元素，并返回该元素的键值对

# 清空字典
dict.clear() # 清空字典 

# 字典的拷贝
dict2 = dict.copy() # 拷贝字典
dict3 = dict.fromkeys(['one', 2, 'three'], 'default value') # 从指定键和值创建一个新的字典, 如果键不存在则使用默认值

# 字典的运算
dict4 = dict.union(dict2) # 并集
dict5 = dict.intersection(dict2) # 交集
dict6 = dict.difference(dict2) # 差集
dict7 = dict.symmetric_difference(dict2) # 对称差集