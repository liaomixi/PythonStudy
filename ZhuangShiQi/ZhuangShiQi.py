def outer(fun):       # fun就等于 show 或 test
    def inner(*args, **kwargs):
        print("before")
        ret = fun(*args, **kwargs)         # 这里就是执行 show() 函数内的语句，并处理原函数返回值
        return ret

    return inner

# @ + 函数，装饰器
# 功能：
# 1。自动执行outer函数并且将其下面的函数名show当作参数传递，相当于 执行 outer(show)
# 2。将outer函数的返回值，重新赋值给show，这里就是 show = inner，相当show函数变成了inner，后面再调用show函数就是调用inner函数了

@outer
def show(arg = None):
    print("show()")
    return arg

@outer
def test(arg = None):
    print("test()")
    return arg


print(show("SSSS"))  # 这里执行show()就相当于执行 inner() 函数
print()
print(test("TTTT"))
