"""
类方法：
   就是在方法定义上面使用装饰器：@classmethod
类方法使用了装饰器，装饰器内部获取了类的信息，并注入这个类给方法的第一个参数


类方法的使用场景：  -- 了解
 1. 工厂方法 -- 创建对象
 2. 修改类属性
"""


class Dog:

    @classmethod
    def eat(cls, food):
        print("吃货", cls, food)


dog = Dog()
"""
被@classmethod修饰的方法就是类方法， 此时使用  对象.类方法()  或者 类.类方法()都会被
解释器自动的转换成 bound method， 那么绑定给第一个参数的是 当前类

"""
print(dog.eat)  # <bound method Dog.eat of <class '__main__.Dog'>>
print(Dog.eat)  # <bound method Dog.eat of <class '__main__.Dog'>>

dog.eat("骨头")
Dog.eat("吃屎")
