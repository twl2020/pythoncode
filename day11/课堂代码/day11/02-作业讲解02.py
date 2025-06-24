"""
打印文件夹下面的所有目录及文件
"""
import os


def list_all_file(file_path):
    files = os.listdir(file_path)
    for file in files:
        abs_file = os.path.join(file_path, file)
        # 如果是文件夹， 就需要当前文件夹下的内容， 使用递归
        if os.path.isdir(abs_file):
            list_all_file(abs_file)

        # 如果file是文件，直接输出, 当然文件夹也需要输出
        print(file)


if __name__ == '__main__':
    path = "D://a"
    list_all_file(path)
