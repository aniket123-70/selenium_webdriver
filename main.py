from selenium import webdriver

chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documention_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documention_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# bug_link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/h2')
# print(bug_link.text)
event_times = driver.find_element_by_css_selector(".event-widget time")
event_names = driver.find_element_by_css_selector(".event-widget a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
    print(events)

driver.quit()


