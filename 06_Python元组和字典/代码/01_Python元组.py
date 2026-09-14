
# 元组 tuple
#    元组就是不可变的列表（不能修改）

# 元组的基本操作
# 1. 创建元组
t = (1, 2, 3)

print(t)

t = (3,) # 表示1个元素的元组. 必须添加逗号
print(t, type(t))


# t = (3)  # <class 'int'>
print(t, type(t))


# 2. 索引 （同列表）
print(t[0])

# 3. 长度 （同列表）
print(len(t))

# 4.遍历（同列表）
for i in t:
    print(i)

# 5.修改元素 （不可以修改元素）
# t[0] = 666 #报错，元组不可以修改

# 6.切片（同列表）  不会修改原元组，得到新的元组
print(t[0:2])

# 7.加法 （同列表）
print(t + (4, 5, 6))

# 8.乘法（同列表）
print(t * 2)

# 9.成员 （同列表）
print(1 in t)



# 元组的功能
# 增 : 不可以
# 删 : 不可以
# 改 : 不可以
# 查 : 索引，切片，循环

# 排序 不可以
#排序:sorted（了解）
t = (2, 3, 4, 1, 7, 9, 6)
t2 = sorted(t)
print(t2)  #[1，2，3, 4，6，7，9]

# 转换成list
nums = list(t) # [2, 3, 4, 1, 7, 9, 6]
print(nums)

# index() : 了解 （同列表）

t = (2, 3, 4, 1, 7, 9, 6)
print(t.index(4)) # 2

# count(): 计数，了解 （同列表）
t = (2, 3, 4, 4, 7, 4, 9, 6)
print(t.count(4)) # 3 个 4

#扩展：快速取值
x, y = 3, 4
print(x, y)
x, y = [3, 4]
print(x, y)
x, y = (3, 4)
print(x, y) # 3 4

_, y = (5, 6) # _是变量名
print(y) # 6


x = tuple([1, 2, 3])
print(x, type(x))



