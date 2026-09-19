
# 作用是让 函数可以变成属性的方法来调用
#   1.必须有返回值， 2.没有参数
# @property  # (掌握)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # gettter方法，用来获取值
    @property
    def age(self):
        return self.__age

    # setter方法，用来设置值
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("年龄设置失败")

# 创建对象
p = Person("张三", 18)
print(p.age)   # 18，调用的是 @property的age方法


p.age = 20   # 调用的是 @age.setter，设置年龄
print(p.age)   # 20，调用的是 @property的age方法，获取年龄








