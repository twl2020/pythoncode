"""
time模块提供了时间的访问和转换。
"""

import time

# time.time() : 返回以浮点数表示的从 epoch 开始的秒数形式的时间。
# start = time.time()
#
# for i in range(100000000):
#     c = i ** 2
#
# end = time.time()
# print(end - start)


# time.sleep(secs): 调用方线程暂停执行给定的秒数。 该参数可以为浮点数以指定一个更精确的休眠时间。
# print("你吃了吗")
# time.sleep(10)
# print("刚刚吃过了")

# time.gmtime([secs]): 将以自 epoch 开始的秒数表示的时间转换为 UTC 的 struct_time
st = time.gmtime()
print(st)

# time.localtime([secs]): 与 gmtime() 相似转换为当地时间。
lt = time.localtime()
print(lt)

"""
time.strftime(format[, t]): 
转换一个元组或 struct_time 由format格式指定的字符串。
如果未提供 t ，则使用由 localtime() 返回的当前时间。 format 必须是一个字符串。
"""
# strftime ===》 string  format  time  将时间格式化成字符串
# 2025-01-08 15:39:50
# 格式化当前时间
stime = time.strftime("%Y-%m-%d %H:%M:%S")
print(stime)

# 格式化指定的时间
# 指定时间是 2024-01-08 13:39:50
# 传入的元组必须是包含struct_time字段值的元组
stime01 = time.strftime("%Y-%m-%d %H:%M:%S", (2024, 1, 8, 13, 39, 50, 2, 8, 0))
print(stime01)





