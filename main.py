from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

max_points = max(article_upvote)
index_of_max_points = article_upvote.index(max_points)
print(article_texts[index_of_max_points])
print(article_links[index_of_max_points])