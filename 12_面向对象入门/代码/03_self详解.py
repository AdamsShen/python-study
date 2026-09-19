

# self:
#   1.不是关键字, 只是一个形参，但是建议写self, 不需要给self传值
#   2.self是指向当前类的对象（哪个对象调用函数，则该函数中的self就是这个对象）
#   3.作用是让你可以在函数中调用类中的其他属性或方法
#   4.self可以任意命名，但是建议写self
#   5.self只能在函数中使用，而且需要在类中使用



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('__init__ 函数中的self', id(self))  # 2749774658736

    def eat(self):
        print('狗喜欢吃骨头')
        print('eat函数中的self:',id(self))  # 2749774658736
        self.sleep()

    def sleep(self):
        print('狗喜欢睡觉')
        print('sleep函数中的self:',id(self))

# 创建对象

dog = Dog('旺财', 2)
dog.eat()
print('id(dog)', id(dog)) # 2749774658736
print('-------------------------------------')

dog2 = Dog('大黄', 3)
dog2.eat()
print('id(dog2):', id(dog2))  # 2585280606480

