from MoKuaiZhongDeTeShuBianLiang import s1

s1.show()

import os

print(os.path.abspath(__file__))     # 获取当前python运行文件的全路径
print(os.path.dirname(__file__))     # 获取当前python运行文件的上一级目录
print(os.path.dirname(os.path.dirname(__file__)))  # 获取当前python运行文件的上一级目录的上一级目录