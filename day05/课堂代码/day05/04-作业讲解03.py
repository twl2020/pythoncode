"""
4. 给定列表 nums = [10, 20, 30, 50, 20], 定义一个函数找出给定元素的所有位置

分析：假设我们需要查找的是20的所有位置
1. 遍历列表， 然后将元素和20逐一比较
    相等： 将该元素的索引存储在容器中
    不等： 不存储索引

2. 设计一个函数， 功能为：
  可以查找一个目标值在列表中的所有位置
"""
nums = [10, 20, 30, 50, 20]
pos = []
for i in range(len(nums)):
    if 20 == nums[i]:
        pos.append(i)

print(pos)

print("----------------------------------")


def get_indies(target, src_list):
    # 查找一个目标值在列表中的所有位置
    positions = []
    for i in range(len(src_list)):
        if target == src_list[i]:
            positions.append(i)

    return positions


pos = get_indies(20, nums)
print(pos)
