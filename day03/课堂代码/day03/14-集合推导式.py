"""
集合推导式：
    就是将列表推导式中的中括号换成大括号{}
     {操作x的表达式  for  x  in  可迭代对象}

字典推导式：
   就是将列表推导式中的中括号换成大括号{}，元素的构造使用key:value的形式
     {key:value  for  x  in  可迭代对象}


元组没有推导式
"""
list01 = [1, 2, 3, 3, 4, 5, 6]
set01 = {i ** 2 for i in list01}
print(set01)

d1 = {i: i ** 2 for i in list01}
print(d1)
