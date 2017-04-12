# 生成器使用函数创造

# 函数中包含 yield 就是一个生成器

def test():
    yield 1
    yield 2
    yield 3

res = test()
print(res)          # 这里不会有任何值输出，只有使用 for 循环迭代 res 的时候才会真正在内存中产生值

res = test()
res1 = res.__next__()     #  获取第一个yield的值
print(res1)

res2 = res.__next__()     #  获取第二个yield的值
print(res2)

#########################################################################################################
# 使用生成器实现 range() 功能

def test1(num):
    start = 0
    while True:
        if start >= num:
            return
        yield start
        start += 1


res = test1(4)   # test1 是一个生成器，执行 test1 函数后它不会在内存中产生0 1 2 3这4个值，只会在下面迭代 res 对象取值的时候，一个一个的产生0 1 2 3
for i in res:
    print(i)