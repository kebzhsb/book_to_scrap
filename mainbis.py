import requests
import csv
from bs4 import BeautifulSoup

accueil_url = "https://books.toscrape.com/"

response = requests.get(accueil_url)

if response.ok :
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

category_list = soup.find("ul", class_= "nav nav-list")
category_links = category_list.find_all("a", href=True)

print(category_links)

# liens des categories trouvé 
