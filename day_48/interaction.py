from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep Chrome Open after search
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Webdriver configuration
driver = webdriver.Chrome(options=chrome_options)

#Navigate to wikipedia
driver.get("https://secure-retreat-92358.herokuapp.com/")

#Hone in on the elements using xpath
# total_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # total_articles.click()

# #find element by link texts
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()

# #Find the "Search" <input> by Name
# search = driver.find_element(By.NAME, value="search")

#Search using keyword keys
#search.click()
# search.send_keys("Python", Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fName")
first_name.click()
first_name.send_keys("DrunkOnPower")
last_name = driver.find_element(By.NAME, value="lName")
last_name.click()
last_name.send_keys("Vic")
email_entry = driver.find_element(By.NAME, value="email")
email_entry.click()
email_entry.send_keys("DOP_Vic@gmail.com")

signup_button = driver.find_element(By.XPATH, value="/html/body/form/button")
signup_button.click()
#Close Program after task is done
# driver.quit()