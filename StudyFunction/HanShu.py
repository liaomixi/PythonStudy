def test(a1):
    a1.append(44)

li = [1,2,3]
test(li)  # python函数调用时传递的是引用，不是传值调用
print(li)

