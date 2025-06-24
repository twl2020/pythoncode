import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import model
# 加载测试数据
test_dataset = datasets.MNIST(root="../data", train=False, download=True,
                              transform=transforms.ToTensor())

test_loader = DataLoader(dataset=test_dataset, batch_size=100)

# 创建模型对象
net = model.MnistNet()
# 加载已经训练好的模型参数
net.load_state_dict(torch.load("mnist_net.pt"))
net.eval()

# 定义一个列表， 计算每个类别的图像数量
class_counts = [0 for _ in range(10)]
# 定义一个列表， 计算预测每个类别准确的图像数量
pred_counts = [0 for _ in range(10)]

for images, targets in test_loader:
    # logits得到的是模型输出的每个类别的 分数
    logits = net(images)
    # 通过logits得到预测的类别
    pred = torch.argmax(logits, dim=-1)
    # 使用预测类别和真实类型进行比较， True表示该图像预测正确， False表示预测错误
    correct = pred.eq(targets)

    for i, label in enumerate(targets):
        # 每个类别总的图像数量
        class_counts[label] += 1
        # 每个类别预测正确的总的数量
        pred_counts[label] += correct[i]


# 计算出每个类别的准确率
for i in range(10):
    print(f"{i}类别的准确率: {pred_counts[i] * 100 / class_counts[i]}, {pred_counts[i]} / {class_counts[i]}")

