
# 私有属性和私有方法   在属性名或方法名前加__即可
# 公有属性和公有方法

class Person:
    def __init__(self, name, age):
        # 公有属性
        self.name = name
        # 私有属性
        # 1、 私有属性只能在类的内部访问
        # 2、 属性名前面需要添加2个下划线
        self.__age = age

    # 公有方法
    def show_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print('年龄设置成功')
        else:
            print('年龄设置失败')
        self.__show_name()  # 调用私有方法

    # 私有方法
    # 1、 私有方法只能在类的内部访问
    # 2、 方法名前面需要添加2个下划线
    def __show_name(self):
       print(self.name)

p = Person('张三', 18)
print(p.name)
# print(p.__age)  # 私有属性，不可以在类的外部访问，会报错 'Person' object has no attribute '__age',
print(p.show_age())  # 18
p.set_age(20)  # 年龄设置成功
print(p.show_age())  #20
# print(p.__show_name())  # 私有方法，不可以在类的外部访问，会报错 AttributeError: 'Person' object has no attribute '__show_name'



# 扩展, 不建议使用，把私有属性当做私有，不建议对象直接使用，不建议使用下面的方式调用
# 特殊
# 可以通过内部的属性调用：_类名__age
# 可以通过内部的方法调用：_类名__show_name()
print(p._Person__age)  # 20
p._Person__show_name() # 调用私有方法, 张三
