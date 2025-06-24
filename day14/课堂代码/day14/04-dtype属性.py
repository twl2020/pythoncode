"""
numpy中ndarray的dtype属性的作用： 表示数组中元素的数据类型

numpy中的dtype支持 python的数据类型

np.bool_  boolean类型
np.int8   int8表示1个字节的大小，8就表示8个bit位， 取值范围 -128 -- 127   "b" 或者 "i1"
np.int16  int16表示2个字节的大小   "i2"
np.int32  int32表示4个字节的大小   "i4"
np.int64  int64表示8个字节的大小   "i8"
np.int_   np.int32的缩写

np.uint8   uint8表示1个字节的大小, 没有负数的 ，8就表示8个bit位， 取值范围 0 -- 255  "u1"
np.uint16  uint16表示2个字节的大小   "u2"
np.uint32  uint32表示4个字节的大小   "u4"
np.uint64  uint64表示8个字节的大小   "u8"

np.float16  表示2个字节大小的半精度浮点数  "f2"
np.float32  表示4个字节大小的单精度浮点数  "f4" 或者 “f”
np.float64  表示8个字节大小的双精度浮点数  "f8" 或者 “d”
np.float_   np.float64的缩写       numpy2.0移除

np.object_  表示对象  "O"

u: unsigned 无符号， 也就是没有负数
数据类型的类型代码： 使用字符串的形式表示数据类型，目的就是简写代码

np.string_  表示的是ascii码字符串   "S"
np.unicode_  表示的是unicode码字符串   "U"
<U1:  < 表示小端字节序; U表示unicode_ ; 1表示字符串的最大长度
>U1:  > 表示大端字节序; U表示unicode_ ; 1表示字符串的最大长度
"""
import numpy as np

list01 = [1, 2, 3, 4, 5, 0]
# list01 = [1, 2, 3, 4, 5, 0, "100"]
# list01 = [1, 2, 3, 4, 5, 0, "a"]
arr = np.array(list01, dtype=np.int_)
# arr = np.array(list01, dtype="i4")
# arr = np.array(list01, dtype=np.uint32)
# arr = np.array(list01, dtype="u4")
# arr = np.array(list01, dtype="O")
print(arr.dtype)
print(arr)

print("--------------------------------------------")
list02 = ["aa", "b", "c", "d", "我爱你"]
# arr01 = np.array(list02, dtype=np.string_)
# arr01 = np.array(list02, dtype=np.unicode_)
arr01 = np.array(list02, dtype="U")
print(arr01.dtype)
