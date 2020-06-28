# 索引和切片
s = "python"

# 获取s中位置编号为0的字符
print(s[0])

# 获取字符 p 在字符串中的位置编号
print(s.index('p'))

# 获取2至4之间的字符串，包括开头，不包括结尾
print(s[2:4])

# 获取字符串最前面至4之间的字符串，包括开头，不包括结尾
print(s[:4])

# 获取字符串从位置4开始至字符串末尾之间的字符串，包括开头，包括结尾
d = 4
print(s[d:])

y = "py"
if y in s:
    print(y)

print(len(y))

if y != s:
    print(y)

if y == s:
    print("yes")

s = "liao mi xi "
print(s.strip())  # 去掉字符串前后空格
print(s.split(" "))  # 使用空格分隔字符串，获得1个列表

s = ["liao", "mi", "xi"]
print(".".join(s))  # 使用 句号(.) 连接字符串
