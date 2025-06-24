import matplotlib.pyplot as plt
import numpy as np

students = [
    {'name': '张三', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese':
        80, 'math': 90, 'english': 85},
    {'name': '李四', 'gender': 'male', 'age': 16, 'class': 'class2', 'chinese':
        70, 'math': 85, 'english': 80},
    {'name': '王五', 'gender': 'female', 'age': 15, 'class': 'class3', 'chinese':
        90, 'math': 95, 'english': 90},
    {'name': '赵六', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese':
        75, 'math': 80, 'english': 85},
    {'name': '钱七', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese':
        85, 'math': 90, 'english': 80},
    {'name': '孙八', 'gender': 'male', 'age': 19, 'class': 'class2', 'chinese':
        90, 'math': 95, 'english': 95},
    {'name': '周九', 'gender': 'female', 'age': 18, 'class': 'class3', 'chinese':
        80, 'math': 85, 'english': 80},
    {'name': '吴十', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese':
        60, 'math': 75, 'english': 70},
]


# 学科类
class Subject:
    def __init__(self, name, score):
        """
        构造函数
        :param name: 学科名称
        :param score: 学科分数
        """
        self.name = name
        self.score = score


# 学生类
class Student:
    def __init__(self, name, gender, age, cls, subjects):
        self.name = name
        self.gender = gender
        self.age = age
        self.cls = cls
        self.subjects = subjects


# 将数据封装成对象
student_list = []
for stu in students:
    subjects = [
        Subject("chinese", stu["chinese"]),
        Subject("math", stu["math"]),
        Subject("english", stu["english"])
    ]
    student = Student(stu["name"], stu["gender"], stu["age"], stu["class"], subjects)
    student_list.append(student)


# 1、用饼图统计信息工程学院女生和男生的人数；
def draw_sex_num():
    # 定义字典， 用来记录男生和女生的人数
    sex_counts = {"male": 0, "female": 0}
    for student_obj in student_list:
        sex_counts[student_obj.gender] += 1

    # 绘制饼图
    plt.pie(list(sex_counts.values()),
            labels=list(sex_counts.keys()),
            autopct="%.2f%%")
    plt.show()


# 2、用柱图分析语文成绩优、良、中、差的人数；
def draw_chinese():
    # 定义优、良、中、差的标准
    score_range = {
        "优": (90, 100),
        "良": (80, 89),
        "中": (70, 79),
        "差": (0, 69),
    }
    # 定义变量记录优、良、中、差的人数
    score_counts = {k: 0 for k in score_range}

    # 统计语文成绩优、良、中、差的人数
    for stu_obj in student_list:
        for k, (min_socre, max_score) in score_range.items():
            if min_socre <= stu_obj.subjects[0].score <= max_score:
                score_counts[k] += 1

    # 绘制柱状图
    plt.bar(list(score_counts.keys()), list(score_counts.values()))
    plt.show()


# 3、利用散点图分析语文和英语成绩的相关性；
def draw_chinese_en():
    # 获取语文成绩
    cn_list = []
    # 获取英语成绩
    en_list = []
    for stu_obj in student_list:
        cn_list.append(stu_obj.subjects[0].score)
        en_list.append(stu_obj.subjects[2].score)

    # 绘制散点图
    plt.scatter(cn_list, en_list)
    plt.xlabel("语文")
    plt.ylabel("英语")

    # 皮尔逊相关系数
    # 皮尔逊相关系数: 分析线性关系的
    # 非线性关系的可以使用散点图直观的观察
    x = np.corrcoef(cn_list, en_list)
    print(x)
    plt.show()


# 4、利用折线图分析学生年龄和数学平均成绩的走势图
def draw_age_avgmath():
    # 获取所有年龄
    all_age = [stu.age for stu in student_list]
    # 将年龄去重并升序
    unique_age = np.unique(all_age)
    # 定义字典存储每个年龄对应的数学平均分
    age_avgmath = {uage: 0 for uage in unique_age}
    # 得到每个年龄对应的所有数学成绩
    for uage in unique_age:
        scores = [stu_obj.subjects[1].score for age, stu_obj in zip(all_age, student_list) if uage == age]
        age_avgmath[uage] += np.mean(scores)

    # 绘制折线图
    plt.plot(unique_age, list(age_avgmath.values()))
    plt.show()


if __name__ == '__main__':
    # 图像中显示中文
    plt.rcParams['font.sans-serif'] = "SimHei"

    # 图片中显示符号
    plt.rcParams['axes.unicode_minus'] = False
    # draw_sex_num()
    # draw_chinese()
    # draw_chinese_en()
    draw_age_avgmath()
