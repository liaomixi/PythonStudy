LOGIN = 0
ADMIN = 0

def check_login(func):
    def inner(*args, **kwargs):
        if LOGIN == 0:
            print("请登录！")
        elif LOGIN == 1:
            res = func(*args, **kwargs)
            return res
    return inner

def check_admin(func):
    def inner(*args, **kwargs):
        if ADMIN == 0:
            print("请管理员登录！")
        elif ADMIN == 1:
            res = func(*args, **kwargs)
            return res
    return inner

@check_login
def login():
    print("登录成功！")

@check_login
@check_admin
def admin():
    print("欢迎管理员!")

def main():
    global LOGIN
    global ADMIN

    while True:
        inp = input("1: login; 2: admin >>>> ")
        if inp == "1":
            LOGIN = 1
            login()
            admin()
        elif inp == "2":
            LOGIN = 1
            ADMIN = 1
            login()
            admin()
        LOGIN = 0
        ADMIN = 0

main()