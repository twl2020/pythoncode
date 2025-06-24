"""
为什么需要继承（继承是用来解决什么问题的）?
   多个类中出现了相同的代码， 就可以将这些相同的代码单独提取成一个类， 然后继承该类即可。

继承不能乱继承，除了满足语法要求外， 还需要符合现实逻辑。
满足  is a（...是...的一种） 的关系才能继承

继承的好处：解决了类中代码的冗余问题， 提高了代码的维护性

继承的语法格式：
   class 类(继承的父类)：
       ...

A类继承B类， 那么A类叫做子类，派生类；  B类叫做父类， 超类
python任何一个类都有一个隐式的父类object
子类只能继承父类非私有的成员
"""


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃东西")

class Cat(Pet):

    def catch_mouse(self):
        print("抓老鼠")


class Dog(Pet):

    def look_door(self):
        print("看门")


cat = Cat("橘猫", 2)
print(cat)
