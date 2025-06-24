"""
os.path.isfile(path)：如果 path 是 现有的 常规文件，则返回 True。
os.path.isdir(path)：如果 path 是 现有的 目录，则返回 True。
os.path.exists(path)：判断文件是否存在
os.path.join(path, *paths): 拼接多个路径
os.listdir(): 返回的是当前路径下的内容组成的列表
"""
import os.path

# e = os.path.exists("a.txt")
# print(e)
# b = os.path.isfile("a.txt")
# print(b)
p = "a.txt"
if os.path.exists(p):
    b = os.path.isfile(p)
    print(b)

# os.path.join(path, *paths): 拼接多个路径
p1 = os.path.join("D://a", "b", "c", "hello.py")
print(p1)

# os.listdir(): 返回的是当前路径下的内容组成的列表
path = "D:\code_39\code_40\day10"
files = os.listdir(path)
for f in files:
    print(os.path.join(path, f))
