"""
2. 定义一个函数,实现返回三个数的最大值
"""


def get_max(x, y, z):
    # 第一步： 先比较x和y的大小， 得到最大值
    num_max = x if x > y else y
    # 第二步： 先比较num_max和z的大小， 得到的就是三个数的最大值
    num_max = num_max if num_max > z else z
    return num_max


max01 = get_max(1, 2, 3)
print(max01)
