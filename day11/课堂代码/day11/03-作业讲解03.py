"""
批量重命名文件
"""
import os


def rename_batch_file(file_path, prefix="zs", start=0):
    # 1. 获取file_path下的所有文件及文件夹
    files = os.listdir(file_path)
    for file in files:
        abs_file = os.path.join(file_path, file)
        if os.path.isfile(abs_file):
            # 文件重命名
            # 1. 获取文件的扩展名
            _, ext_name = os.path.splitext(abs_file)
            # 2. 设置新的文件名
            new_filename = f"{file_path}/{prefix}{start}{ext_name}"
            # 3. 重命名
            os.rename(abs_file, new_filename)
            start += 1
        else:
            # 文件夹, 使用递归获取内容
            rename_batch_file(abs_file)


if __name__ == '__main__':
    rename_batch_file("D://a")
