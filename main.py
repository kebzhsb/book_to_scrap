import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

reponse = requests.get(url)

if reponse.ok :
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    title = soup.find("h1").get_text(strip=True)
    description = soup.select_one("#product_description + p").get_text(strip=True)
    category = soup.select_one("ul.breadcrumb li:nth-of-type(3) a").get_text(strip=True)
    
    
    infos = {}
    for tr in soup.find_all("tr"):
        th = tr.find("th").get_text(strip=True)
        td = tr.find("td").get_text(strip=True)
        infos[th] = td
       
        infos["Title"] = title
        infos["Category"] = category
        infos["Description"] = description

    with open("book.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=infos.keys(), delimiter=';')
        writer.writeheader()
        writer.writerow(infos)








    
    

   
