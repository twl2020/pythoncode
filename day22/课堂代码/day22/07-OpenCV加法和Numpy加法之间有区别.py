"""
注意 OpenCV加法和Numpy加法之间有区别。
OpenCV加法是饱和运算，而Numpy加法是模运算。
"""
import numpy as np
import cv2

m1 = np.uint8([200])
m2 = np.uint8([100])

# Numpy加法是模运算。
print(m1 + m2)
print(300 % 256)

# OpenCV加法是饱和运算
print(cv2.add(m1, m2))
