"""
numpy.array():
numpy.arange(): 使用方式和python中的range函数一致
numpy.linspace(): 获取等差数列组成的数组
numpy.logspace(): 获取等比数列组成的数组

"""
import numpy as np

a = np.arange(1, 10, 2)
print(a)

print("-----------------------------")
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None,
#              axis=0):  获取等差数列组成的数组
# start: 起始值  stop: 结束值
# num: 获取的元素个数
# endpoint=True: 包含stop值
# retstep: return step  表示是否将step值（公差）也返回
b = np.linspace(1, 100, num=10, retstep=True)
print(b)

print("-----------------------------")
# logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None,
#              axis=0): 获取等比数列组成的数组
# start: 表示的是以base为底的 起始次方
# stop: 表示的是以base为底的 结束次方
# base: 表示底数
c = np.logspace(1, 5, num=5, base=2)
print(c)