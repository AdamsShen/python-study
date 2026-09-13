''' '''
# 练习：
# 1. 打印1-100之间的所有偶数
i = 1
while i <= 100:
    if i % 2 ==0:
        print(i)
    i += 1

# 2.求 1-100之间可以被6整除的数的个数

num = 0
i = 1
while i <= 100:
    if i % 6 == 0:
        num += 1
    i += 1
print(num)

# 3. 打印1-100之间的所有奇数

i = 1
while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1


# 4.计算1到100以内所有偶数的和。

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)


# 5.计算1到100以内所有能被3或者7整除的数的和。

i = 1
sum = 0
while i <= 100:
    if i % 3 == 0 or i % 7 == 0:
        sum += i
    i += 1
print(sum)


# 6.计算1到100以内能同时被7和3整除的数的个数。

i = 1
num = 0
while i <= 100:
    if i % 7 == 0 and i % 3 == 0:
        num += 1
    i += 1
print(num)



