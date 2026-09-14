
# 集合 set
#   特点: 唯一性(去重), 无序性, 元素不能是可变类型(list,dict,set)

# 1.创建集合
s = {1, 2, 3, 4, 5, 4, 5}
print(s) # {1, 2, 3, 4, 5}

s = {}  # 默认是空字典
print(s, type(s)) # {} <class 'dict'>
s = set()  # 创建空集合
print(s, type(s)) # set() <class 'set'>

# 2.不能用索引, 集合是无序的，索引不能使用
s = {1, 3, 4, 3, 2, 2, 2}
# print(s[0]) # TypeError: 'set' object is not subscriptable


# 3.长度
print(len(s))

# 4.循环
for i in s:
    print(i)


# 5.修改:删除一个,然后再添加新的
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s) # {1, 2, 4, 5}

# 6.不能用切片
# 7.不能用加法
# 8.不能用乘法
# 9.成员
print(3 in {12, 3, 4, 5})  # True


# 功能
#  add(): 添加元素
#  pop(): 删除元素
#  clear(): 清空
#  remove(3)  # 删除元素3,如果元素不存在会报错
#  discard(3)  # 删除元素3,如果元素不存在不会报错
s = {1, 2, 3, 4, 5}
s.add(6)
print(s)


s.pop()  #删除第一个元素
print(s)

s.clear()
print(s)

s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)    # {1, 2, 4, 5}
s.discard(30)  # 删除元素30,如果元素不存在不会报错
print(s)


# 集合关系
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)  # 交集  {3, 4}
print(s1 | s2)  # 并集 {1, 2, 3, 4, 5, 6}
print(s1 - s2)  # 差集（相对补集） {1, 2}, 只存在s1中的元素
print(s1 >= s2)  # 包含关系 True ,表示s1中是否全部包含s2的元素, False


# 练习：利用集合去重
nums = [1, 3, 3, 2, 2, 2, 4, 5, 4, 5]
#空间复杂度: 占用内存大小
#时间复杂度: 消耗的时间
nums = set(nums)
print(nums)
print(list(nums))


