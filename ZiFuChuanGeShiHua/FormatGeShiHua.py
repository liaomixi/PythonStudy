s = "liao {} is {} good {}".format("mixi", "a", "man")
print(s)

s = "liao {0} is {0} is good {1}".format("mixi", "man")
print(s)

s = "liao {:s} age {:d}".format("mixi", 14)
print(s)
print()

# ===================================================================

s = "{name:s} age is {age:d}".format(name="liaomixi", age=14)
print(s)
print()

# ===================================================================
# 进制转换
s = "{:#x}".format(15)
print(s)

s = "{:b}".format(5)
print(s)
print()

# ===================================================================
# 百分比
s = "{:.2%}".format(0.23456)
print(s)  # 输出 23.46%

# ===================================================================
# 列表处理

li = [1, 2, 3]
s = "is {:d} is {:d} is {:d}".format(*li)
print(s)

li1 = [1, 2, 3]
li2 = ["liao", "mi", "xi"]
s = "{0[2]} {1[2]} {0[1]}".format(li1, li2)
print(s)
