"""
再将data.txt数据读取出来存储在dataDic中形式为
"""
with open("data.txt", encoding="UTF-8") as f:
    list01 = list(f)[1:]
    result = {}
    for line in list01:
        split_list = line.split()
        result[split_list[0]] = [int(i) for i in split_list[1:]]
print(result)
