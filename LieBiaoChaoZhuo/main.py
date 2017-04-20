# 列表切片操作
# li[ start : end : step ]  step默认步长是1，start索引从0开始, 不包括end位置的值
# 或
# li[ start : end ]

li = [1, 2, 3, 4, 5]

print(li[::2])
print(li[::-1])   # 反转列表

print(li[0:2])

print(li[0:-2])   # 这里位置0就是元素 1 ， 位置-2就是元素 4，其实相当于 li[0:3], 因为位置3和-2上的元素都是4






