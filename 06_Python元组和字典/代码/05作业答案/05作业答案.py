
# 作业

# 已知列表 names = ['jeff','rain','jack','lucy','lance','feifei']
# a.往names列表里feifei前面插入一个alex
names = ['jeff','rain','jack','lucy','lance','feifei']

names.insert(names.index('feifei'),'alex')
print()

# b.把lucy的名字改成中文：路西
names[names.index('lucy')] = '路西'
print(names)


# c.往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
names.insert(names.index('rain') + 1, ['oldboy', 'oldgirl'])
print(names)

# d.返回lance的索引值
names.index('lance')
print(names.index('lance'))

# e.创建新列表["佩奇", "喜羊羊"],合并入names列表
new_list = ["佩奇", "喜羊羊"]
names.extend(new_list)
print(names)
names = names + new_list
print(names)

# f.取出names列表中索引4-7的4个元素
names[4:7]
print(names[4:7])

# g.取出names列表中索引2-10的5个元素，步长为2
print(names[2:10:2])

# h.取出names列表中最后3个元素
print(names[-3:])
names[-3:]

# I.循环names列表，打印每个元素和索引值，如果索引值为偶数时，把对应的元素改成-1
for i in range(len(names)):
    print(i, names[i])
    if i % 2 == 0:
        names[i] = -1

for i,n in enumerate(names):
    if i % 2 == 0:
        n = -1
    print(i,n)

