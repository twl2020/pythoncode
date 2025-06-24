import torch
from torch.utils.data import DataLoader

from data import YellowDataset
from torchvision import transforms
from net import Model
from torch import nn, optim
from PIL import ImageDraw


class Trainer:

    def __init__(self):
        # 数据集
        self.train_set = YellowDataset(root="sample", transform=transforms.ToTensor())
        self.test_set = YellowDataset(root="sample", transform=transforms.ToTensor())
        self.train_loader = DataLoader(self.train_set, batch_size=4, shuffle=True)
        self.test_loader = DataLoader(self.test_set, batch_size=1)

        self.net = Model()
        self.bce_loss = nn.BCEWithLogitsLoss(reduction="sum")
        self.mse_loss = nn.MSELoss(reduction="sum")
        self.optimizer = optim.SGD(self.net.parameters(), momentum=0.9)

    def train(self):
        self.net.train()
        # 定义变量， 存储总的训练损失
        train_total_loss = 0
        for image, label, loc in self.train_loader:
            pred_label, pred_loc = self.net(image)
            # 计算损失
            # 二分类的损失
            label_loss = self.bce_loss(pred_label, label)
            # 回归任务的损失
            loc_loss = self.mse_loss(pred_loc, loc)
            # 计算分类和回归的整体损失
            loss = label_loss + loc_loss
            train_total_loss += loss
            # 梯度清零
            self.optimizer.zero_grad()
            # 反向传播
            loss.backward()
            # 更新参数
            self.optimizer.step()

        # 计算平均损失
        train_avg_loss = train_total_loss / len(self.train_set)
        print(train_avg_loss)

    def calc_area(self, box):
        """
        计算矩形的面积
        :param box: 传入的矩形坐标的四元组
        :return: 面积
        """
        lx, ly, rx, ry = box
        # 计算出长宽
        box_len = rx - lx
        box_width = ry - ly
        if box_len <= 0 or box_width <= 0:
            return 0
        return box_len * box_width

    def calc_iou(self, box1, box2):
        # 计算两个box的面积
        box1_area = self.calc_area(box1)
        box2_area = self.calc_area(box2)

        # 计算两个box的交集的面积
        lx, ly = torch.maximum(box1, box2)[:2]
        rx, ry = torch.minimum(box1, box2)[2:]
        inter_box = torch.hstack((lx, ly, rx, ry))
        # 交集的面积
        inter_area = self.calc_area(inter_box)

        # 计算iou
        return inter_area / ((box1_area + box2_area) - inter_area)

    def valid(self):
        self.net.eval()
        test_total_loss = 0
        # 使用验证集或者测试集进行验证
        # 在这里我就使用 训练集演示 验证过程； 你们是不允许的， 你们自己准备测试集数据
        for test_img, test_label, test_loc in self.test_loader:
            p_label, p_loc = self.net(test_img)
            # 计算验证的损失
            test_label_loss = self.bce_loss(p_label, test_label)
            test_loc_loss = self.mse_loss(p_loc, test_loc)
            test_loss = test_label_loss + test_loc_loss
            test_total_loss += test_loss

            if test_label[0].item() == 1:
                # 在验证集中需要计算 iou
                # 计算的就是 test_loc 和 p_loc的iou
                iou = self.calc_iou(p_loc[0], test_loc[0])
                if iou > 0.5:
                    _, _, h, _ = test_img.shape
                    # 绘制真实框和预测框
                    # test_img 是一个tensor, 所以需要转成Image
                    transform = transforms.ToPILImage()
                    img = transform(test_img[0])
                    # 通过img得到画笔
                    draw = ImageDraw.Draw(img)
                    # 在img图像上绘制真实矩形框
                    tx, ty, tx1, ty1 = test_loc[0] * h
                    draw.rectangle((tx, ty, tx1, ty1), outline="blue", width=2)
                    # 在img图像上绘制预测矩形框
                    px, py, px1, py1 = p_loc[0] * h
                    draw.rectangle((px, py, px1, py1), outline="red", width=2)
                    img.show()

        # 计算验证的平均损失
        test_avg_loss = test_total_loss / len(self.test_set)
        print(f"验证损失：{test_avg_loss}")

    def run(self, epoches):
        for epoch in range(epoches):
            self.train()
            self.valid()


if __name__ == '__main__':
    Trainer().run(100)
