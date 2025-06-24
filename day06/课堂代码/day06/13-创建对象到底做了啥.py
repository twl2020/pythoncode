"""
创建对象的时候到底做了哪些事情？？

1. 首先调用__new__函数， __new__函数的作用就是创建对象
切记： __new__我们不能显式写出来的


2. 然后调用__init__函数
__init__函数叫做构造函数， 作用是给对象的数据进行初始化操作

以上两个函数都是python解释器自动调用，无需我们调用
"""
class Student:
    name = "zhangsan"
    age = 18

    def __init__(self):
        print("init----------------------")


stu = Student()
# print(stu)

