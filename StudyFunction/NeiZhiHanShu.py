# abs() 取绝对值

##################################################################################################

# all()，any() 函数
n = all([1,2,3]) # 所有传入all()函数的元素都为真就为真，all()函数就返回 True
print(n)

nn = all([0,1,2]) # 所有传入all()函数的元素有一个为假，比如这里的 0 ，all()函数就返回 False
print(nn)

nnn = any([0,1,2]) # 只要有一个元素为真，any()函数就返回 True
print(nnn)


##################################################################################################

# bin()函数接受10进制数转为二进制
# oct()函数接受10进制数转为八进制
# hex()函数接受10进制数转为十六进制

print(bin(5))
print(oct(5))
print(hex(5))


##################################################################################################

# bytes() 函数, 将字符串转化为字节。 str() 将字节转化为字符串

# utf-8 编码，一个汉字占 3 个字节
# gbk编码，一个汉字占 2 个字节

## utf-8
s = "你好"
s1 = bytes(s, encoding="utf8")
print(s1) # 输出：\xe4\xbd\xa0\xe5\xa5\xbd 刚好 6 个字节

print(str(s1, encoding="utf8"))

## gbk
ss = "你好"
ss1 = bytes(ss, encoding="gbk")
print(ss1) # 输出：\xc4\xe3\xba\xc3 刚好 4 个字节

print(str(ss1, encoding="gbk"))


##################################################################################################

# chr() ，ord() 函数，ascii 码与字符相互转换

print(chr(65), type(chr(65)))  # 数字转换为字符
print(ord("A"), type(ord("A")))  # 字符转换为数字

##################################################################################################

# compile() 函数，用来将字符串编译成python代码
# exec() , eval() 函数

s = "print(1234)"

# 编译
r = compile(s, "<string>", "exec")  # 几种编译模式，exec，eval， single

# exec() 执行python代码，没有返回值
exec(r)

# 不编译，直接执行也可以
li = ["1", "2", "3"]
s = "+".join(li)  # 将li转换为字符串 "1+2+3"
ss = "print(%s)" % (s,)
exec(ss)

# eval() 函数，将字符串作为一个表达式执行。有返回值
s = "8*8"
r = eval(s)
print(r, type(r))

##################################################################################################
# divmod() 得到商和余数，主要用于分页功能
# 有97条数据，每页显示10条，需要多少页？
(r, i) = divmod(97, 10)  # r是商，i是余数
if i != 0:
    r += 1
print(r)

##################################################################################################

# isinstance() 判断对象是否是某个类的实例

r = isinstance([1, 2, 3], list)


##################################################################################################
# filter()
# filter(函数名，可迭代的对象)

def f1(a):
    if a > 22:
        return True    # 函数返回True，将元素添加到结果中

ret = filter(f1, [11, 33, 22, 44])
print(list(ret))  # 输出 [33, 44]

# 等价于

f1 = lambda a: a > 22
ret = filter(f1, [11, 33, 22, 44])
print(list(ret))

##################################################################################################
# map()
# map(函数名，可迭代对象)

f1 = lambda a: a + 2
ret = map(f1, [1, 2])
print(list(ret))

# 等价于

def f1(a):
    return a + 2        # 将函数返回值添加到结果中

ret = map(f1, [1, 2])
print(list(ret))

##################################################################################################
# len() 在python3以前的版本只能按 字节方式 进行计数

# 字符方式
s = "你好"
print(len(s))  # 输出 2

# 字节方式
s = "你好"
ss = bytes(s, encoding="utf8")
print(len(ss))  # 输出 6


##################################################################################################
# zip()

l1 = ["liao", 11, 22, 33]
l2 = ["mi", 11, 22]
l3 = ["xi", 11, 22, 33]
r = zip(l1, l2, l3)
print(list(r))  # 输出  [('liao', 'mi', 'xi'), (11, 11, 11), (22, 22, 22)]

##################################################################################################


















