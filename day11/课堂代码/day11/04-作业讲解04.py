"""
将以下数据写入文件
"""
# 定义数据
data = [
    ['path', 'x', 'y', 'w', 'h'],
    ['1.png', '100', '100', '200', '200'],
    ['2.png', '50', '100', '100', '100'],
    ['3.png', '200', '50', '150', '100'],
    ['4.png', '150', '100', '100', '100']
]

with open("data.txt", mode="at", encoding="UTF-8") as f:
    for ele in data:
        print("\t".join(ele), file=f, flush=True)