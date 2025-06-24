"""
类中直接定义属性， 该属性被该类所有对象所共享。
但是有些属性的值应该是每个对象不同的， 不能直接在类中写死。
比如： 以下Student类的不同对象应该具备不同的name值, 此时name就不应该是类属性，
而应该定义成对象的属性， 对象的属性值就可以是不同的对象使用不同的值

如何将属性设置成对象的属性？？？？
    对象.属性=值  ---> 这就是定义对象的属性
python中对象的属性基本上都是在__init__中定义的


self.属性： 叫做成员属性
self.变量： 叫做成员变量
self.方法： 叫做成员方法
"""

class Student:

    # self代指对象的， 哪一个对象调用该方法，self就表示哪一个对象
    # self仅仅是一个参数名称， 可以任意的标识符
    def __init__(self, name, age):
        self.name = name
        self.age = age

# stu1 = Student()  --> new ---> stu1.__init__()
stu1 = Student("张三", 23)
print(stu1)
# stu2 = Student()  --> new ---> stu2.__init__()
stu2 = Student("李四", 33)
print(stu2)
# 动态添对象的属性， 赋值即定义
# . 点语法， 表示从属关系， 翻译成中文就是 xxxx的
# stu1.name = "lisi"
# stu1.sex = "male"
# print(stu1.sex)
# print(stu2.sex)