import torch
from torch import nn
from torchsummary import summary


class MLP(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer01 = nn.Linear(3, 5)
        self.layer02 = nn.Linear(5, 5)
        self.layer03 = nn.Linear(5, 2)
        self.relu = nn.ReLU()

    def forward(self, data):
        data = self.relu(self.layer01(data))
        data = self.relu(self.layer02(data))
        out = self.layer03(data)
        return out


if __name__ == '__main__':
    net = MLP()
    # input_size：表示特征的数量
    # batch_size：表示批次的大小， 也就是每个批次中的样本数量
    summary(net, input_size=(3,), batch_size=1, device="cpu")
