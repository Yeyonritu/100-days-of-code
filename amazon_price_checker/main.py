from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import lxml
import os
import smtplib

# amazon_url = "https://appbrewery.github.io/instant_pot/"
amazon_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url=amazon_url)
amazon_webpage = response.content
soup = BeautifulSoup(amazon_webpage, "lxml")
item_price_whole = soup.find(name="span", class_="aok-offscreen").get_text()
print(item_price_whole[2:])
float_price = float(item_price_whole[2:])

product = soup.find(name="span", id="productTitle")
product_name = product.getText().strip().split()
to_print = ' '.join(product_name)

if float_price < 120:
    message = f"{to_print} is now below $100 {amazon_url}\n"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], 587) as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(from_addr=os.environ["MY_EMAIL"], to_addrs="yeyonritu@gmail.com", msg=f"Subject: PRICE UPDATE!!!\n\n{message}".encode('utf-8')) 


