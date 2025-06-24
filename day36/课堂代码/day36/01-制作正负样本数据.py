"""
制作正负样本：
   正样本： 有目标的样本
   负样本： 没有目标的样本

我们需要将正负样本的尺寸设置成：224 * 224
由于背景图像的尺寸不一样， 如果简单的设置成224*224会造成图像被压缩变形， 所以我们这里从采取
填充背景的方式解决图像变形的问题， 一般填充 黑色或灰色
"""

from PIL import Image, ImageOps
import glob
import numpy as np


class Sample:
    def make_sample(self, bg_img_root=None, obj_img_root=None, size=(224, 224)):
        # 加载图像
        img_paths = glob.glob(f"{bg_img_root}/*")
        for i, img_path in enumerate(img_paths):
            bg_img = Image.open(img_path)
            # 获取图像的宽高
            w, h = bg_img.size
            # 获取宽高的最大值
            max_side = max(w, h)
            border_lr = (max_side - w) // 2
            border_ud = (max_side - h) // 2
            # 使用border边框线扩展图像
            # border边框线的顺序是： left, top, right, bottom
            # fill就是边框线填充的颜色
            sampling = ImageOps.expand(bg_img, border=(border_lr, border_ud, border_lr, border_ud), fill=(0, 0, 0))
            # 创建224 * 224的负样本
            sampling = sampling.resize(size)
            # 保存负样本
            sampling.save(f"sample/img_{i}.0.0.0.0.0.png")

            # 制作正样本： 就是在负样本上面加上小黄人
            # 添加小黄人：1. 随机获取小黄人  2. 随机大小  3. 随机坐标
            yellow_id = np.random.randint(1, 21)
            yellow_size = np.random.randint(60, 151)
            yellow_x = np.random.randint(0, size[0] - yellow_size)
            yellow_y = np.random.randint(0, size[0] - yellow_size)

            # 获取小黄人
            yellow_img = Image.open(f"{obj_img_root}/{yellow_id}.png")
            # 随机改变小黄人的尺寸
            yellow_img = yellow_img.resize(size=(yellow_size, yellow_size))
            # 将小黄人粘贴到负样本，得到的就是正样本
            # 小黄人是RGBA带有透明度
            # r, g, b, a = yellow_img.split()
            # sampling.paste(yellow_img, (yellow_x, yellow_y), mask=a)

            # 小黄人是RGBA带有透明度， 所以直接将小黄人当作mask传入， 图像就是RGBA
            sampling.paste(yellow_img, (yellow_x, yellow_y), mask=yellow_img)
            # 保存正样本
            sampling.save(
                f"sample/img_{i}.1.{yellow_x}.{yellow_y}.{yellow_x + yellow_size}.{yellow_y + yellow_size}.png")


if __name__ == '__main__':
    s = Sample()
    s.make_sample("images/bg_pic", "images/yellow")
