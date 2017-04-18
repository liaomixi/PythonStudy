import sys   # 解释器相关在里面
import os    # 系统相关在里面
import time

print(sys.version)  # 获取当前python版本
#print(sys.argv[0])  # 命令行参数

print(os.path.join("/Users/mixi/PycharmProjects/PythonStudy", "main.py", "aa"))  # 拼接路径，自动加上相应操作系统下的路径分割符号
print(os.path.join("/liao", "mi", "xi"))           # 第一个斜杠不能少

# 进度条功能
def view_bar(num, sum):
    rate = int(num / sum * 100)
    r = "\r%d%%" % (rate,)       # \r 代表每次回到当前行的起始位置
    sys.stdout.write(r)          # 输出 r 不自动换行，print() 会自动换行
    sys.stdout.flush()

# if __name__ == '__main__':
#     for i in range(101):
#         time.sleep(1)
#         view_bar(i, 100)



