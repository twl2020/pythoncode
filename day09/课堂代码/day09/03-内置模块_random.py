"""
random模块用于生成伪随机数。

伪随机数: 代码中实现随机数都是伪随机数， 因为随机数是通过程序员设计的算法得到的。
真随机数： 生活中的随机数才是真随机数。

"""

# 导入random模块
import random

# print(dir(random))

# sedd()： 设置随机数的种子
# 随机数是根据随机种子得到的。种子变化，随机数就在变化；种子固定了，得到的随机数就是不变的。
# random.seed(1)

# randint(a, b): 返回[a, b] 范围的一个随机整数
# 注意： 这里的随机函数是前闭后闭的
for i in range(10):
    num = random.randint(1, 10)
    print(num)

print("-----------------------------------------")
# randrange(start, stop, step): 用法和range()函数一样，只是这里返回的是随机数
n = random.randrange(3, 10, 2)
print(n)

print("-----------------------------------------")
# random.random(): 返回[0, 1)之间的随机小数
x = random.random()
print(x)

print("------------------------------------")
# random.uniform(a, b)：返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a 。
y = random.uniform(7, 4)
print(y)

print("----------------------------------")
# random.choice(seq)：从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 IndexError。
s = random.choice("abcd")
print(s)

# random.choices(): 从容器中随机返回k个元素， 然后组成列表
s2 = random.choices("abcd", k=2)
print(s2)

print("------------------------------------")
# random.shuffle(): 洗牌， 随机打乱数据
list01 = [1, 2, 3, 4, 5, 6]
random.shuffle(list01)
print(list01)

print("---------------------------------------")
# random.sample(population, k, *, counts=None)：
# 返回从总体序列中选取的唯一元素的长度为 k 的列表。 用于无重复的随机抽样。
# 没有指定counts的时候是无重复的随机抽样: 就是被抽中的不再放回去
# counts: 表示每个元素可以被采样的次数， 长度必须和population长度一样
list01 = [1, 2, 3, 4, 5, 6]
counts = [1, 2, 3, 1, 1, 1]
res = random.sample(list01, k=5, counts=counts)
print(res)
