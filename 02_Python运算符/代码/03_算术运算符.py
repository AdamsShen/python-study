

# Python算术运算符：
#    +  -  *  /(除，有小数)  %  //（整除:向下取整）   **（次方）
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 / 4)
print(10 % 4)
print(10 // 4)
print(10 ** 4)   # 10000


print(-10 //4 ) # -3

# 科学计数法
a = 3.14* 10**5
b = 3.14e5
print(a)
print(b)


# 常见内存单位：
# 1b = 0 或 1
# 1Byte = 8bit
# 1KB = 1024Byte
# 1MB = 1024KB
# 1GB = 1024MB
# 1TB = 1024GB
# 1PB = 1024TB
# 1EB = 1024PB
# ...

num = int(input("请输入三位数："))
print(num)
print(type(num))
#得到个位十位百位
ge = num % 10
shi = num // 10 % 10
bai = num // 100
print(ge, shi, bai)



