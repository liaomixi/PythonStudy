# 实现注册，登录功能

def login():
    return True

def register():
    return False

if __name__ == '__main__':
    t = input("1: 登录； 2：注册")
    if t == "1":
        login()
    elif t == "2":
        register()
