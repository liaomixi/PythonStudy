############################
# 打开文件, mac下，command + 鼠标指针移动到函数名上 就可以看函数的源码
# f = open("test01", "r+") # 读写，用的最多，写是覆盖写
# f = open("test01", "w") # 覆盖写
# f = open("test01", "a") # 追加写，文件不存在就创建
# f = open("test01", "ab") # 追加写，以字节的方式
# f = open("test01", "x") # 文件存在就报错，不存在就创建并写文件，python3里面新加功能

# 以字节方式读写文件
# f = open("test01", "ab")
# f.write(bytes("liaomixi", encoding="utf8"))
# f.close()
#
# f = open("test01", "rb")
# data = f.read()
# print(str(data, encoding="utf8"))
# f.close()

f = open("test01", "r+")
f.read(2)    # 2代表读2个字符，文件指针往后移2位，从0开始
print(f.tell())    # 输出为2

f.seek(f.tell())
f.write("4")
f.seek(0)   # 重新将指针调整到文件开始处，以实现读取文件全部内容
print(f.read())
f.close()


############################
# 操作文件


############################
# 关闭文件