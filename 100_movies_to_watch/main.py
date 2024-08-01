import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movies_article = soup.find_all(name="h3", class_="title")
movies_r_list = []

for movies in movies_article:
    to_add = movies.getText()
    movies_r_list.append(to_add)
    
movies_list = movies_r_list[::-1]

with open("test.txt", 'w', encoding='utf-8') as file:
    for i in movies_list:
        file.write(i + "\n")
