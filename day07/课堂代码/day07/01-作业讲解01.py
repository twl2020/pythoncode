"""
1. 编程实现：投100轮色子，每轮投3次， 统计出每轮连续出现6点的次数。

连续出现6点:
  1. 66x
  2. x66

分析：
 1. 投100轮色子 -- 循环100次， 表示轮次
 2. 每轮投3次 -- 循环3次， 表示每一轮次摇色子的次数， 所以这个循环需要嵌套在100次循环内部
 3. 每次获取的色子点数应该是1-6的随机值
 4. 统计66x和x66的出现的次数
"""
import random

# 计数器
count = 0
#  1. 投100轮色子 -- 循环100次， 表示轮次
for epoch in range(101):
    # 定义列表存储每一轮色子的点数
    points = []
    # 2. 每轮投3次 -- 循环3次， 表示每一轮次摇色子的次数， 所以这个循环需要嵌套在100次循环内部
    for i in range(3):
        #  3. 每次获取的色子点数应该是1-6的随机值
        point = random.randint(1, 6)
        points.append(point)
    match points:
        case [6, 6, _]:
            count += 1
        case [_, 6, 6]:
            count += 1

print(count)

print("-----------------------------------------")
count = 0
for epoch in range(101):
    points = [random.randint(1, 6) for i in range(3)]
    match points:
        case [6, 6, _] | [_, 6, 6]:
            count += 1

print(count)
