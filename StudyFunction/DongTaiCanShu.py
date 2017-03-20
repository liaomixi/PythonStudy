# 动态参数，一个 *，形参args是一个元组
def show(*args):
    print(args, type(args))

show("liao", "mi", "xi")

li = [1, 2, 3]
show(li)  #将li列表作为一个元素
show(*li) #相当于将li里的元素直接赋值给args


# 动态参数，两个 *，形参args是一个字典
def test(**args):
    print(args, type(args))


test(n1=1, n2=2)

dic = {"1":"liao", "2":"mi"}
test(n=dic)
test(**dic) #相当于将dic里的元素直接赋值给args

##########################################################

# 万能参数
def all(*args, **kwargs):   # 两个 * 的形参只能放最后
    print(args)
    print(kwargs)

all(1, 2, 3, k1="1", k2="2")   # 元素1，2，3放入args，元素k1="1", k2="2"放入kwargs




