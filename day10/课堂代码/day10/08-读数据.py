
f = open("test/words.docx", mode="r", encoding="UTF-8")
# read()：表示读取文件全部内容
# read(9)：表示读取9个字符串

"""
f.read(size) ：
可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象（在二进制模式下）。
 size 是可选的数值参数。省略 size 或 size 为负数时，读取并返回整个文件的内容
 size 取其他值时，读取并返回最多 size 个字符（文本模式）或 size 个字节（二进制模式）。
 如已到达文件末尾，f.read() 返回空字符串（''）。

"""
print(f.read())