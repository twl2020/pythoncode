# 使用模式匹配完成字面值的比较
status = 404
match status:
    case 200:
        print("网络正常")
    # 这里的 | 表示 或的意思
    case 400 | 404 | 500:
        print("程序错误")
    case _:
        print("未知错误")