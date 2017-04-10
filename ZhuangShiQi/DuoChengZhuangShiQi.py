LOGIN = 0
ADMIN = 0

def check_login(func):
    def inner(*args, **kwargs):

        res = func(*args, **kwargs)
        return res


    return inner


def check_admin():
    pass


def login():
    print("登录成功！")

def admin():
    print("欢迎管理员")


def main():
    global LOGIN
    global ADMIN

    while True:
        inp = input("1: login; 2: admin >>>> ")
        if inp == "1":
            LOGIN = 1
            login()
        elif inp == "2":
            LOGIN = 1
            ADMIN = 1
            admin()


main()