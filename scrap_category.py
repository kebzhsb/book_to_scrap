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

def recuperer_liens_livres(url_categorie):
    """
    Récupère tous les liens des livres d'une catégorie donnée,
    en parcourant toutes les pages de la catégorie.
    """
    tous_les_liens = []
    page_courante = url_categorie

    while page_courante:
        try:
            reponse = requests.get(page_courante)
            reponse.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Impossible de charger la page {page_courante} :", e)
            break

        page = BeautifulSoup(reponse.text, "html.parser")

        # Récupération des liens des livres sur cette page
        livres = page.select("article.product_pod h3 a")
        for livre in livres:
            lien_complet = requests.compat.urljoin(page_courante, livre["href"])
            tous_les_liens.append(lien_complet)
            print(f"Lien ajouté : {lien_complet}")

        # Passage à la page suivante si elle existe
        btn_suivant = page.select_one("li.next a")
        if btn_suivant:
            page_courante = requests.compat.urljoin(page_courante, btn_suivant["href"])
            print("On passe à la page suivante...")
        else:
            page_courante = None
            print("Fin de la catégorie, tous les liens récupérés.")

    return tous_les_liens
