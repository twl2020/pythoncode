"""
统计学校school中两个教室的学生表情, 描述如下:
grade_01 = [{"happy": 10}, {"dispirited": 2}]
grade_02 = [{"happy": 11, "exciting": 12}, {"dispirited": 5}]
school = [grade_01, grade_02]
统计结果为:
{'happy': 21, 'dispirited': 7, 'exciting': 12}
"""

grade_01 = [{"happy": 10}, {"dispirited": 2}]
grade_02 = [{"happy": 11, "exciting": 12}, {"dispirited": 5}]
school = [grade_01, grade_02]
results = {}
# 遍历school得到年级grade
for grade in school:
    # grade是list列表， 再次遍历
    for faces in grade:
        # faces 就是一个一个的字典， 继续遍历字典
        for face, nums in faces.items():
            results.update({face: results.get(face, 0) + nums})


print(results)
