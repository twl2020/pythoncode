import yaml


# yaml.load(): 将yaml文件解析成python对象
# yaml.dump()

def test_load():
    with open("config.yaml", encoding="UTF-8") as f:
        # yaml中是可以写入 代码的
        # FullLoader: 完整加载器， 会加载代码
        # SafeLoader： 安全加载器， 不会执行代码，达到安全效果
        # obj = yaml.load(f, yaml.SafeLoader)
        obj = yaml.safe_load(f)
        print(obj["server.config"]["port"])


def test_dump():
    d1 = {
        "info": {
            "id": 100,
            "max": "老大",
            "nums": [10, 9, 3]
        }
    }

    with open("info.yaml", mode="w", encoding="UTF-8") as f:
        yaml.safe_dump(d1, f, allow_unicode=True)


if __name__ == '__main__':
    # test_load()
    test_dump()
