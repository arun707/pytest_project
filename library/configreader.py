import  configparser

def read_config_data(section , key):
    config = configparser.ConfigParser()
    config.read("./configuration_files/config.cfg")
    return  config.get(section,key)



