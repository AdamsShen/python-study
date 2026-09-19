
# 作用是让 函数可以变成属性的方法来调用
#   1.必须有返回值， 2.没有参数
# @property  # (掌握)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("年龄设置失败")







