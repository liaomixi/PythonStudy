# 字典复制，d1 和 d2 在不同的内存空间内，是真正的复制，修改 d2 不会影响 d1
d1 = {1:"liao", 2:"mi", 3:"xi"}
d2 = d1.copy()
print("d1 id: %d, d2 id: %d" % (id(d1), id(d2)))

# 向字典 d1 添加字典 d2 中的全部健值对
d1 = {1: "liao"}
d2 = {2: "mi", 3: "xi"}
d1.update(d2)
print(d1)

# 清空字典内的键值对，字典对象还在
d = {1: "liao"}
d.clear()
print(id(d))

# 获取字典值 get() 和 setdefault()
# get()
d = {1: "liao"}
print(d.get(2))    # 健 2 不存在，没有获取到值，返回值为 None
print(d.get(2, "mi"))  # 如果字典中不存在健 2 ，就返回默认值 "mi"
d.clear()

# setdefault()
d = {1: "liao"}
d.setdefault(2)  # 健 2 不存在，向字典 d 中新增健值对 {2: None}
print(d)
d.setdefault(2, "mi") # 健 2 存在，不会向字典 d 中新增健值对 {2: "mi"}
print(d)

# 遍历字典，items() keys() values()
d = {1: "liao", 2: "mi", 3: "xi"}
for i in d:
    print("k: %d, v: %s" % (i, d[i]))

for i in d.items():
    key, value = i
    print("k: %d, v: %s" % (key, value))

for i in d.keys():
    print("k: %d, v: %s" % (i, d[i]))

for v in d.values():
    print(v)

# 删除字典中健值对
d = {1: "liao", 2: "mi"}
d.pop(1)
print(d)




