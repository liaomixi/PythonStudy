# json只能支持基本数据类型序列化

import json

# 1次
# 4次
dic1 = {'k1': 123}

print(dic1, type(dic1))

# 将python基本数据类型转换为字符串类型，也称为序列化
res = json.dumps(dic1)

print(res, type(res))

# 将字符串转换为python基本类型，也称为反序列化
dic1 = json.loads(res)

print(dic1, type(dic1))
print(dic1['k1'])
