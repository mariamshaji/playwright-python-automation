from configparser import ConfigParser


#approach 1 
'''config = ConfigParser()
config.read('utils/config.ini')
print(config.get("basic info" , "URL"))
print(config.get("mobile" , "os"))'''


#approach 2- using functions
class ConfigReader:
    def config_reader(self,section,key):
        config = ConfigParser()
        config.read('testData/config.ini')
        return config.get(section,key)


#print(config_reader("basic info" , "URL"))