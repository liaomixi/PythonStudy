############################
# 打开文件, mac下，command + 鼠标指针移动到函数名上 就可以看函数的源码
# f = open("test01", "r+") # 读写，用的最多
# f = open("test01", "w") # 覆盖写
# f = open("test01", "a") # 追加写
# f = open("test01", "ab") # 追加写，以字节的方式
# f = open("test01", "x") # 文件存在就报错，不存在就创建并写文件，python3里面新加功能

# 以字节方式读写文件
f = open("test01", "ab")
f.write(bytes("liaomixi", encoding="utf8"))
f.close()

f = open("test01", "rb")
data = f.read()
print(str(data, encoding="utf8"))
f.close()

############################
# 操作文件


############################
# 关闭文件