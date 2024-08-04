from selenium import webdriver
from selenium.webdriver.common.by import By
#Keep Chrome browser open after running program
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_places = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_places[i].text
    }
    
print(events)

# driver.close()#Only closes a single tab
driver.quit()#Quits entire program, Preferable to the close method
