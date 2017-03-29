def test(a1):
    a1.append(44)

li = [1,2,3]
test(li)  # python函数调用时传递的是引用，不是传值调用
print(li)
print()

#########################################################################
# 全局变量，全局变量在文件内所有位置都可以读
# 如果想修改全局变量，需要用 global 关键字
# 如果全局变量是列表，字典，不用global也是可以修改的。但是不可以重新赋值

NAME = "liaomixi"

def f1():
    global NAME   # global了后再去修改 NAME 才会生效。没有用 global，NAME = 4444是不会生效的
    NAME = 4444
    print(NAME)

def f2():
    print(NAME)

f1()
f2()

