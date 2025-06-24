"""
面向对象思想： OOP
   本质： 不停的创建对象， 使用对象完成功能

创建对象是需要根据类来创建的

创建类：
  class 类名:
      定义类成员

创建对象：
   对象名 = 类名()
"""

class Dog:
    name = "旺财"
    age = 20


dog1 = Dog()
dog2 = Dog()
dog1.name = "大黄"
dog2.sex = "公"

print(id(Dog))
print(Dog.name, dog1.age)
print(dog2.name, dog2.age)
print(dog2.sex)
print(dog1.sex)
