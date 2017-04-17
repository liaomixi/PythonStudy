import logging


#  只记录 WARNING 以及比 WARNING 更严重的级别的日志, 非常普通的用法
# logging.basicConfig(format="%(asctime)s  %(message)s", datefmt="%m/%d/%Y %I:%M:%S", filename="test.log", level=logging.WARNING)
# logging.warning("[warning] liao mi xi")
# logging.critical("[critical] liao mi xi")
# logging.error("[error] liao mi xi")


# 同时把log日志打到标准输出和文件里

# 首先创建logger对象, 这个logger对象最好是一个全局变量，整个程序都可以用
LOGGER = logging.getLogger("TEST-LOG")
LOGGER.setLevel(logging.WARNING)

# 创建handler1对象，主要处理输出到标准输出(屏幕)
handler1 = logging.StreamHandler()
handler1.setLevel(logging.WARNING)

# 创建handler2对象，主要处理输出到文件
handler2 = logging.FileHandler("test.log")
handler2.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")

handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

LOGGER.addHandler(handler1)
LOGGER.addHandler(handler2)

# 封装成函数供外面模块使用
def Mlog(type, message):
    if type == "error":
        LOGGER.error(message)
    elif type == "critical":
        LOGGER.critical(message)
    elif type == "warning":
        LOGGER.warning(message)
    elif type == "info":
        LOGGER.info(message)
    elif type == "debug":
        LOGGER.debug(message)



