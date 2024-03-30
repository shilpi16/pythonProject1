import configparser
import os

path = "C:\\PycharmProjects"
file_name = os.path.join(path, 'pythonProject1', 'Configurations', 'config.ini')

config=configparser.RawConfigParser()
config.read(file_name)

# As these are static methods, these can be access directly through the classname without creating any objects

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserName():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

