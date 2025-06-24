import numpy as np

"""
区别：
    np.array(): 如果接收的是ndarray, 也会复制数据产生一个新的ndarray对象
    np.asarray(): 如果接收的是ndarray, 不会产生新的ndarray对象

相同点：
   np.array() 和 np.asarray() 如果传入的是列表或元组， 都会产生新的ndarray对象

"""
list01 = [1, 2, 3, 4, 5]
arr = np.array(list01)


a1 = np.array(arr)

print(arr)
print(a1)
arr[0] = 100
print(arr)
print(a1)


print("---------------------------------------------------")
list01 = [1, 2, 3, 4, 5]
arr = np.array(list01)

a2 = np.asarray(arr)
print(arr)
print(a2)
arr[0] = 300
print(arr)
print(a2)

print(id(arr))
print(id(a2))