"""
abs(): 得到绝对值
ascii(): 获取ascii码值
bin(): 获取二进制数据
bool(): 将数据转成bool
chr(): 例如： chr(97) 返回字符串 'a'
ord(c): 例如 ord('a') 返回整数 97
dict(): 创建字典
divmod(): 得到商和余数
enumerate(iterable, start=0):
  iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。
  enumerate() 返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。

eval(): 实参是一个字符串, 解析字符串并作为 Python 表达式进行求值.
也就说， eval()函数会将参数字符串当作python代码进行解析求值.

filter(function, iterable): 用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。

hash(): 获取数据的哈希值
help(): 内置的帮助函数，如果实参是其他任意对象，则会生成该对象的帮助页。
hex(): 获取十六进制信息
max()和min()： 获取最大值和最小值
map(function, iterable)： 返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。
round(): 四舍六入五取偶

zip(*iterables,strict=False): 在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。
默认strict=False 是木桶原理
zip() 是延迟执行的：直至迭代时才会对元素进行处理. ---- 惰性的
zip: 拉链

float():
int():
bool():
list():
set():
tuple():
dict():
str():

"""
print(bin(10))
print(f"{10:08b}")
print(bool(0))
print(bool(" "))  # True
print(bool(""))  # False
print(divmod(7, 3))

list01 = [11, 23, 14, 25]
for i, v in enumerate(list01):
    print(i, v)

# point = eval(input("请输入xy坐标："))
# print(point)
# print(point[0])
# print(point[1])

list01 = [11, 23, 14, 25, 30]
it = filter(lambda x: x % 2 == 0, list01)
for e in it:
    print(e)

list01 = [11, 23, 14, 25, 30]
res = map(lambda x: x - 10, list01)
# print(list(res))
print(next(res))

print("-------------------------")
print(round(3.4))  # 3
print(round(4.4))  # 4

print(round(3.5))  # 4
print(round(4.5))  # 4

print(round(3.6))  # 4
print(round(4.6))  # 5

print("-------------------------")
print(round(-3.4))  # -3
print(round(-4.4))  # -4

print(round(-3.5))  # -4
print(round(-4.5))  # -4

print(round(-3.6))  # -4
print(round(-4.6))  # -5

print("-------------------------")
# zip: 默认strict=False 是木桶原理
list01 = [1, 2, 3, 4, 5]
list02 = [11, 12, 13, 14, 15, 16]
zip_list = zip(list01, list02)
for e in zip_list:
    print(e)
