# 文件操作之with处理上下文

# with open("test01", "r+") as f:
#     print(f.read())
#
# # 等价于
#
# f = open("test01", "r+")
# print(f.read())
# f.close()

##############################################################################################################

# with 同时打开多个文件，python2.7 之后才开始支持

with open("test01", "r", encoding="utf8") as f1, open("test02", "w", encoding="utf8") as f2:
    for line in f1:
        new_line = line.replace("liao", "chen")
        f2.write(new_line)

##############################################################################################################








