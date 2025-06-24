"""
3. 自定义Student类， 创建5个学生对象存储在以上自定义容器中， 完成增删查改操作
"""
from container import MyList


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name:{self.name}, age:{self.age}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.age == other.age
        return False


# 创建5个学生对象
stu01 = Student("米线儿", 23)
stu02 = Student("王炸", 27)
stu03 = Student("蘑菇头", 21)
stu04 = Student("球球", 20)  # 0x001
stu05 = Student("猪小明", 23)
stu06 = Student("台总", 33)

list01 = MyList()
list01.append(stu01)
list01.append(stu02)
list01.append(stu03)
list01.append(stu04)
list01.append(stu05)

print(list01)
del list01[0]

print(list01)

list01[1] = stu06
print(list01)

print(list01[0])

stu04 = Student("球球", 20)  # 0x3001
i = list01.index(stu04)
print(i)
