# import FanShe.s1
#
# FanShe.s1.f1()
#
# # 通过反射方式调用s1中的f1()
# # hasattr（检查） getattr（查找） setattr delattr  这就是几个反射
#
# str = "f1"
# if hasattr(FanShe.s1, str):
#     func = getattr(FanShe.s1, str) # 反射就是利用字符串的形式去对象中操作（查找／检查／删除／设置）相同名字的成员
#     func()
# else:
#     print("no func {:s}".format(str))


########################################################################################################################
########################################################################################################################

# 通过字符串导入指定模块
mn = "s1"
fn = "f1"

obj = __import__(mn)            # 使用字符串导入模块
if hasattr(obj, fn):
    func = getattr(obj, fn)
    func()
else:
    print("no funtion {:s} in module {:s}".format(fn, mn))