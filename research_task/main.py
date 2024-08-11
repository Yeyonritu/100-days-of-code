import requests
from bs4 import BeautifulSoup

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdBoFYZL5Zs9EYAPaPahXdsRVLanAfJjubGPK5OJrr1A-2uxw/viewform?usp=sf_link"
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage, "html.parser")
rental_articles = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
addresses_articles = soup.find_all(name="address", attrs={'data-test': 'property-card-addr'})
rental_prices = []
article_links = []
addresses = []

for price in rental_articles:
    to_add = price.getText()[0:6]
    rental_prices.append(to_add)
    
for link in soup.find_all(name='a', class_="StyledPropertyCardDataArea-anchor"):
    article_links.append(link.get('href'))
    
for address in addresses_articles:
    to_add = address.getText().strip()
    addresses.append(to_add)

