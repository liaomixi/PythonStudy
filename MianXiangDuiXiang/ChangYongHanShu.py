# python中一切皆对象

# 判断1个对象是否可迭代
s = "liaomixi"
i = 44
if hasattr(s, "__iter__"):
    print("yes")

if hasattr(i, "__iter__"):
    print("yes")

# dir(object) 查看对象 object 具有哪些属性和方法
print(dir(s))
