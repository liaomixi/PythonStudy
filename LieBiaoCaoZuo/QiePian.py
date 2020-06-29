lst = ["java", "c++", "python"]

print(lst[-3:-1])
print(lst[:-1])
print(lst[-3:])

print(lst[1:4])

# list[start: end: step]
lst = [1, 3, 5, 6, 7, 8]
print(lst[::2])

lst = [1, 2, 3]
# 列表反转 [1, 2, 3] 变为 [3, 2, 1]
print(lst[::-1])

# 反转字符串
s = "liao"
print("".join(list(reversed(s))))
