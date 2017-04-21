# from LeiHeDuiXiang import c1
#
# obj = c1.Bar()
# obj.show()


class Test:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def show(self):
        print("Test.show")


# 继承
class Te(Test):
    def __init__(self):
        super(Te, self).__init__("liaomixi", 18)   # 调用父类构造方法, 或 Test.__init__(self, "liaomixi", 18)

    # 重写父类中的 show 方法
    def show(self):
        super(Te, self).show()   # 执行父类的show方法。或 Test.show(self)
        print("Te.show")

    def test(self):
        print("Te.test")


# 多重继承，如果父类内有同名方法，就会从左往右找，一条道走到黑。如果多个父类有共同的基类，最后才会到基类里面去找
class Tt(Te, Test):
    pass

tt = Tt()
tt.show()



