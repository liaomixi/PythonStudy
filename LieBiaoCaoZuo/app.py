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

# 查看某个元素在列表中的出现次数，元素不存在就报错
lst = [1, 2, 3, 4, 1, 1]
print(lst.count(1))

# 查看某个元素在列表中的位置，元素不存在就报错
lst = [1, 3, 4]
print(lst.index(1))

# 向列表中特定位置插入元素
lst = [1, 3, 4]
lst.insert(0, 44)
print(lst)

# 删除列表中的元素，remove(x) , pop()
lst = ["liao", "mi", "liao", "xi"]
lst.remove("liao")  # 只会删除列表中第一个 "liao"
print(lst)

lst.pop()  # 删除列表中最后1个元素
print(lst)

lst.pop(-1) # 如果指定了index，就删除指定index位置的元素
print(lst)

# split() 和 join()
s = "liao mi xi"
lst = s.split(" ") #将字符串 "liao mi xi" 转换为列表 ["liao", "mi", "xi"]
print(lst)

s = ",".join(lst)  # 将列表 ["liao", "mi", "xi"] 转换为字符串 "liao,mi,xi"
print(s)
