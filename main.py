import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

reponse = requests.get(url)

if reponse.ok :
    soup = BeautifulSoup(reponse.text, "html.parser")
    title = soup.find("h1").get_text(strip=True)
    description = soup.select_one("#product_description + p").get_text(strip=True)
    category = soup.select_one("ul.breadcrumb li:nth-of-type(3) a").get_text(strip=True)
   
    print(title , description , category)
