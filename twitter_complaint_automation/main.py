from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 50
PROMISED_UP = 3.5
TWITTER_EMAIL = "victory20031@outlook.com"
TWITTER_PASSWORD = "Praise2003.1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        
        self.up = 0 
        self.down = 0
        self.driver = webdriver.Chrome(options=chrome_options)
        
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/16596325205")
        go_button = self.driver.find_element(By.CSS_SELECTOR, value='.start-button a')
        go_button.click()
        
        sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
       
    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")
        
        sleep(2)
        username_entry = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
        username_entry.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        
        sleep(5)
        next_button.click()
        password_entry = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]')
        
        sleep(5)
        password_entry.click()
        password_entry.send_keys(TWITTER_PASSWORD)
        
        sleep(5)
        to_send = self.driver.find_element(By.XPATH, value ='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        to_send.click()
        to_send.send_keys(f"My internet provider is giving subpar speeds, it's giving {self.down} download speed and {self.up} speed, when i paid for {PROMISED_DOWN} download and {PROMISED_UP} upload")
        
        sleep(5)
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()


