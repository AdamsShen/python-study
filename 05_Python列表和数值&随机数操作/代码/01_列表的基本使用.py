from dis import print_instructions

# Python数据类型:
#  int, float, str, bool, NoneType,
#  list, tuple, dict, set(了解), bytes

# list列表 : Array数组
# 为什么要使用列表：
# 举例：如果我们表示汽车品牌用变量保存单个值
a = "BYD"
b = "五菱宏光"
c = "小米"
d = "蔚来"
e = "法拉利"
f = "兰博基尼"
g = "路虎"

# 如果要你表示300个品牌, 变量就太多了，这时我们可以使用列表来表示：
cars = ["BYD", "五菱宏光", "小米", "蔚来", "蔚来", "法拉利", "兰博基尼", "路虎"]



# 列表的基本功能
# 1.列表定义
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 建议使用相同类型的元素


# 2.索引,下标
#   从0开始
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print(nums[5])
print(nums[6])

# 倒数第一个元素
print(nums[-1])
print(nums[-2])

# 3.长度,元素个数
print(len(nums))

# 4.遍历,循环
for i in nums:
    print(i)

for i in range(len(nums)):
    print(nums[i])


for i,n  in enumerate(nums):
    print(i, n)

# 5.修改列表

nums = [1, 2, 3]
nums[0] = 666
print(nums)



# 6.切片 (很重要) : 不会修改原列表
#    list[start : stop : step] : [start, stop)
#  和range(start, stop, step)类似  [start, stop)

ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(ages[:])  # 取所有数据
print(ages[0:5])
print(ages[:5])  # 取前5个元素  [0, 5)
print(ages[5:])  # 取后5个元素  [5, 10)

print(ages[0:10:2])   # 取前10个元素，步长为2
print(ages[::2])   # 取所有元素，步长为2
print(ages[9:1:-1])   # 取后10个元素，步长为-1
print(ages[::-1])  # 取所有元素，步长为-1,倒序

# 7. 合并 +  (了解)
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

# 8. 重复 * (了解)
print(a * 3)


# 9. 成员 in (掌握)
print(3 in a)

if 3 in a:
    print("3在列表a中")

# 需求: 列表去重 (掌握)
nums1 = [1, 2, 2, 3, 4, 4, 5]

nums2 = []
for i in nums1:
    if i not in nums2:
        nums2.append(i)   # 添加元素
print(nums2)

nums1 = [1, 2, 2, 3, 4, 4, 5]
nums2 = list(set(nums1))
print(nums2)





# 10.删除元素 del (了解)

num = [1, 2, 3, 4, 5]
del num[0]
print(num)
del num[1:3]
print(num)
del num[:]
print(num)
