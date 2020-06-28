# 列表是可以修改的数据类型， 字符串不是
lst = ["liao", "xi"]
lst[1] = "mi"
print(lst)

s = "liao"
# s[1] = 'a'  # 无法执行，字符串不能修改
print(s)

# 给列表增加元素
lst = [1, 2]
lst.append(3)
print(lst)

# 给列表增加1个列表
l1 = [1, 2]
l2 = ["liao", "mi"]
l1.extend(l2)
print(l1)