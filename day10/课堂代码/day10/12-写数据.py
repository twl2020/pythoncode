"""
写数据的时候，是先将数据写进缓冲区， 然后在将缓冲区的数据写进文件

什么时候才会将缓冲区的数据写进文件？？？
   1. 缓冲区的数据满了
   2. 手动将缓冲区的数据刷写到文件

手动刷写数据： flush()
注意： 调用close()释放文件资源的时候会先自动调用flush()


"""
with open("test/a.txt", mode="w", encoding="UTF-8") as f:
    f.write("abcd\n")
    f.write("1234")
    f.flush()   # 将缓冲区的数据刷写到文件中 ---- 手动放水
    while True:
        pass