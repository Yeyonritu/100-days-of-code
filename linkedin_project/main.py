from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3988844039&f_AL=true&geoId=101213860&keywords=python%20developer&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

# sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
# sign_in_button.click()

# # username_login = driver.find_element(By.ID, value="username")
# # username_login.click()
# # username_login.send_keys(os.environ["email"])

# # password_login = driver.find_element(By.ID, value="password")
# # password_login.click()
# # password_login.send_keys(os.environ["password"])

# driver.quit()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the LinkedIn jobs search page
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3988844039&f_AL=true&geoId=101213860&keywords=python%20developer&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

# Wait for the sign-in button to be clickable and click it
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/nav/div/a[2]'))
)
sign_in_button.click()

username_login = driver.find_element(By.ID, value="username")
username_login.click()
username_login.send_keys("gojookkotsu99@gmail.com")

password_login = driver.find_element(By.ID, value="password")
password_login.click()
password_login.send_keys("20riTu03.")

login_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

# save_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/button/span[1]')
# save_button.click()

job_listings = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li data-job-id")
print(len(job_listings))
