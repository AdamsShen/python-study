#构造方法：初始化方法，在创建对象时自动被调用
#  __init__
#析构方法：在对象销毁时自动被调用（了解）
#__del__

#魔法方法：双下划线的方法

class Person:
    # 构造方法
    def __init__(self, name):
        print("构造方法被调用，在对象创建时会自动调用！")
        self.name = name

    # 析构方法
    def __del__(self):
        # 在这里可以写一些资源释放的代码
        print("析构方法被调用，对象销毁时会自动调用！")


p = Person("张三")  # 构造方法被调用，在对象创建时会自动调用！

from time import sleep
sleep(3)

del p  # 析构方法被调用，对象销毁时会自动调用！


from time import sleep
sleep(3)
print('end')

