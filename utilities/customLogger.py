import logging
import os

path = "C:\\PycharmProjects"
Logdir_name = os.path.join(path, 'pythonProject1', 'Logs')
Logfull_name = os.path.join(Logdir_name, 'automation.log')

class LogGen:
    @staticmethod
    def loggenerator():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=Logfull_name, mode='a')
        formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
