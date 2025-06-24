import torch.optim

import data
import model
import torch.nn as nn
import tqdm


# 运行设备, 模型和数据必须在相同的设备上
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# 获取到训练数据和验证数据
train_loader, valid_loader = data.get_tarin_valid(root="../data")
# 得到模型
net = model.MnistNet().to(device)
# 定义损失函数
loss_fn = nn.CrossEntropyLoss(reduction="sum")
# 创建优化器对象
optimer = torch.optim.Adam(net.parameters())
# 定义超参数
eopches = 1000

# 定义一个初始化的损失， 用来比较损失保存模型
min_valid_loss = torch.inf

for epoch in tqdm.tqdm(range(eopches)):
    # 定义一个变量， 保存训练集的总损失
    total_train_loss = 0
    # 定义一个变量， 保存验证集的总损失
    total_valid_loss = 0

    # 训练
    net.train()  # 表示模型进入训练模式， dropout, BN才能起效果
    for images, targets in train_loader:
        images = images.to(device)
        targets = targets.to(device)
        # 使用模型进行前向传播
        pred = net(images)
        # 计算损失
        loss = loss_fn(pred, targets)
        total_train_loss += loss
        # 梯度清零
        optimer.zero_grad()
        # 反向传播计算梯度
        loss.backward()
        # 更新参数
        optimer.step()

    # 计算训练数据的总体的平均损失
    avg_train_loss = total_train_loss / len(train_loader.sampler)

    # 训练一轮就验证一次
    net.eval()  # 表示模型进入评估模式， 此时dropout不起作用， BN计算也不一样
    with torch.no_grad():
        for valid_imgs, valid_targets in valid_loader:
            valid_imgs = valid_imgs.to(device)
            valid_targets = valid_targets.to(device)
            valid_pred = net(valid_imgs)
            # 计算模型在验证集上的损失
            valid_loss = loss_fn(valid_pred, valid_targets)
            total_valid_loss += valid_loss

    # 计算验证数据的总体的平均损失
    avg_valid_loss = total_valid_loss / len(valid_loader.sampler)
    # 保存模型的条件： 验证集的损失比前一轮小，就保存模型
    if avg_valid_loss < min_valid_loss:
        print(
            f"保存模型：avg_train_loss：{avg_train_loss}, "
            f"min_valid_loss:{min_valid_loss},"
            f" avg_valid_loss:{avg_valid_loss}")
        # 保存模型
        torch.save(net.state_dict(), "mnist_net.pt")
        # 将当前轮的损失赋值给min_valid_loss
        min_valid_loss = avg_valid_loss
