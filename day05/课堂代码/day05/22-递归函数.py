"""
递归函数： 函数体中调用函数自身， 这样的函数就是递归函数

实现递归函数的步骤;
1. 定义函数
2. 必须存在结束条件， 否则就是死递归
3. 查找规律

递归函数由 "递" 和 "归" 组成
"递" ： 表示的将功能进行拆分
"归"： 将拆分后的功能的结果合并回来

递归函数的思想： 就是一个复杂的问题分解成若干个小问题， 将这些小问题的结果合并回来得到复杂问腿的结果

"""

# 使用递归实现阶乘
"""
分析：
  1. 定义函数
  2. 结束条件
      0! = 1
      1! = 1
      2!= 1 * 2
      3! = 1 * 2 * 3
      4! = 1 * 2 * 3 * 4
  3. 找规律
     n! = n * (n-1)!
  
"""


def factorial(n):
    if n < 0:
        return NotImplemented
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


res = factorial(-5)
print(res)
