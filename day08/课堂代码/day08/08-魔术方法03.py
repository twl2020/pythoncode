"""
比较运算符对应的魔术方法：
    ==   对应的魔术方法__eq__()
    >    对应的魔术方法__gt__()
    >=   对应的魔术方法__ge__()
    <    对应的魔术方法__lt__()
    <=   对应的魔术方法__le__()
    !=   对应的魔术方法__ne__()

"""


class Person:

    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age

    # equals 表示相等的意思
    def __eq__(self, other):
        return self.pid == other.pid and self.name == other.name and self.age == other.age


p1 = Person(1111, "张三", 20)
p2 = Person(1111, "张三", 20)
# == 默认比较的是地址值, 但是python内置的数据类型都重写了==底层对应的魔术方法， 变成了比较内容
# is 比较的是地址值
print(p1 == p2)  # False
print(p1 is p2)  # False
