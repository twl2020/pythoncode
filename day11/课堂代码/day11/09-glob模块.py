"""
glob： python内置的一个模块
glob 模块会按照 Unix shell 所使用的规则找出所有匹配特定模式的路径名称，但返回结果的顺序是不确定的。
glob 模块的作用： 就是按照规则查找路径下的文件或文件夹

glob的规则：
  1. *  零个或多个字符 （.开头的文件不能匹配）
  2. ?  1个字符
  3. [abc] a或b和c
  4. [!a] 除了a以外的任意字符
  5. ** 是配合 recursive=True 的时候使用， 用于递归查找

"""

import glob

# list01 = glob.glob("D://a/*a*.txt")
# list01 = glob.glob("D://a/?a?.txt")
# include_hidden=True  要求 python>3.10
# list01 = glob.glob("D://a/*.txt", include_hidden=True)
# 需要得到D://a 下所有的txt, 包括隐藏文件的txt
# list01 = glob.glob("D://a/*.txt") + glob.glob("D://a/.*.txt")
# list01 = glob.glob("D://a/*.txt") + glob.glob("D://a/.[!.]*.txt")

# list01 = glob.glob("D://a/**/*", recursive=True)
list01 = glob.glob("D://a/**/*", recursive=True)
print(list01)