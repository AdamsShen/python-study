#类属性： 通过类名访问的属性，也可以用对象名访问，但不推荐
#对象属性： 只能通过对象名访问的属性

class Person:
    # 类属性
    sex = '男'
    age= 30

    def __init__(self, name, age):
        # 对象属性
        self.name = name
        self.age = age


p = Person(name='小黄', age=10)
'''
print(p.name)
# print(Person.name)  # AttributeError: type object 'Person' has no attribute 'name'


#类属性的调用， 建议使用类名调用
print(p.sex)  # 男
print(Person.sex) # 男
'''

# 对age操作
print(Person.age) # 30， 只能得到类属性
print(p.age) # 10, 优先访问对象属性

#修改age
Person.age = 40
print(Person.age)  # 类名只能修改类属性age， 40

p.age = 13  # 不管有没有对象属性age，都只修改对象属性age，相当于添加了一个对象属性age
print(p.age, Person.age)  # 13   40

# 总结

# 尽量用 对象 去操作 对象属性
# 尽量用 类名 去操作 类属性


# 扩展（了解）
# 同一个类的类属性，是可以被这个类创建的不同对象共享的（针对可变类型，比如：list)

class Dog:
    likes = ['骨头']

    def __init__(self, name):
        self.name = name
        self.likes2 = ['骨头']

dog1 = Dog('小白')
dog2 = Dog('小黑')


# 修改类属性
Dog.likes.append('米饭')
print(Dog.likes)  # ['骨头', '米饭']
print(dog1.likes)  # ['骨头', '米饭']
print(dog2.likes)  # ['骨头', '米饭']

# 修改对象属性
dog1.likes2.append('米饭')

print(dog1.likes2)  # ['骨头', '米饭']
print(dog2.likes2)  # ['骨头']


