"""
在前面读取文件的操作中， 我们 打开文件 --- 读取数据 --- 关闭资源 的流程中
关闭资源是我们手动调用close完成， 这种方式如果我们忘记了close, 就没有是释放资源

此时python中提供with上下文， 将操作文件的代码写在with上下文中， 操作完成后会自动的释放资源

with上下文没有作用域
"""
with open("test/a.txt", encoding="UTF-8") as f:
    for line in f:
        print(line, end="")
