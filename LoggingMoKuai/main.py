import logging


#  只记录 WARNING 以及比 WARNING 更严重的级别的日志
logging.basicConfig(format="%(asctime)s  %(message)s", datefmt="%m/%d/%Y %I:%M:%S", filename="test.log", level=logging.WARNING)
logging.warning("[warning] liao mi xi")
logging.critical("[critical] liao mi xi")
logging.error("[error] liao mi xi")





