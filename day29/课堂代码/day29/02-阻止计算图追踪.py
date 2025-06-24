"""
在模型训练的时候是需要 计算图追踪的
在模型验证阶段或推理阶段是不需要计算图追踪的

主要作用包括：
    1. 节省内存： 在推理阶段，不需要计算梯度，因为模型的参数不再更新。使用 torch.no_grad()
    可以阻止 PyTorch 保存梯度相关的信息，从而减少内存占用。
    2. 避免不必要的计算： 在一些情况下，只需要模型的预测结果而不需要梯度信息。禁用梯度计算可以
    避免进行不必要的计算。
"""
import torch

x = torch.tensor(1., requires_grad=True)
y = x ** 2

with torch.no_grad():
    z = y ** 2

z.backward()
print(x.grad)
