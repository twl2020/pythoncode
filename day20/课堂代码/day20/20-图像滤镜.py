"""
Image.filter(filter)：使用给定的过滤器过滤此图像。
图像滤镜需要使用ImageFilter模块。

Pillow提供了以下一组预定义的图像增强过滤器:
    BLUR（模糊）: 对图像应用模糊效果，降低细节清晰度，使图像看起来更柔和。
    CONTOUR（轮廓）: 强化图像中的轮廓效果，通过强调颜色和亮度变化的边缘来产生线条化的外观。
    DETAIL（细节增强）: 增强图像中的细节部分，使得细小的纹理和结构更加明显。
    EDGE_ENHANCE（边缘增强）: 加强图像中颜色或亮度急剧变化的边缘，使边缘更加突出。
    EDGE_ENHANCE_MORE（更强的边缘增强）: 比EDGE_ENHANCE更强烈地增强图像边缘，效果更为显著。
    EMBOSS（浮雕）: 应用一种效果，使图像看起来像浮雕一样，通过模拟光线从不同角度照射在物体表面上产生的阴影和高光来增加立体感。
    FIND_EDGES（查找边缘）: 识别并突出显示图像中的主要边缘，常用于边缘检测，结果通常是黑白的，仅显示边缘轮廓。
    SHARPEN（锐化）: 增强图像的对比度，特别是边缘和细节部分，让图像看起来更加清晰。
    SMOOTH（平滑）: 减少图像中的噪声和不规则性，通过平均相邻像素的颜色值来达到平滑效果。
    SMOOTH_MORE（更强的平滑处理）: 比SMOOTH更强烈地进行平滑处理，进一步减少图像中的细节和噪点，可能会导致更多的信息损失。
"""

from PIL import Image, ImageFilter

img01 = Image.open("b.jpeg")
# 高斯模糊
# img02 = img01.filter(ImageFilter.GaussianBlur)
img02 = img01.filter(ImageFilter.EMBOSS)
img02.show()
