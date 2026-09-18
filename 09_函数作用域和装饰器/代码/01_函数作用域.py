
# 作用域：变量起作用的范围
#   函数有作用域

# 全局作用域,全局变量，默认不会释放内存
a = 10

def func():
    # 局部作用域,局部变量,退出函数时，会自动将变量占用的内存释放掉
    b = 10
    print('b', b)
    print('a', a)

func()

# if，while, for语句，没有作用域
if True:
    c = 100

print('c', c)

i = 1
while i:
    d = 100
    i -= 1
print('d:', d)


# 函数嵌套
# 内建作用域 B： Built-in, 整个python环境都可以使用
# 全局作用域 G： Global
# 函数作用域 E： EnClosing
# 局部作用域 L： Local


x = 3 # 全局作用域
def fn1():
    y = 4 # 函数作用域 E: EnClosing 闭包环境（如果存在函数嵌套，中间的变量就是函数作用域）

    def fn2():
        z = 5 # 局部作用域 L: Local

def outer():
    e = 100
    print('e', e)

    def inner():
        f = 100
        print('f', f)
        print('e', e)

    inner()
    print('e', e)


print()
# 关键字： global，nonlocal


# global :全局
m = 10
def f1():
    m = 4
    print('m:', m) # m: 4
f1()
print('函数外的m:', m)   # 函数外的m: 10


print()
m = 10
def f1():
    global m
    m += 4
    print('m:', m) # m: 4
f1()
print('函数外的m:', m)


print()
def outer():
    e = 100
    print('e', e)

    def inner():
        global e   # 声明e为全局变量
        e = 200
        print('e', e)

    inner()
    print('e', e)

outer()
print('outer e', e)



print()
# nonlocal : 声明使用闭包变量, 在函数嵌套时才会使用
e = 10 # 全局作用域
def outer():
    e = 100 # 函数作用域
    print('e', e)

    def inner():
        nonlocal e  # 声明e为闭包变量， 声明使用的是函数作用域下的变量
        e = 200
        print('inner e', e)

    inner()
    print('e', e)

outer()
print('outer e', e)
