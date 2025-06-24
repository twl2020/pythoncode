import cv2
import numpy as np

# 准备一个黑色的背景
bg = np.zeros((480, 640, 3))

# 绘制多边形 -- 五边形
# 绘制多边形的时候，点位的形状必须是(1, 顶点个数, 2)
pts = np.array([[10, 10], [100, 100], [200, 120], [300, 300], [230, 250]])
print(pts.shape)  # (5, 2)
# cv2.polylines(bg, [pts], True, (0, 0, 255), 3, cv2.LINE_AA)
# pts = pts[np.newaxis, :, :]
# pts = pts[None, :, :]
# pts = pts[None]
# pts = pts[np.newaxis]
pts = np.expand_dims(pts, 0)
# cv2.polylines(bg, pts, True, (0, 0, 255), 3, cv2.LINE_AA)

# 绘制实心的多边形
cv2.fillPoly(bg, pts, (0, 0, 255, cv2.LINE_AA))

cv2.imshow("win", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
