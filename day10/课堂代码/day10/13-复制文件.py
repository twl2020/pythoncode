"""
复制txt文件：

分析：
  复制文件其实就是一个 读数据  写数据的动作
  1. 读取源数据
  2. 将读取到的数据写到目标文件
"""
with open("test/a.txt", encoding="UTF-8") as src_file:
    with open("D://a.txt", mode="w", encoding="UTF-8") as dest_file:
        line = src_file.readline()
        dest_file.write(line)



