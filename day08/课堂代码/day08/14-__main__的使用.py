"""
在Python中，__main__ 是一个特殊的预定义名称，它标识着一个模块是否作为程序的入口点被直接执行.

__main__ 就是程序的入口点

这样的设计非常有用，因为它使得模块既可以作为独立的脚本执行，又可以作为其他模块的一部分被导入使用，
而不会导致其中的某些初始化代码被执行两次。

"""

import my_test as m
m.add(2, 8)