students = [
    {'name': 'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel': '15300022839'},
    {'name': 'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel': '15300022838'},
    {'name': 'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel': '15300022837'},
    {'name': 'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel': '15300022428'},
    {'name': 'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel': '15300022653'},
    {'name': 'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel': '15300022867'}
]

# 1） 遍历所有的姓名
for student in students:
    print(student["name"])
# 2） 统计不及格学生的个数
# 先获取出score小于60分的student
# 方式一： 使用计数器
student_count = 0
for student in students:
    if student["score"] < 60:
        student_count += 1
print(student_count)

# 方式二： 将score小于60分的student存在容器中， 最终容器的长度就是不及格的人数
list01 = [student for student in students if student["score"] < 60]
print(len(list01))

# 方式三： 将score小于60分的student在容器存储一个1， 最终计算容器中所有1的和
list02 = [1 for student in students if student["score"] < 60]
print(sum(list02))

# 3） 打印所有男生的信息
list03 = [student for student in students if student["sex"] == "男"]
print(list03)

# 4） 求平均分数
list04 = [student["score"] for student in students]
print(sum(list04) / len(list04))
