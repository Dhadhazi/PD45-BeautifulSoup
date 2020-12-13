from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.li)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")

company_url = soup.select_one(selector="p a")

headings = soup.select(".heading")