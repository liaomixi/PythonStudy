import sys
print(sys.getdefaultencoding())  # 获取当前环境的默认编码格式

# python3 中所有的字符串都是Unicode字符串
# 获取字符 Q 的编码是多少
n = ord("Q")
print(n)

# 码值转换为字符
s = chr(n)
print(s)


