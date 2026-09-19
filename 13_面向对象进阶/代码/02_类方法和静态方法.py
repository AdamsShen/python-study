
# 类：
#    属性：类属性，对象属性，私有属性
#    方法：对象方法，私有方法， 类方法，静态方法

class Person:

    age = 30 # 类属性

    def __init__(self, name, age):
        self.name = name  # 对象属性
        self.__age = age  # 私有属性

    # 对象方法/成员方法
    def run(self):
        print('running')
        print(self.name)
        print(self.age, Person.age)
        self.__sleep()

    # 私有方法
    def __sleep(self):
        print('sleeping')

    # 类方法: (掌握)
    # @classmethod
    #    1.类方法可以用类名来调用（推荐），也可以用对象来调用
    #    2.类方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用类方法，可以节省内存
    #    3.类方法中有cls,没有self,表示可以去调用类名能调用的，不能调用(对象属性，对象方法，私有属性，私有方法)
    #      cls可以调用类属性，其他类方法，静态方法
    #    4.类方法 可以传递其他参数
    @classmethod
    def eat(cls):   # cls: class
        print('eat')
        print(cls.age)
        print(cls == Person)

    # 静态方法:（了解）
    # @staticmethod
    #    1.静态方法可以用类名来调用（推荐），也可以用对象来调用
    #    2.静态方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用静态方法，可以节省内存（类名来调用）
    #    3. 既没有cls，也没有self，静态方法内部不需要调用类中的任何属性和方法
    #    4.静态方法 可以传递其他参数
    @staticmethod
    def game():
        print('playing')


# 创建对象
p = Person("张三", 18)
# p.run()

Person.eat()
Person.game()  # playing，使用类名调用静态方法



# 类方法: (掌握)
# @classmethod
#    1.类方法可以用类名来调用（推荐），也可以用对象来调用
#    2.类方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用类方法，可以节省内存
#    3.类方法中有cls,没有self,表示可以去调用类名能调用的，不能调用对象属性，对象方法，私有属性，私有方法
#      cls可以调用类属性，其他类方法，静态方法

# 静态方法:（了解）
# @staticmethod
#    1.静态方法可以用类名来调用（推荐），也可以用对象来调用
#    2.静态方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用静态方法，可以节省内存（类名来调用）
#    3. 既没有cls，也没有self，静态方法内部不需要调用类中的任何属性和方法


import datetime
dt = datetime.datetime(year=2023, month=10, day=1)
print(dt.day)  # 1

# 第一个datetime是模块名，第二个datetime是类名，第三个fromtimestamp 是datetime类的静态方法名
datetime.datetime.fromtimestamp()



