import torch
import matplotlib.pyplot as plt

# 设定随机种子以确保结果可复现
torch.manual_seed(0)

# 生成模拟数据
data = torch.randn(100).cumsum(dim=0)  # 生成累积和，模拟时间序列数据
data += torch.arange(1, 101)  # 添加线性增长趋势


# 定义计算 EWA 的函数
def compute_ewa(data, beta=0.9):
    ewa = [data[0]]  # 初始化 EWA 列表
    for i in range(1, len(data)):
        ewa.append(beta * ewa[-1] + (1 - beta) * data[i])
    return torch.tensor(ewa)


# 计算 EWA
beta = 0.9  # 可以调整这个参数看不同效果
ewa_data = compute_ewa(data, beta)

# 使用 Matplotlib 绘图
plt.figure(figsize=(10, 6))
plt.plot(data, label='Original Data', alpha=0.7)
plt.plot(ewa_data, label=f'EWA (β={beta})', linestyle='--')
plt.title('Exponentially Weighted Average (EWA)')
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
