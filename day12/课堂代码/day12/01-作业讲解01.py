"""
请设计一个函数，分别将训练集图片和测试集图片读取到列表中 :
"""

import glob
import os


def get_data(dir_path, train=True):
    # D://data/**/*.png
    if train:
        sub_path = "train"
    else:
        sub_path = "test"
    files = glob.glob(os.path.join(dir_path, sub_path, "**", "*.png"))
    return files


train_list = get_data(r"D:\data\mnist")
test_list = get_data(r"D:\data\mnist", train=False)

print(train_list)
print("-----------------------")
print(test_list)
