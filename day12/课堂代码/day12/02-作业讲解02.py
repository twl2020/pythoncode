"""
1. 实现一个班级点名器， 要求：
  a. 学生信息存储在json文件中
  b. 点名要求实现随机出现名字
  c. 连续两次出现的名字不能相同
  json格式：
    [
    {"name": "Alice", "id": 1},
    {"name": "Bob", "id": 2}
   ]

分析：
   学生信息存储在json中：
     1.  python中如何表示学生信息???  对象
     2.  将数据保存成json文件  -- json.dump
   点名要求实现随机出现名字  -- 使用random
   连续两次出现的名字不能相同  -- 临时变量

序列化：  就是将对象数据转字节数据的过程
反序列化：就是将字节数据转对象数据的过程
"""

import json
import sys
import random


class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name


class StudentCaller:
    def __init__(self):
        self.__students = []

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.__students.append(vars(student))

        with open("students.json", mode="wt", encoding="UTF-8") as f:
            json.dump(self.__students, f, ensure_ascii=False, indent=4)

    def call_name(self):
        with open("students.json", mode="rt", encoding="UTF-8") as f:
            student_list = json.load(f)
            return random.choice(student_list)


if __name__ == '__main__':
    caller = StudentCaller()
    old_called_name = ""
    print("真术点名系统".center(20, "*"))
    while True:
        print("1. 录入学生信息  2. 点名")
        code = input("请选择：")
        match code:
            case "1":
                uid = input("请输入学号：")
                name = input("请输入姓名：")
                caller.add_student(Student(uid, name))
            case "2":
                while True:
                    called_name = caller.call_name()
                    if old_called_name != called_name:
                        print("被点名的是：", called_name)
                        old_called_name = called_name
                        break
            case _:
                sys.exit(0)
