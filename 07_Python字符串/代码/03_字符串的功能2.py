
# 转义字符 \ : 让有语义的字符失去语义 (掌握)
# \\ 表示一个\
s = 'C:\\user\\xmly'
print(s)

# r'' : 让字符串中有语义的字符失去语义 （掌握）
s = r'C:\user\xmly'
print(s)


# b'' : 字节
# bytes: 字节类型，二进制类型
a = b'hello'
print(a, type(a))

# f'' : f-string
name = "杰伦"
age = 45
salary = 1.4567
# print('大家好，我是杰伦，我今年45，我的年薪1.4567亿')
print(f'大家好，我是{name}，我今年{age}，我的年薪{salary}亿')


# 编码和解码
#  编码: encode() 将 字符串 => 二进制
#  解码: decode() 将 二进制 => 字符串
s = 'hello 中国'
s1 = s.encode('utf-8')
print(s1) # b'hello \xe4\xb8\xad\xe5\x9b\xbd'

s2 = s.encode('gbk')
print(s2) # b'hello \xd6\xd0\xb9\xfa'


s11 = s1.decode()
print(s11)

s22 = s2.decode('gbk')
print(s22)

# ASCII码(了解)
print(ord('A')) # 65
print(chr(65)) # A


# strip() : 去除两边的指定字符(默认去除空格)
s = '   hello    world   '
print(s.strip())

s1 = '-- hello world --'
print(s1.strip('-'))

print(s1.lstrip('-'))
print(s1.rstrip('-'))


# 对齐方式 : 了解
print('hello'.center(40)) #                  hello
print('hello'.ljust(40)) # hello
print('hello'.rjust(40)) #                 hello
print('hello'.center(40, '*')) # ********hello***********
print('hello'.zfill(40)) # 0000000000000000000000000000hello

# 前缀和后缀
print(s.startswith('hello'))
print(s.endswith('world'))

print('hellow'.startswith('hellow'))
print('hellow'.endswith('hellow'))

