import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
reversed_movies = []
movie_names = []

for tag in soup.find_all(name='h3', class_='title'):
    reversed_movies.append(tag.text)

movie_names = reversed_movies[::-1]

with open("movies.txt", "x", encoding="utf-8") as f: #"x" because i was writing into the file 

    for movie in movie_names:
        f.write(movie + "\n")



