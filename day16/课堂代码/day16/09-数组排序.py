"""
np.sort(arr, axis=-1, kind=None, order=None)
    kind排序类型 {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}，默认是'quicksort
    order 排序字段


np.argsort(a, axis=-1, kind=None, order=None): 返回对数组进行排序的索引。


在numpy中只要是 argxxx()的方法或函数， 返回的都是元素对应的索引

"""
import numpy as np

a = np.array([1, 3, 5, 2, 7, 4, 6])
print(a)
b = np.sort(a, kind="mergesort")
print(b)

print("---------------------------")
x = np.array([
    [10, 3, 11],
    [7, 22, 15],
    [11, 15, 3],
])
# y = np.sort(x, axis=0)
y = np.sort(x, axis=1)
print(x)
print(y)
print("==========================")
i = np.argsort(x, axis=1)
print(i)
