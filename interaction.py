from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

time.sleep(5)

first_name = driver.find_elements_by_name("fName")
first_name[0].send_keys("ani")
last_name = driver.find_elements_by_name("lName")
last_name[0].send_keys("de")
email = driver.find_elements_by_name("email")
email[0].send_keys("appbrewary@gmail.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()

# article_count = driver.find_element_by_css_selector("#articlecount a")
# # print(article_count.text)
# # article_count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_elements_by_name("search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
