''' '''

# 循环结构：
#    while循环
#    for-in循环

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")


# 死循环：无限循环，循环不会停止

# while True:
#     print("hello world")

#  死循环一般可以和input或time.sleep结合使用
# 需求：不断输入年龄，判断该年龄是否大于30
#
# while True:
#     age = int(input("请输入年龄: "))
#     if age > 30:
#         print("大于30")
#     else:
#         print("小于等于30")



# 使用场景：
#  1. 无限循环
#  2. 可以是已知循环次数，也可以是未知循环次数

# 需求： 1+2+3+..+100
i = 1
sum = 0

while i <= 100:
    sum += i
    i += 1
print(i)  # 输出结果是101，因为i在循环结束后多加了1
print(sum)





# 练习：计算 10 的阶乘 : 1 * 2 * 3 * ...* 10
#   n的阶乘： 1*2*3*..*n

n = 10
result = 1

while n > 0:
    result *= n
    n -= 1

print(result)

# 练习2：求1~100之间的能被6整数的数的和

i = 1
sum = 0
while i <= 100:
    if i % 6 == 0:
        sum += i
    i += 1
print(sum)

# 练习3：求1~100之间的奇数的个数

number = 0  # 奇数的个数
i = 1
while i <= 100:
    if i % 2 != 0:
        number += 1
    i += 1
print(number)


