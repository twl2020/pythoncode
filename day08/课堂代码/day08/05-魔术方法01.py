"""
魔术方法：python中以__开头和结尾的方法就是魔术方法
魔术方法是自动调用的， 不需要我们手动调用。
__new__() : 创建对象， 给对象开辟内存空间
__init__(): 构造函数， 给对象数据进行初始化
__str__(): 直接格式化对象或者输出对象的时候，返回的当前对象的文本显示方式
__repr__(): 间接格式化对象或者输出对象的时候，返回的当前对象的文本显示方式
当__str__没有重写的时候， 间接和直接都是调用__repr__()
子类不重写__str__的时候， __str__函数调用的是__repr__()


"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name:{self.name}, age:{self.age}"

    def __repr__(self):
        return f"name===={self.name}, age===={self.age}"


stu = Student("米线儿", 23)
list01 = [stu]
# 直接输出对象
print(stu)
# 间接输出对象
print(list01)
for student in list01:
    # 直接输出对象
    print(student)
