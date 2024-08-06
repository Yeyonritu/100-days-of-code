from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

sleep(5)
login_button = driver.find_element(By.XPATH, value='//*[@id="o131391810"]/div/div[1]/div/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]/div')
login_button.click()

sleep(5)
google_account = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[2]/div[1]/div[1]')
google_account.click()

sleep(5)
account_button = driver.find_element(By.XPATH, value='//*[@id="credentials-picker"]/div[1]/div[1]')
account_button.click()

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for i in range(100):
    dislike_button = driver.find_element(By.XPATH, value='//*[@id="o131391810"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button/span/span')
    dislike_button.click()
