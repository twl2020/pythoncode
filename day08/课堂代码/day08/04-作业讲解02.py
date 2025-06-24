"""
1. 人体关键点的描述，使用面向对象完成
人有姓名、年龄。根据下面的图形还有很多的关键点landmarks。每一个关键点的描述使用 x, y去
描述。
要求:
创建关键点(创建3个即可), 给person人添加关键点之后。遍历每一个关键点


以后写代码只要有一个东西身上有多个属性， 立马想到封装对象
"""


# 人体关键点类
class LandMark:
    def __init__(self, landmark_id, x, y):
        self.landmark_id = landmark_id
        self.x = x
        self.y = y


class Person:
    def __init__(self, name, age, landmarks):
        self.__name = name
        self.__age = age
        self.__landmarks = landmarks

    def add_landmark(self, landmark):
        if isinstance(landmark, LandMark):
            self.__landmarks.append(landmark)

    def show_landmarks(self):
        for landmark in self.__landmarks:
            print(landmark.landmark_id, landmark.x, landmark.y)


landmark0 = LandMark(0, 100, 200)
landmark1 = LandMark(1, 140, 230)
landmark2 = LandMark(2, 140, 130)
landmark_list = [landmark0, landmark1, landmark2]

person = Person("张三", 33, landmark_list)
person.show_landmarks()

print("---------------------------------")
# 以下代码中LandMark对象是一个匿名对象
person.add_landmark(LandMark(3, 300, 200))
person.show_landmarks()
