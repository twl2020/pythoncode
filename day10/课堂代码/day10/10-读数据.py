"""
从文件中读取多行时，可以用循环遍历整个文件对象（惰性对象）。
这种操作能高效利用内存，快速，且代码简单。
如需以列表形式读取文件中的所有行，可以用 list(f) 或 f.readlines()。

"""
f = open("test/a.txt", encoding="UTF-8")
# for line in f:
#     print(line, end="")

for line in list(f):
    print(line, end="")

f.close()