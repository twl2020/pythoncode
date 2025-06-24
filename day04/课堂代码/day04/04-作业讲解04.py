"""
给定一个整数列表 nums 和一个整数目标值 target，请在列表中
找出和为目标值的两个整数。
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

1:9 <-->9:1 取其中一个
2:8 <-->8:2
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(nums)
target = 10
for i in range(length):
    for j in range(i + 1, length):
        if nums[i] + nums[j] == target:
            print(nums[i], ":", nums[j])
