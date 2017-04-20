# from LeiHeDuiXiang import c1
#
# obj = c1.Bar()
# obj.show()


class Test:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def show(self):
        print(self.n, self.a)


# 继承
class Te(Test):
    def __init__(self):
        super(Te, self).__init__("liaomixi", 18)   # 调用父类构造方法, 或 Test.__init__(self, "liaomixi", 18)

    # 重写父类中的 show 方法
    def show(self):
        super(Te, self).show()   # 执行父类的show方法。或 Test.show(self)
        print("Te show")

    def test(self):
        print("Te test")



o1 = Te()
o1.show()



