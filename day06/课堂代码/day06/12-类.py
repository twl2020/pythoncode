"""
面向对象： 就是不停的创建对象，使用对象完成功能的一种思想

如何创建对象：
   创建对象是需要使用类来创建的。

类和对象的区别：
  类： 共性的    --   模板
  对象： 个性的， 具象化的

对象是需要根据类创造出来的， 所以必须先有类才能创建对象

创建类的语法：
   class 类名：
      共性的代码(变量、 函数)

类名使用大驼峰命名


创建对象语法：
  对象名 = 类名()

对象也叫叫做实例， 创建对象也叫做实例化
"""


class Person:
    # 类成员(类中的变量和方法)： 该类的所有对象共享的
    name = "张三"
    age = 20

    def eat(self):
        print("吃饭")


p1 = Person()
p2 = Person()
print(p1)
print(p2)
print(Person)  # <class '__main__.Person'>
print(Person.name)
print(Person.age)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

p1.eat()
p2.eat()
