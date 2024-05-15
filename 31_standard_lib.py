#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pyth 常用的标准库有：
# 1. os：操作系统接口
# 2. sys：系统相关的参数和函数
# 3. time：时间日期
# 4. datetime：日期时间
import datetime
print(datetime.datetime.now()) # 获取当前时间戳
print(datetime.datetime.today()) # 获取今天
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 格式化时间戳
# 5. calendar：日历
# 7. random：随机数生成
# 9. re：正则表达式
import re
match = re.match(r"\w+.\w+.com", "www.baidu.com"); print(match) # 匹配字符串的开始位置
search = re.search(r"\w+.\w+.com", "www.baidu.com"); print(search) # 匹配整个字符串，并返回第一个匹配结果
findall = re.findall(r"\w+.\w+.com", "www.baidu.com"); print(findall) # 匹配整个字符串，并返回所有匹配结果
# 10. math：数学
import math
print(math.pi) # 圆周率
print(math.e) # 自然常数
print(math.sqrt(2)) # 平方根
print(math.pow(2, 3)) # 2的3次方
print(math.floor(3.5)) # 向下取整
print(math.ceil(3.5)) # 向上取整
print(math.sin(math.pi/2)) # 正弦值
print(math.cos(math.pi/2)) # 余弦值
print(math.log(math.e)) # 自然对数
# 11. json：JSON 数据处理
# 12. csv：CSV 文件读写
# 13. sqlite3：SQLite 数据库
# 14. xml：XML 数据处理
# 15. html：HTML 网页解析
# 16. smtplib：发送邮件
# 17. email：邮件处理
# 18. urllib：URL 处理
# 19. http.client：HTTP 客户端
# 20. ftplib：FTP 客户端
# 21. subprocess：子进程
# 22. shutil：文件复制、移动、删除、压缩 | shutil.copyfile(src, dst) shutil.move(src, dst) shutil.rmtree(path)
# 23. glob：文件路径匹配 | glob.glob(‘*.txt’)可以列出所有.txt文件的路径列表
# 24. tempfile：临时文件和目录
# 25. logging：日志记录
# 26. unittest：单元测试
# 27. argparse：命令行参数解析
# 28. traceback：异常跟踪
# 29. pdb：Python 调试器
# 30. gc：垃圾回收
# 31. ctypes：外部函数库
# 32. multiprocessing：多进程
# 33. threading：多线程