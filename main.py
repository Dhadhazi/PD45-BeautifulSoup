from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="title")

movie_string = "1) "
for i in range(len(titles)-1, -1, -1):
    movie_string += (titles[i].getText())+"\n"

with open("movies.txt",mode="w") as file:
    file.write(movie_string)