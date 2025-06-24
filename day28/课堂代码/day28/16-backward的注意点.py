"""
backward的注意点:
  在同一个计算图中， backward()只能调用调用一次
  当多个计算图使用相同的叶子节点时， 叶子节点上的导数会累加。 此时需要使用梯度清零

"""
import torch

x = torch.tensor(3, dtype=torch.float32, requires_grad=True)
for i in range(10):
    y = x ** 2
    # if x.grad is not None:
    #     x.grad.zero_()  # 该代码要理解， 但是在深度学习中基本不用， 因为会直接使用优化器的清零方法
    y.backward()
    print(x.grad)