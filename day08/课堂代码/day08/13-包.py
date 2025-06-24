"""
包： package   包其实就是文件夹， 是一个包含了 __init__.py文件的文件夹
如果是多级包， 也就是多层文件夹  包名格式就是  xxx.yyy.zzz
使用.表示包的层级
包下的内容就是模块： 包名.模块名

python中的包必须要有__init__.py文件， 为什么？
   因为包也是模块， 但是包是文件夹， 所以python做了一件事： 将文件夹和__init__.py进行映射
com --> __init__.py
   所以 __init__.py就是包对应的模块文件
"""

import com

print(com.x)
print(com.y)
com.add(2, 5)

print("----------------------------------")

from com import x, y, add

print(x)
print(y)
add(3, 6)

print("----------------------------------")
import com.zs as zs

print(zs.name)

from com.zs import name

print(name)

import com.aa as a

print(a.aa)
