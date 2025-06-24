"""
统计下面字符出现的次数
letters = 'abcdabcdabcdabcefg'
打印出下面的结构:
    a:4
    b:4
    c:4

分析：根据输出结果的结构， 我们应该采用字典存储结果

判断 a 是否在 results中
       不在： 之前没有统计过，这是第一次统计
              results={"a":1}
       在： 说明之前统计过， 获取旧的计数+1 作为新的计数
              results = {"a":2}
"""

# 存储结果的字典


letters = 'abcdabcdabcdabcefg'
# 方式一：
results = {}
for letter in letters:
    if letter in results:
        # 在： 说明之前统计过， 获取旧的计数+1 作为新的计数
        results[letter] = results[letter] + 1
    else:
        # 不在： 之前没有统计过，这是第一次统计
        results[letter] = 1

# 方式二：
results = {}
for letter in letters:
    if letter in results:
        # 在： 说明之前统计过， 获取旧的计数+1 作为新的计数
        results.update({letter: results[letter] + 1})
    else:
        # 不在： 之前没有统计过，这是第一次统计
        results[letter] = 1


# 方式三：
results = {}
for letter in letters:
    if letter in results:
        # 在： 说明之前统计过， 获取旧的计数+1 作为新的计数
        results.update({letter: results[letter] + 1})
    else:
        # 不在： 之前没有统计过，这是第一次统计
        results.update({letter: 1})

# 方式四：
results = {}
for letter in letters:
    # get(key, default): 获取key对应value, 如果key不存在就返回default
    # update({k:v}): k存在就是更新；k不存在就是插入
    results.update({letter: results.get(letter, 0) + 1})

print(results)
