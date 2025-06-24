"""
OpenCV提供了一种训练方法或预先训练的模型，可以使用cv2.CascadeClassifier()方法读取。预训练的模型位于OpenCV安装的data文件夹中。
步骤：
cv2.CascadeClassifier()或者 load() 加载必要的XML文件
分类器对象.detectMultiScale()方法完成检测，该方法返回检测到的脸部或眼睛的边界矩形。
"""
import cv2

img = cv2.imread("c.jpeg")
# cv2.namedWindow("win", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("win", 480, 640)

# 人脸检测需要级联分类器
# 加载预训练好的模型文件有两种方式：
# a. 就是在构造函数中加载  cv2.CascadeClassifier("xml文件")
# b. 级联分类器对象.load("xml文件")
# classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
# 人脸检测
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# scaleFactor缩放因子必须大于1， 默认值是1.1  一般使用1.1 -- 1.5
# scaleFactor = 1.3  表示图像缩放成： 原图/1.3
# scaleFactor越大， 检测效率很快， 可能会漏检, 误检
# minNeighbors: 表示检测人脸的时候周边6个区域都有人脸特征信息
# minSize: 要求人脸区域大小最低是多少
faces = classifier.detectMultiScale(img_gray, scaleFactor=1.5)
# faces = classifier.detectMultiScale(img_gray, minSize=(300, 300))
if faces is not None:
    for face in faces:
        x, y, w, h = face
        # 绘制矩形
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
