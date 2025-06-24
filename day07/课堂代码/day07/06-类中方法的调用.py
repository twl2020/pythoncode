"""
python中的函数和方法：
 1. 如果不细分的化， 可以认为函数和方法是一样的
 2. 如果要细分的化：
      函数： 调用的时候   函数名()
      方法： 调用的时候   对象.方法名()

类中定义的带有self参数的函数调用方式：
方式一： 对象.函数名()   ---- python解释器将函数转成 “绑定方法”
方式二： 类.函数名(对象)  ---- 还是普通的函数调用，需要手动传入实参

"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def look_door(self):
        print("看门", self)


# 函数的调用
# max()
# min()

# 方法的调用一
dog = Dog("旺财", 2)
"""
思考： look_door方法定义的时候是有参数self, 但是使用 对象.look_door() 调用的时候却没有传入实参，
      代码也没有报错， 为什么？？？？
      
      原因是： 对象.函数名()的时候， python解释器会将将该函数转成“绑定方法”， 然后将调用的对象绑定给
      函数中的第一个参数(self)
"""
dog.look_door()
print(dog.look_door)  # <bound method Dog.look_door of <__main__.Dog object at 0x000002A291197FD0>>

# 方法的调用二
print(Dog.look_door)  # <function Dog.look_door at 0x000001B113AAB370>
Dog.look_door(dog)
