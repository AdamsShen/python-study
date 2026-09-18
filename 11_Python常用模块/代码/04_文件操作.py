
# 文件操作:
#  1.打开文件
#  2.操作文件(读取read / 写入write)
#  3.关闭文件


# 1.打开文件
# open(file, mode='r')
#   file: 打开的文件路径
#   mode:
#     r : 只读read, 如果文件不存在则报错
#     rb: 只读二进制, 如果文件不存在则报错
#
#     w : 清空写write, 如果文件不存在会自动创建
#     wb: 清空写 二进制, 如果文件不存在会自动创建
#     a : 追加写append, 如果文件不存在会自动创建
#     ab: 追加写二进制, 如果文件不存在会自动创建



# 文件句柄, 文件对象
# 读取
# fp = open('a.txt')  # No such file or directory: 'a.txt'

fp = open('b.txt', 'r', encoding='utf=8')  # 以字符串方式进行读取， 不是二进制方式读取的话都要写encoding
# fp = open('b.txt', 'rb')  # 以二进制方式读取数据 b'1232\r\n3werwer\r\nwerqer\r\n' <class 'bytes'>
str1 = fp.read()
print(str1, type(str1))  # 读取所有内容

# print(fp.readline())  # 一次读一行，会一直往下读行
# print(fp.readline())

# print(fp.readlines())  # 一次读取所有行，放在列表中  ['1232\n', '3werwer\n', 'werqer\n']


# print(fp.read(2))   # 一次读取2个字符  12
# print(fp.read(4))  # 继续往下读取4个字符，换行符也是一个字符


fp.close()
# 写

# fp = open('b.txt', 'w', encoding='utf-8') # 清空写
# fp.write('节课')


# fp = open('b.txt', 'wb') # 清空写
# # fp.write('节课')  # TypeError: a bytes-like object is required, not 'str'
# fp.write('jieke'.encode('utf-8'))

# fp = open('b.txt', 'a', encoding='utf-8') # 追加写
# fp.write('节课\n')
# fp.write('节课\n')
# fp.write('节课\n')

fp = open('b.txt','ab') # 追加写
fp.write('hello 马克'.encode())

fp.close()



# with-as : 会自动关闭文件, 建议这样写，抛异常也会关闭文件
with open('b.txt', 'r', encoding='utf-8') as fp:
    print(fp.read())




