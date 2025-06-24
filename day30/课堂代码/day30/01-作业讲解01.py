"""
根据以下image、kernel矩阵得出第三个矩阵:
image:
[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

kernel:
[[1, 0],
[0, -1]]

result:
[[-5. -5. -5.]
[-5. -5. -5.]
[-5. -5. -5.]]


分析：
   result的结果就是kernel在image上移动得到的结果
"""
import torch

image = torch.tensor([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])

kernel = torch.tensor([[1, 0],
                       [0, -1]])

# 得到imge的宽高
h, w = image.shape
kh, kw = kernel.shape

# 定义result
result = torch.empty((h - kh + 1, w - kw + 1))

# 得到kernel在image上移动时覆盖区域的数据
for row in range(h - 1):
    for col in range(w - 1):
        area_data = image[row:row + 2, col:col + 2]
        # 将area_data和kernel进行逐元素相乘再相加
        dot_result = torch.dot(area_data.flatten(), kernel.flatten())
        result[row, col] = dot_result

print(result)
