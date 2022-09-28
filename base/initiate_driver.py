from selenium.webdriver import Chrome

from  library import configreader

def start_browser():
    global driver
    path = r"C:\driver\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get(configreader.read_config_data("Details" , "app_url"))

    return driver

def close_browser():
    driver.close()
