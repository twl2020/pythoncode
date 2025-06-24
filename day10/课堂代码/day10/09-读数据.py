"""
f.readline()：
从文件中读取单行数据；字符串末尾保留换行符（\n），只有在文件不以换行符结尾时，
文件的最后一行才会省略换行符。这种方式让返回值清晰明确；
只要 f.readline() 返回空字符串，就表示已经到达了文件末尾，
空行使用 '\n' 表示，该字符串只包含一个换行符。

"""
f = open("test/a.txt", mode="rt", encoding="UTF-8")

while True:
    line = f.readline()
    print(line, end="")
    if not line:
        break

f.close()  # 释放资源

# line = f.readline()
# print(line, end="")
# line = f.readline()
# print(line, end="")
# line = f.readline()
# print(line, end="")
