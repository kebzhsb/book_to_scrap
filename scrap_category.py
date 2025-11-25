import requests
from bs4 import BeautifulSoup
import requests.compat

def recuperer_toutes_categories(url_base="https://books.toscrape.com/"):
    """Récupère toutes les catégories disponibles sur le site."""

    try:
        reponse = requests.get(url_base)
        reponse.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Impossible de charger la page principale {url_base} :", e)
        return {}

    page = BeautifulSoup(reponse.text, "html.parser")

    # Sélection du bloc contenant les catégories
    bloc_categories = page.find("ul", class_="nav nav-list")
    liens_categories = bloc_categories.find_all("a", href=True)

    categories = {}
    # On ignore le premier lien (Books principal)
    for lien in liens_categories[1:]:
        nom_categorie = lien.get_text(strip=True)
        url_categorie = requests.compat.urljoin(url_base, lien["href"])
        categories[nom_categorie] = url_categorie
        print(f"Catégorie trouvée : {nom_categorie}")

    return categories
