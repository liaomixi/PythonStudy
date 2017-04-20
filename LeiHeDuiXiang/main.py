# from LeiHeDuiXiang import c1
#
# obj = c1.Bar()
# obj.show()


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

o1 = Test("liaomixi", "18")
o1.show()

print()

o2 = Test("mixi", "20")
o2.show()
