
from base import  initiate_driver

def test_validate_login():

    driver = initiate_driver.start_browser()
    fname = driver.find_element_by_name("wpforms[fields][2][first]")
    fname.send_keys("arun")

    lname = driver.find_element_by_name("wpforms[fields][2][last]")
    lname.send_keys("dabral")





