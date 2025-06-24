import re

# 按照.将字符进行分割
ip = "192.168.10.11"
# s = re.split("\\.", ip)
s = re.split("[.]", ip)
print(s)


# 按照空格将字符进行分割
info = "welcome   to   cheng      du"
s1 = re.split("\\s+", info)
print(s1)

