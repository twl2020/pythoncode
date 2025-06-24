import json

"""
json.load(文件对象)
json.dump(python数据, 文件对象)
"""


def parse_json_file(json_file):
    """
    解析json文件
    :return:
    """
    with open(json_file, mode="rt", encoding="UTF-8") as f:
        obj = json.load(f)
        print(type(obj))
        print(obj)


def dump_data_json(data):
    """
    将python字典或列表数据保存成json文件
    :param data:
    :return:
    """
    with open("test03.json", mode="w", encoding="UTF-8") as f:
        # ensure_ascii=False 表示内容不转换成ascii
        # indent: 表示缩进
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # parse_json_file("test02.json")

    d1 = {
        "uid": 3001,
        "username": "赵老师",
        "age": 30,
        "scores": [100, 89, 90]
    }
    dump_data_json(d1)
