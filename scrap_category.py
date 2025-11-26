import requests
from bs4 import BeautifulSoup
import requests.compat

def recuperer_toutes_categories(url_base="https://books.toscrape.com/"):
    """Récupère toutes les catégories du site."""

    try:
        reponse = requests.get(url_base)
        reponse.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {}

    page = BeautifulSoup(reponse.text, "html.parser")

    # Sélection du bloc des catégories
    bloc_categories = page.find("ul", class_="nav nav-list")
    liens_categories = bloc_categories.find_all("a", href=True)

    categories = {}
    # On saute le premier lien
    for lien in liens_categories[1:]:
        nom_categorie = lien.get_text(strip=True)
        url_categorie = requests.compat.urljoin(url_base, lien["href"])
        categories[nom_categorie] = url_categorie
        print(f"Catégorie trouvée : {nom_categorie}")

    return categories

def recuperer_liens_livres(url_categorie):
    """
    Recuperation des lien de categories
    """
    tous_les_liens = []
    page_courante = url_categorie

    while page_courante:
        try:
            reponse = requests.get(page_courante)
            reponse.raise_for_status()
        except requests.exceptions.RequestException as e:
            break

        page = BeautifulSoup(reponse.text, "html.parser")

        # Récupération des liens des livres sur cette page
        livres = page.select("article.product_pod h3 a")
        for livre in livres:
            lien_complet = requests.compat.urljoin(page_courante, livre["href"])
            tous_les_liens.append(lien_complet)

        # Passage à la page suivante si elle existe
        btn_suivant = page.select_one("li.next a")
        if btn_suivant:
            page_courante = requests.compat.urljoin(page_courante, btn_suivant["href"])
            print("Page OK")
        else:
            page_courante = None
            print("Fin de catégorie")

    return tous_les_liens
