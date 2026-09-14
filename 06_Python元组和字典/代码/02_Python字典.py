
# 字典 dict  dictionary字典

# dict特点：
#   1. 字典的key不能重复 （key 唯一性）
#   2. 字典的key不可以是 可变类型(list,dict,set)，但是建议使用字符串
#   3.  key无序性



# 1.创建
#  key:value ：键值对
d= {'name':'张三丰','age':100, 'age': 2}
print(d)

d= {'name':'张三丰','age':100, 1: 2}
print(d)

d= {'name':'张三丰','age':100, (1, ): 2}  #(1, ) 表示元组
print(d)

# 2.索引 : 没有数字索引，但是可以使用key
d= {'name':'张三丰','age':100}
print(d['name']) # 张三丰
print(d['age']) # 100

print(d.get('name'), d.get('names')) #张三丰. None找不到的话，不会报错，会返回None
print(d.get('names', 'lance')) #如果找不到names, 则使用默认值"lance"

# 3.长度
d= {'name':'张三丰','age':100}
print(len(d))

# 4.遍历
d= {'name':'张三丰','age':100}

print(d.keys())
print(d.values())
print(d.items())

print(list(d.keys())) # 所有的key['name','age']
print(list(d.values())) #所有的value['张三丰'，100]
print(list(d.items())) #所有的key:value [('name','张三丰'), ('age',100)]

# 推荐
for key in d:
    print(key, d[key]) # key

# 不推荐
# for key in d.keys():
# print(key)
for val in d.values():
    print(val)

#推荐
for key,val in d.items():
    print(key, val)

# 5.修改元素
d= {'name':'张三丰','age':100}
d['age'] = 200
print(d)


# 6.切片: 不可以, 字典是无序的, 且没有数字索引

# 7.合并
d1 = {'name':'张三丰','age':100}
d2 = {'mingzi':'张三丰','nianling':100}
# print(d1 + d2) #不可以，会报错
print(d1.update(d2)) # 将d2合并到d1，d1会更新，d2保持不变
print(d1)   # {'name': '张三丰', 'age': 100, 'mingzi': '张三丰', 'nianling': 100}
print(d2)  # {'mingzi': '张三丰', 'nianling': 100}




# 8.重复： 不可以
# print(d1 * 3)

# 9.成员 (掌握)
d1 = {'name':'张三丰','age':100}
print('name' in d1) # True
print('name' not in d1) # False
print('names' in d1) # False



# 字典的功能
# 增删改查
#  增，改
d1 = {'name':'张三丰','age':100}
d1['age'] = 200
print(d1)
d1['names'] = '张三丰' #新增元素

print(d1)  # {'name': '张三丰', 'age': 200, 'names': '张三丰'}




# 删：
#  pop(key): 删除key对应的元素 (掌握 )
#  clear() : 清空字典 （了解）
#  popitem() : 删除一个元素 （了解）
d = {'name': '张三丰', 'age': 200, 'names': '张三丰'}
d.pop('name') # 删除key为'name'的元素
print(d)
d.clear()

print(d)    # {},空字典

d =  {'name': '张三丰', 'age': 200, 'names': '张三丰'}
d.popitem() # 删除最后一个元素
print(d)



