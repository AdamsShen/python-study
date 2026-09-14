
# 字符串的基本操作
#  str : 引号包裹的就是字符串 'abc'  "abc" """abc"""(多行字符串)

# int

# 1.创建字符串
s = '宝，买房吗'
print(s)

# 2.索引
print(s[0])
print(s[1])
print(s[2])
print(s[-1])

# 3.长度
print(len(s))

# 4. 循环
s = 'abc'
for i in s:
    print(i)   #字符char

for i in range(len(s)):
    print(s[i])   #字符char

for i, v in enumerate(s):
    print(i, v)   #字符char


# 5.修改字符串: 字符串str是不可变类型。不可以修改
# s = 'abc'
# s[0] = 'B'  # 报错，字符串是不可变类型
# print(s)

s = 'abc'
s = s + 'def'
print(s)


# 6.切片
s = 'ABCDEFGHI'
print(s[0:2])   #字符char
print(s[:4]) #'ABCD'
print(s[4:])   #'EFGHI'
print(s[2:4])#'CD'
print(s[2:7:2])# 'CEG'
print(s[::-1])   # 'IHGFEDCBA'

# 7.加法
s = 'abc'
s = s + 'def'
print(s)

# 8.乘法
s = 'abc'
s = s * 3
print(s)


# 9.成员
s = 'abc'
print('a' in s)

print('abc' in s)


