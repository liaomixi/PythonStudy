import logging

# 日志级别严重级（依次递减）：CRITICAL  ERROR   WARNING   INFO   DEBUG

# 同时把log日志打到标准输出和文件里

# 首先创建logger对象, 这个logger对象最好是一个全局变量，整个程序都可以用
LOGGER = logging.getLogger("TEST-LOG")

# 创建handler1对象，主要处理输出到标准输出(屏幕)
handler1 = logging.StreamHandler()
handler1.setLevel(logging.WARNING)

# 创建handler2对象，主要处理输出到文件。只记录error和error级别以上的日志
handler2 = logging.FileHandler("test.log")
handler2.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")

handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

LOGGER.addHandler(handler1)
LOGGER.addHandler(handler2)

# 封装成函数供外面模块使用
def mLog(type, message):
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

mLog("warning", "liao mi xi")


