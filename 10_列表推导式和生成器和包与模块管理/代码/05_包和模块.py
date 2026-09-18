''' '''

import math


# 包 package :  是一个有__init__.py文件夹
# 模块 module:  是一个python文件,以.py结尾的文件都可以算作一个module

# 封装思路: 项目 => 包(文件夹) => 模块(python文件) => 类 => 函数 => 代码

# 创建包
# 创建模块



# 导入模块
#   import
#   from - import
import time,math,random
import time
import math
from ctypes.macholib.framework import framework_info

print(time.time())

# 精确导入
# from matplotlib import pyplot as plt
# from time import sleep   # 从time模块中导入sleep
# sleep(1)


# # 模糊导入 : * 表示所有内容
from time import *   # 表示导入time的所有模块,和 import 模块的区别，就是在使用时无需加上模块名称
print(time())


# 自定义模块: 模块是单利模式(导入多次，只会执行一次)
print()
'''
import module1  # 我是模块1
import module1
print(module1.name)   # ikun
module1.fn1()  # 9
'''



from module1 import name, fn1
print(name)  # ikun
# print(module1.name)  # 不导入会报错
fn1()  # 9


# 模块在包中,有包的情况下 一定要from package
# 有以下两种方式
# print()
# from package1 import module2
# print(module2.name)


from package1.module2 import name
print(name)


print()
# 别名: as   改名后只能用别名,不能使用原来的方式
import module1 as m1
print(m1.name)


from package1 import module2 as m2
print(m2.name)


from module1 import name as n1
print(n1)

# from package1 import 123  # 模块名不能随便命名，导入的时候就报错了