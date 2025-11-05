import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url)

if response.ok :
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    
    #Autres infos
    title = soup.find("h1").get_text(strip=True)
    description = soup.select_one("#product_description + p").get_text(strip=True)
    category = soup.select_one("ul.breadcrumb li:nth-of-type(3) a").get_text(strip=True)
    #Recuperer note
    star_tag = soup.find('p', class_='star-rating')
    rating_note = star_tag['class'][1]
    word_to_number = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
    }
    rate = word_to_number.get(rating_note, 0)
    #Recupe Url de l'image
    images = soup.find_all("img")
    for img in images:
        src = img.get("src")
        if src:
            # Completer url de l'image
            img_url = requests.compat.urljoin(url, src)
    
    
    #Infos principales du tableau + créa du dico
    infos = {}
    for tr in soup.find_all("tr"):
        th = tr.find("th").get_text(strip=True)
        td = tr.find("td").get_text(strip=True)
        infos[th] = td
    # Ajout du reste au dico
    infos["Title"] = title
    infos["Category"] = category
    infos["Description"] = description
    infos["Rate"] = rate
    infos["Image_url"] = img_url
    infos[""] = 

    # Crea Csv
    #with open("book.csv", "w", newline="", encoding="utf-8-sig") as f:
    #    writer = csv.DictWriter(f, fieldnames=infos.keys(), delimiter=';')
    #    writer.writeheader()
    #    writer.writerow(infos)
    







    
    

   
