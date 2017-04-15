# pickle可以支持复杂对象的序列化，比如类的对象，仅能python使用，python2版本和python3在pickle上可能不通用

import pickle
li = [1, 2, 3]

res = pickle.dumps(li)

res = pickle.loads(res)

print(res)

