#!/usr/bin/env python3

# Dictionary是无序键值对，相当于Java中的Map
myDict = {}
myDict['one'] = "This is one" # 添加键值对，键为'one'，值为'This is one'
myDict[2] = "This is two" # 添加键值对，键为2，值为'This is two'

# 也可以这样初始化字典
myDict = {'one': 'This is one', 2: 'This is two'}

# 还可以通过dict()函数，传入一个序列来初始化字典，序列的元素必须是键值对
myDict = dict([('one', 'This is one'), (2, 'This is two')])

# 访问字典元素
# 通过key访问value
print(myDict['one']) # 输出This is one 
print(myDict[2]) # 输出This is two

print(myDict.get('one')) # 输出This is one, 等价于dict['one']
print(myDict.get(2)) # 输出This is two, 等价于dict[2]
print(myDict.get('three', 'Not found')) # 输出Not found, 找不到键'three'时返回默认值'Not found'

# 遍历字典
for key in myDict:
    print(key, myDict[key]) # 输出键值对

for key, value in myDict.items():
    print(key, value) # 输出键值对

print(len(myDict)) # 输出字典的长度
print(myDict.keys()) # 输出字典的键列表
print(myDict.values()) # 输出字典的值列表

# 更新字典
myDict['one'] = 'This is new one' # type: ignore # 更新键为'one'的值
myDict[2] = 'This is new two' # type: ignore # 更新键为2的值
myDict.update({'three': 'This is three'}) # 添加键值对，键为'three'，值为'This is three'

# 删除字典元素
del myDict['one'] # 删除键为'one'的元素
myDict.pop(2) # 删除键为2的元素，并返回对应的值
myDict.popitem() # 删除字典中的最后一个元素，并返回该元素的键值对

# 清空字典
myDict.clear() # 清空字典 

# 字典的拷贝
dict2 = myDict.copy() # 拷贝字典
dict3 = myDict.fromkeys(['one', 2, 'three'], 'default value') # 从指定键和值创建一个新的字典, 如果键不存在则使用默认值