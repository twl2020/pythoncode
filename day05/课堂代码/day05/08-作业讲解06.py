"""
2. 前 K 个高频元素
nums7 = [2, 3, 1, 2, 3, 3, 3, 4, 4, 4]
前 K 个高频元素: [3, 4]


这道作业题其实就是我们常见的 TopN问题
分析：
  1. 统计出每个数字出现的次数
    {2:2, 3:4, 1:1, 4:3}
  2. 按照次数降序
    {3:4, 4:3, 2:2, 1:1}
  3. 获取前k个结果即可
"""


# 以下的函数是传给key函数的
# 形参是接收列表中的每个元素的
def tuple_sort(t):
    return t[1]


nums7 = [2, 3, 1, 2, 3, 3, 3, 4, 4, 4]
# num_counts = {2:2, 3:4, 1:1, 4:3}
num_counts = {num: nums7.count(num) for num in nums7}
# 字典转list
num_counts = [(k, v) for k, v in num_counts.items()]
# 排序, 列表如果是元组， 默认按照元组的第一个元素升序， 如果想按照元组的其他元素升序， 需要给定key函数
# 列表的每个元素都会应用key函数一次， 也就是说元素有几个， key函数就调用几次
# key函数的返回值就是列表排序的时候比较的值
# 函数当作参数使用的时候是不能带()的
num_counts.sort(key=tuple_sort, reverse=True)
# 获取前 K 个高频元素
k = 2
res = [num for num, _ in num_counts[:k]]
print(res)
