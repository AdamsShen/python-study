
# 使用场景：
#   while循环： ①无限循环， ②未知循环次数
#   for循环：一般使用在已知循环次数




# 打印1~100的每一个数
'''
i = 1
while i<= 100:
    print(i)
    i += 1
'''

# for-in循环：
#  每次循环，i会自动等于右边range中的每一个数

for i in range(1, 101):
    print(i)

# 求1~100的和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)


# for循环使用场景
# 1.和range结合
#   比如：循环1~10，找到能被3整除的数

for i in range(1, 11):
    if i % 3 == 0:
        print(i)



# 2.和列表结合
# 列表的基本操作
#  元素：列表中的每一个值

nums = [1, 2, 3, 4, 5]
print(nums)
# 索引
print(nums[0])

print(nums[-1])  # 最后一个元素

print(len(nums))  # 列表的长度


# 遍历列表
for num in nums:
    print(num)   # num是列表中的每一个元素


for i in range(len(nums)):
    print(i, nums[i])

# enumerate:枚举，列举，会将索引和元素一起得到
for i,n in enumerate(nums):
    print(i, n)

# 还可以使用for的有：

#    range()
#    list: [1,2,3]
#    dict: {'name': 'ikun', 'age': 20}
#    tuple: (1,2,3)
#    set: {1,2,3}
#    str: "hello"



