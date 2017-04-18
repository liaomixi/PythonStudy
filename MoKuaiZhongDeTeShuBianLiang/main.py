from MoKuaiZhongDeTeShuBianLiang import s1

s1.show()

import os

print(os.path.abspath(__file__))     # 获取当前python运行文件的全路径
print(os.path.dirname(__file__))     # 获取当前python运行文件的上一级目录
print(os.path.dirname(os.path.dirname(__file__)))  # 获取当前python运行文件的上一级目录的上一级目录
print(os.path.basename(__file__))    # 获取当前python运行文件的文件名


# 只有执行当前python文件的时候，当前文件的特殊变量 __name__ == "__main__" 才成立


