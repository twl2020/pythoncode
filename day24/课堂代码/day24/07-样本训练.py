"""
训练前， 需要将样本数据制作成数据集
然后将数据集交给模型训练， 得到每个人脸的特征

数据集需要包含哪些信息：人脸的数据和对应的标签
"""
import cv2
import os

import numpy as np


def make_face_dataset(dir_path, classifier):
    """
    制作人脸识别的数据集
    :param dir_path: 样本数据所在文件夹的路径
    :param classifier: 级联分类器
    :return: 返回人脸数据， 标签数据
    """
    # 获取路径下的所有文件及文件夹
    files = os.listdir(dir_path)
    # 循环files, 判断里面的内容是文件还是文件夹
    for file in files:
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            # 是文件夹， 获取路径下的所有文件及文件夹
            make_face_dataset(file_path, classifier)
        else:
            # 是文件， 读取该图像
            img = cv2.imread(file_path)
            # 检测人脸
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(img_gray)
            if faces is not None:
                for x, y, w, h in faces:
                    # 得到人脸数据
                    face_data = img_gray[y:y + h, x:x + w]
                    face_list.append(face_data)
                    # 保存一张脸的数据， 就需要对应保存一个标签
                    lable = file_path.split("\\")[1]
                    # 标签要求是数字类型
                    lable_list.append(int(lable))


if __name__ == '__main__':
    face_list = []
    lable_list = []
    classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    make_face_dataset("data", classifier)

    # 将数据集交给模型(脸部识别器)训练， 提取每张脸的特征， 然后将特征和标签保存成文件
    # 创建脸部识别器对象
    face_recognizer = cv2.face.LBPHFaceRecognizer.create()
    # 使用脸部识别器对象训练数据集
    face_recognizer.train(face_list, np.array(lable_list))
    # 将模型训练好的数据保存成文件, 文件的格式可以txt, json, xml, yaml
    face_recognizer.write("face_recognizer.xml")
