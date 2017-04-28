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

    def my(self):
        print("Test.my")


# 继承
class Te(Test):
    def __init__(self):
        super(Te, self).__init__("liaomixi", 18)   # 调用父类构造方法, 或 Test.__init__(self, "liaomixi", 18)

    # 重写父类中的 show 方法
    def show(self):
        super(Te, self).show()   # 执行父类的show方法。或 Test.show(self)
        print("Te.show")
        self.my()  # 现在 Test , Te , Tt 三个类中都有 my() 方法，但是这里的self就是 Tt 类的 tt 对象，因此调用时会先到Tt类里去找my()方法，找的规则就是下面写的

    def my(self):
        print("Te.my")


# 多重继承，如果父类内有同名方法，就会从左往右找，一条道走到黑。如果多个父类有共同的基类，最后才会到基类里面去找
# __init__() 方法也是像上面这样处理
class Tt(Te, Test):
    css = "中国"      # 静态字段，属于类，通过 Tt.css 访问，也可通过对象访问

    def __init__(self, name):
        self.n = name   # 普通字段，属于对象
    pass

tt = Tt()
tt.show()


