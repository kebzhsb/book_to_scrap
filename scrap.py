import requests
import csv
from bs4 import BeautifulSoup


# 1️⃣ Fonction pour scrapper un livre 

def scrape_book(url):
    response = requests.get(url)

    if response.ok:
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Autres infos
        title = soup.find("h1").get_text(strip=True)
        description_tag = soup.select_one("#product_description + p")
        description = description_tag.get_text(strip=True) if description_tag else ""
        category = soup.select_one("ul.breadcrumb li:nth-of-type(3) a").get_text(strip=True)
        
        # Récupérer note
        star_tag = soup.find("p", class_="star-rating")
        rating_note = star_tag["class"][1]
        word_to_number = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        rate = word_to_number.get(rating_note, 0)
        
        # Récupérer URL de l'image
        img_tag = soup.find("img")
        img_url = requests.compat.urljoin(url, img_tag["src"]) if img_tag else ""
        
        # Infos principales du tableau
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
        infos["page_url"] = url

        return infos
