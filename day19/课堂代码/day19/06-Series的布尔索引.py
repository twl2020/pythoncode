import pandas as pd

data = [11, 12, 13, 14, 15]
s1 = pd.Series(data, index=[*"abcde"])
print(s1)
print(s1[[True, True, False, False, True]])
print("----------------------------")
# print(s1 > 13)
print(s1[s1 > 13])