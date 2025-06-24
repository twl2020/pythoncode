"""
7. 定义一个函数, 求出1 + 2！+ 3！+ 4！+...+20！的结果

以上的需求综合了 累乘 和 累加
"""


def get_factorial_sum(n):
    # 先计算阶乘， 然后再累加阶乘
    factorial = 1
    factorial_sum = 0
    for i in range(1, n + 1):
        factorial *= i
        factorial_sum += factorial

    return factorial_sum


res = get_factorial_sum(3)
print(res)
