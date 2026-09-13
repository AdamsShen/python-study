''' '''

# 三大结构
# 顺序结构
# 分支结构
# 循环结构

# if分支结构

# Python语言有强制缩进

if True:
    print("True")

# 单分支
# age = int(input('请输入年龄：'))
# if age >= 18:
#     print('恭喜你，成年了!')
# print('end')

# 双分支


# age = int(input('请输入年龄：'))
# if age >= 18:
#     print('恭喜你，成年了!')
# else :
#     print('你还是个孩子!')
# print('end')

# 多分支
#  age范围
#    age<18 : 未成年
#    18~30 : 年轻人
#    30~60 : 中年人
#    age>60 : 老年人

'''
age = int(input('请输入年龄：'))
if age < 18:
    print('未成年')
elif 18 <= age < 30:
    print('的年轻人')
elif 30 <= age < 60:
    print('中年人')
elif 60 <= age < 100:
    print('老年人')
else:
    print('你是一个老年人!')
print('end')
'''




# 练习：
#    输入年龄age，要求输入0~12岁之间
#    0~3 : 婴儿
#    3~6 ： 幼儿
#    6~12 ：儿童

# age = int(input('请输入年龄：'))
# if age < 3:
#     print('未成年')
# elif age <= 6:
#     print('的年轻人')
# elif age < 12:
#     print('中年人')
# print('end')

# 练习2：
#    输入性别sex,判断sex
#    如果sex=='男'：输出王思聪
#    如果sex=='女'：输出刘亦菲
#    否则：输出泰国人

# sex = input('请输入性别：')
# if sex == '男':
#     print('王思聪')
# elif sex == '女':
#     print('刘亦菲')
# else:
#     print('泰国人')



# if嵌套
#   可以在if语句中 再写if
# 比如：有一个女孩，她母亲要给他介绍对象，女孩有几个要求：
#   1.年龄<=30
#   2.身高>=1.75m
#   3.年薪>=20w

# age = int(input('请输入年龄：'))
# height = float(input('请输入身高：'))
# salary = float(input('请输入年薪：'))
#
# if age <= 30:
#     if height >= 1.75:
#         if salary >= 20:
#             print('可以')
#         else:
#             print('年薪不足')
#     else:
#         print('身高不足')
# else:
#     print('年龄不足')

# print('可以')



# if 条件
# bool值隐式判断
if 10:
    print('10')



# 扩展
# 输入2个数，得到较大的数
a = 30
b = 20
if a > b:
    print(a)
else:
    print(b)


# 一行来表示
print(a if a > b else b)


# 练习：
#   input("请说出你的心里话(喜欢/不喜欢):")
#   如果喜欢，输出：小女子无以为报,只有以身相许
#   如果不喜欢，输出：小女子无以为报,只有来世做牛做马报答公子大恩

heart = input("请说出你的心里话(喜欢/不喜欢):")
if heart == '喜欢':
    print('小女子无以为报,只有以身相许')
elif heart == '不喜欢':
    print('小女子无以为报,只有来世做牛做马报答公子大恩')



# 练习：
# 输入一个成绩score,判断这个成绩属于哪个等级
#    score >= 90: A
#    70<= score <90: B
#    60<= score <70: C
#    score < 60 : D
score = int(input("请输入成绩："))
if score >= 90:
    print('A')
elif 70<= score <90:
    print('B')
elif 60<= score <70:
    print('C')
else:
    print('D')


