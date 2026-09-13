
# 列表的功能：对列表中元素操作
#    增删改查

# 增加: 添加元素
#    append(n) : 在列表的末尾追加元素
#    insert(i, n) : 在下标i的位置插入元素n
#    extend(iterable) : 在列表末尾添加多个元素
#           iterable: 列表/元组/字符串/字典/集合
# 注意append和extend区别
list1 = [1, 2, 3]
list1.append(6)
print(list1)
list1.append([4, 5])
print(list1)

list1.insert(0, 5)
print(list1)

list1.extend([7, 8])
print(list1)

# 删除:
#    pop(i) : 弹出(删除并返回)下标i对应的元素, 默认删除最后一个元素
#    remove(n) : 删除指定元素n
#    clear() : 清空列表

nums = [10, 20, 30, 40, 50]
n = nums.pop()
print(nums) # [10, 20, 30, 40]
print(n)

nums = [2, 3, 3, 4, 5, 3, 5]
nums.remove(3)  #一次只会删除一个元素
print(nums) # [2, 3, 4, 5, 1, 5]


# count(): 计数,统计列表中元素出现的次数
while nums.count(3):
    nums.remove(3)
print(nums) # [2, 4, 5, 5]

# clear() : 了解
nums.clear()

# 改: 修改元素
# nums[1] = 333
# print(nums)
# print()


# 查: 查询
#  索引: nums[1]
#  切片: nums[2:4]
#  循环: for n in nums:
#       for i in range():
#       for i,n in enumerate(nums):


# index(n) : 获取元素n第一次出现的下标,如果元素不存在则报错
nums = [2, 3, 3, 3, 3, 4, 4, 4, 5]
print(nums.index(3))  # 1
print(nums.index(4))  # 5




# 排序
#   sort() : 默认升序排列, 直接修改原列表
##     sorted(): 默认升序排列, 不改变原列表 (了解)
#   reverse() : 倒序,逆序, 直接修改原列表
##     reversed() : 倒序,逆序, 不改变原列表 (了解)


nums = [2, 4, 7, 33, 99, 6, 8]
nums.sort() # 升序 [2, 4, 6, 7, 8, 33, 99]
print(nums)

nums.sort(reverse=True) # 降序 [99, 33, 8, 7, 6, 4, 2]
print(nums)


nums = [2, 4, 7, 33, 99, 6, 8]
nums.reverse()
print(nums) # [8, 6, 99, 33, 7, 4, 2]

print(nums[::-1])# 不会修改原列表 [8, 6, 99, 33, 7, 4, 2]
print(nums)


nums = [2, 4, 7, 33, 99, 6, 8]
nums2 = sorted(nums)
print(nums2) #[2, 4, 6, 7,8,33, 99]
# print(nums) # [2, 4, 7, 33, 99, 6, 8]


# copy(): 复制,拷贝

nums = [1, 2, 3]
nums2 = nums.copy()# 复制一份列表
nums[0] = 666

print(nums) # [666, 2, 3]
print(nums2) # [1, 2, 3]



