"""
面向对象的三大特性：
  1. 封装
  2. 继承
  3. 多态


封装就类似于生活中的打包
1. 找个箱子将需要打包的东西装起来
2. 封口 -- 安全性， 也就是不能让东西露出来

什么是封装：
   1. 定义类， 类中编写需要封装的代码（变量、函数）
   2. 不能向外暴露出来的代码使用私有修饰
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_person(self):
        print(f"name:{self.__name}, age:{self.__age}")

