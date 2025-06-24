import model
import torch
from torchvision import transforms
from PIL import Image

# 创建模型对象
net = model.MnistNet()
# 加载已经训练好的模型参数
net.load_state_dict(torch.load("mnist_net.pt"))
net.eval()


# 将图像交给模型，得到类别
# 1. 使用PIL加载图像
img = Image.open("../img/6.jpg")
# 2. 图像预处理
transform = transforms.Compose([
    # 将图像变成单通道
    transforms.Grayscale(),
    # 将图像的尺寸变成 28 * 28
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])

# 3. Compose对象是一个可调用对象， 直接将图像交给它， 就可以得到预处理后的结果
data = transform(img)
# 4. 将预处理后的图像数据喂给模型，得到十个类别的分数
logits = net(data)
# 5. 取出最大分数值的索引就是预测的类别
# cls_pred = torch.argmax(logits)
_, cls_pred = torch.max(logits, dim=-1)
print(cls_pred.item())


