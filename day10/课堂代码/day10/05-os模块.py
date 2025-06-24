"""
路径path： 就是用来定位资源
    计算机中路径分为： 绝对路径，相对路径

绝对路径：直接使用该路径就可以定位到资源，那么这个路径就是绝对路径
常见的绝对路径：
     以盘符开头的路径：D://code_39/code_40/day10/01-异常的演示.py
     以网络协议开头的路径：http://www.baidu.com

弊端：移植性比较差

相对路径：不能直接定位到资源的， 必须借助参照路径才能定位资源， 这样的路径就是相对路径。
参照路径：就是当前文件所在路径

相对路径： 01-异常的演示.py
参照路径： D://code_39/code_40/day10
D://code_39/code_40/day10/01-异常的演示.py

"""

import os

# os.mkdir(path): 创建一个名为 path 的目录。只能创建单级目录。
# test  相对路径
# D://code_39/code_40/day10 参照路径
# D://code_39/code_40/day10/test
# os.mkdir("test")

# os.makedirs(name)：递归目录创建函数，创建多级目录。
# os.makedirs("test/a")

# os.rmdir(path)：移除（删除）空目录 path。
# 如果目录不存在或不为空，则会分别引发 FileNotFoundError 或 OSError。
# os.rmdir("test")

# os.removedirs(name)：递归删除空目录。
# 递归删除多级空目录的时候，path路径需要指定到最里面一层路径， 然后删除的时候会从里向外递归删除
# os.removedirs("test/a")


# os.remove(path)：移除（删除）文件 path。 如果 path 是目录，则会引发 OSError。
os.remove("a.txt")



