
from base import  initiate_driver

def test_validate_login():

    driver = initiate_driver.start_browser()
    job = driver.find_element_by_name("wpforms[fields][4]")
    job.send_keys("developer")

    driver = initiate_driver.close_browser()





