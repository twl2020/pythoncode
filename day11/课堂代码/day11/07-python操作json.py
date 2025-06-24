"""
json.loads():  将json字符串解析成python对象
json.dumps():  将python的字典或者列表转成json字符串
"""

import json
json_str = '''{
  "id": 1001,
  "name": "张三",
  "married": false,
  "scores": [100, 89, 49, 30],
  "family": {
    "father": "老王",
    "mather": "露西"
  }
}
'''

obj = json.loads(json_str)
print(obj)

d2 = {'id': 1001, 'name': '张三', 'married': False, 'scores': [100, 89, 49, 30], 'family': {'father': '老王', 'mather': '露西'}}
json_str02 = json.dumps(d2, ensure_ascii=False)
print(json_str02)