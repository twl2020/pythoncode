"""
为什么需要访问控制？
   目的是隐藏实现的细节，保证代码的安全性

如何隐藏实现的细节， 保证代码的安全性？？
   需要将属性或函数私有化处理

私有化基于相当于生活中的 私有财产，只能在本类中使用，出了类就不能使用
私有属性原则上只能在本类中访问, 因为可以通过  _当前类+私有属性名称 去访问私有属性
虽然如此， 但是我们还是遵守私有的约定， 别人定义了私有属性， 你就不要随便通过  _当前类+私有属性名称 去访问私有属性


私有(private)属性:
   使用双下划线开头（至多一个后缀下划线）的属性，就是私有属性。会被解释器修改为 _当前类+私有属性名称



保护(protected)属性:
    在属性的前面使用一个下划线_开头，表示保护属性。
注意：
    保护成员不会改名，在类外部也可以直接访问。这个仅仅是python程序员之间的不成文规定。
    在python中没有什么属性是访问不到的，但是请遵守这些约定

"""


class Person:
    def __init__(self, name, age):
        # 私有属性
        self.__name = name
        if age > 0:
            self.__age = age
        else:
            self.__age = 18

    # 私有方法
    def __sleep(self):
        print("睡觉")

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age > 0:
            self.__age = age


p1 = Person("张三", -33)
print(p1.name)
p1.set_age(-22)
p1._Person__age = -100
# 动态添加属性, 不是私有的属性， 必须是self.__xx定义的才是私有属性
p1.__age = 33
print(p1.__age)
print(p1.get_age())
print(p1.__dict__)

