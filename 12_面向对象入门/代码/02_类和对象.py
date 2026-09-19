
# 类和对象
#   类是对象的抽象，class, 同一类事物的统称
#   对象是类的具体，object, 需要通过类来创建
#
#   类：不占内存
#   对象：占内存，不同对象占不同内存

#   类          对象
#   人          我
#  电脑       你的那台华为电脑
#  华为电脑   你的那台华为电脑
#  男朋友     你的男朋友



# 自定义类
#   所有的类都会默认继承object

class Person(object):
    # 属性：变量，静态的，表示一些特征，比如：名字，年龄，身高，
    # 类属性：一般用类名来调用
    name = 'jack'
    age = 30

    # 方法：初始化方法
    # 1. 作用是用来初始化属性值
    # 2. 会在创建对象时，自动调用
    def __init__(self, name, sex):
        # 对象属性：成员属性，对象来调用
        self.name = name
        self.sex = sex


    # 方法：函数，动态的，表示一些功能，比如：吃，睡，玩，
    def eat(self):
        print(self.name, '正在吃')


# 创建对象
p1 = Person('jack', 'male')
print(p1.name, p1.sex)  # jack male
p1.eat()   # jack 正在吃

print()
p2 = Person('rose', 'female')
print(p2.name, p2.sex)  # rose female
p2.eat()   # rose 正在吃




# 一个类可以创建任意多个对象
# 比如：工厂生产华为手机的模型就是类
#      生产的每一部具体的手机就是一个对象


# 练习
# 1.创建Phone类
#      属性：color, size, price
#      方法：call, play_game, chat

class Phone:
    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price

    def call(self):
        print(self.color, '打电话')
    def play_game(self):
        print(self.color, '玩游戏')
    def chat(self):
        print(self.color, '聊天')

iphone16 = Phone(color='黑色', size=6, price=8000)
print(iphone16.color, iphone16.size, iphone16.price)  # 黑色 6 8000

# 2.小美在朝阳公园溜旺财【注：旺财是狗】
#   类People：
#       属性：姓名 name
#       方法：溜旺财 walk_dog
#            def walk_dog(self, place, dog_name):
#                   小美 在 朝阳公园 溜 旺财


class People:
    def __init__(self, name):
        self.name = name

    def walk_dog(self, place, dog_name):
        print(f'{self.name}在{place}溜{dog_name}')

p = People('小美')
p.walk_dog('朝阳公园', '旺财')