"""
3、学生信息
1) 封装Student类，包含属性name、age、tel、score、sex，包含方法getScore(打印name、
score)、 getStudent（打印个人的全部信息）。
2) 使用list列对象，存储5个学生对象，迭代所有学生信息。
3) 打印不及格学生信息以及统计不及格学生数量

"""


class Student:
    def __init__(self, name, age, tel, score, sex):
        self.name = name
        self.age = age
        self.tel = tel
        self.score = score
        self.sex = sex

    def getScore(self):
        print(f"name={self.name}, score={self.score}")

    def getStudent(self):
        print(f"name={self.name},age={self.age},tel={self.tel}, score={self.score}, sex={self.sex}")


stu1 = Student("蘑菇头", 22, 212, 30, "男")
stu2 = Student("球球", 18, 112, 45, "女")
stu3 = Student("王炸", 23, 232, 30, "男")
stu4 = Student("猪小明", 21, 131, 30, "男")
stu5 = Student("冷萌", 20, 212, 30, "女")

students_list = [stu1, stu2, stu3, stu4, stu5]

for student in students_list:
    student.getStudent()


print("-----------------------------------------------")
# 打印不及格学生信息以及统计不及格学生数量
count = 0
for student in students_list:
    if student.score < 60:
        count += 1
print(count)

print("-----------------------------------------------")
# 打印不及格学生信息以及统计不及格学生数量
res = filter(lambda stu: stu.score < 60, students_list)
print(len(list(res)))

