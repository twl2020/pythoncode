"""
继承中， 子类可以继承父类的非私有信息， 继承是将内容原封不动的继承；但是有时候我们需要将继承的父类的内容进行修改，
此时就需要用到方法的重写。

方法的重写， 也叫做方法覆盖， 就是子类中出现和父类同名的方法

方法的重写作用就是修改从父类继承下来的方法

子类中调用父类的成员使用： super().父类成员
super() 可以理解成表示父类对象


super class: 超类， 父类
"""


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃东西")


# 猫： 具备name,age,color属性
class Cat(Pet):

    # 子类中出现了和父类同名的方法， 这就是方法重写
    def __init__(self, name, age, color):
        # super().xxx  就是访问父类的成员
        # super() 和 super(本类的类名, <first argument>) 是一样的
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age)
        self.color = color

    def eat(self):
        print("猫吃鱼")

    def catch_mouse(self):
        print("抓老鼠")


cat = Cat("波斯猫", 2, "豹纹")
print(cat.name, cat.age, cat.color)

cat.eat()
