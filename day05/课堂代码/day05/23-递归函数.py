"""
有一个很有名的数学逻辑题叫做不死神兔问题:
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问第二十个月的兔子对数为多少？

1  1  2  3  5  8  13  21  34  .....   斐波拉契数列


分析：
1. 规律：
   从第三个月开始， 数据的值就是前两个月数据的和
2. 结束条件
   月份等于1或2的时候， 这时候的兔子数量是最少的，也是不变的

"""


def get_rabbit_num(month):
    if month <= 0:
        return NotImplemented
    if month == 1 or month == 2:
        return 1
    return get_rabbit_num(month - 1) + get_rabbit_num(month - 2)


res = get_rabbit_num(5)
print(res)
