from LeiHeDuiXiang import c1

obj = c1.Bar()
obj.show()


class Test:
    def show(self):
        print(self.name)

o1 = Test()
o1.name = "liaomixi"
o1.show()