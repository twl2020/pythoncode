"""
三目运算符：也叫做三元运算符
   语法格式：
      变量 = value_if_true if condition else value_if_false
注意： 三元运算符可以简化 if…else….


一元运算符：~2
二元运算符：+ - * /
"""

# 需求：根据输入的分数，输出及格和不及格
score = int(input("请输入分数："))
if score >= 60:
    print("及格")
else:
    print("不及格")


print("------------------------------")
print("及格") if score >= 60 else print("不及格")
info = "及格" if score >= 60 else "不及格"
print(info)
print("及格" if score >= 60 else "不及格")