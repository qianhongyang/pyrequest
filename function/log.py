import logging
from datetime import datetime
import threading
import function.read_config
import os

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        path = "D:\pyrequest-master\config\\log.ini"
        proDir = function.read_config.ReadConfig.readconfig(path,"log","logdir")
        resultPath = os.path.join(proDir, "result")
        # create result file if it doesn't exist
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test_myself result file name by localtime
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # create test_myself result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined logger
        self.logger = logging.getLogger()
        # defined log level
        self.logger.setLevel(logging.INFO)

        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)

class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log