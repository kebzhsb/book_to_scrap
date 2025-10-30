import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

reponse = requests.get(url)

if reponse.ok :
    soup = BeautifulSoup(reponse.text, "html.parser")
    title = soup.find("title")
    print(title)
