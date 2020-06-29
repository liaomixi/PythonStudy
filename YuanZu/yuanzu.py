t = 1, "liao", [44, 144]   # t 就是1个元组
print(t)

# 元组本身是不支持修改的，但是可以先将元组转换为列表进行修改后，再转换为元组
t = (1, 2, 3)
t = list(t)   # 先将元组转换为列表
t.append(44)
t = tuple(t)  # 再转换为元组
print(t)
print(type(t))

