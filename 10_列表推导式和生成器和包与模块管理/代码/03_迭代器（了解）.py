
# 迭代器Iterator,
# 可迭代对象Iterable
from collections.abc import Iterator, Iterable

# type(): 查看数据类型
# isinstance() : 判断某个变量是否为某个数据类型
print(10, type(10))  # 10 <class 'int'>
print(type(10) == int)  # True
print(isinstance(10, int))  # 判断10是否是整数
print(isinstance(10, (int, float, bool)))  # 判断10是否是，int或者float，bool类型


# 迭代器Iterator (了解)
#    1. 可以使用for循环遍历
#    2. 可以使用next调用
# 可以使用for循环遍历 并且 可以使用next调用 就是迭代器
# '''
print(isinstance(3, Iterator))  # False
print(isinstance(3.14, Iterator))  # False
print(isinstance("hello", Iterator))  # False， 只能for循环
print(isinstance(None, Iterator))  # False
print(isinstance(True, Iterator))  # False
print(isinstance([1,2], Iterator))  # False， 只能for循环
print(isinstance((1,2), Iterator))  # False， 只能for循环
print(isinstance({1:2}, Iterator))  # False， 只能for循环
print(isinstance({1,2}, Iterator))  # False， 只能for循环
print(isinstance((i for i in range(3)), Iterator))  # True，生成器即可以for也可以next
# '''

# 可迭代对象 Iterable
#   1. 可以使用for循环遍历，只要可以for循环 就是 可迭代对象
# '''
print(isinstance(3, Iterable))  # False
print(isinstance(3.14, Iterable))  # False
print(isinstance("hello", Iterable))  # True
print(isinstance(None, Iterable))  # False
print(isinstance(True, Iterable))  # False
print(isinstance([1,2], Iterable))  # True
print(isinstance((1,2), Iterable))  # True
print(isinstance({1:2}, Iterable))  # True
print(isinstance({1,2}, Iterable))  # True
print(isinstance((i for i in range(3)), Iterable))  # True
# '''

# iter() : 可迭代对象 => 迭代器 (了解)，可以将可迭代对象转换为迭代器
n = [1, 2, 3]
n2 = iter(n)
print(n2)  # list_iterator object
print(next(n2))  # 1
print(next(n2))  # 2

# 还原成列表,list() 变成列表
n3 = list(n2)
print(n3)  # [3]


