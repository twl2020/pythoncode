"""
模块（module）: 模块就是py文件， 文件名就是模块名
模块名需要满足标识符的命名规范

为什么需要模块？？？
1. 使用模块可以实现代码的复用
2. 使用模块可以让不同模块的作者不必担心彼此的全局变量名一样


导入模块；
 完全导入语句：
   - 完全导入：import 模块1,模块n
   - 模块设置别名：import 模块 as 别名


"""
# import utils  # 这种方式是直接使用模块名作为模块对象的名字
import utils as xx  # 这种方式是使用as 后面的名字作为 模块对象的名字
# print(utils)
# print(type(utils))
# print(id(utils))

print(xx.num)
xx.add(10, 10)

a = xx.A()
print(a)
a.show()


