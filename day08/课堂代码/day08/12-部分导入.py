"""
模块使用部分导入的时候， 可以使用 * 导入模块内容

* 在这里表示通配符 ， 如果没有__all__，这种方式会导入所有不以下划线（_）开头的名称。
如果定义了__all__， 那么使用 * 导入的时候 导入的就是__all__中定义的内容
"""

from utils import *
print(num)
print(A)
print(sub)
print(_age)

import sys
# print(sys.builtin_module_names )
print(*sys.path, sep="\n")