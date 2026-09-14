
# Python
#   不可变类型: int,float,str,tuple,bool,NoneType
#    可变类型: list, set, dict

# 赋值
# 不可变类型 (没有关联)
a = 10
b = a
b = 20
print(a, b) # a=10, b=20

# 可变类型 (有关联)
a = [1, 2, 3]
b = a
b[0] = 666
print(a, b) # [666, 2, 3] [666, 2, 3]


# 深浅拷贝的可视化视图
#  http://pythontutor.com/live.html#mode=edit

# copy: 浅拷贝/浅复制,只对可变类型有用
a = [1, 2, 3]
b = a.copy()
b[0] = 666
print(a, b) # [1, 2, 3] [666, 2, 3]

# deepcopy 深拷贝,只对可变类型有用
a = [1, 2, [3, 4]]
b = a.copy()
b[-1][-1] = 888
print(a, b) # [1, 2, [3, 888]] [1, 2, [3, 888]]

import copy
# deepcopy 深拷贝,只对可变类型有用(针对二维或者多维数组)
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[-1][-1] = 888
print(a, b) # [1, 2, [3, 4]] [1, 2, [3, 888]]

