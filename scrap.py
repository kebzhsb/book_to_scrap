import requests
from bs4 import BeautifulSoup

def recuperer_infos_livre(page_url):
    """Récupère les informations d'un livre depuis sa page produit."""

    try:
        reponse = requests.get(page_url)
    except requests.exceptions.RequestException as e:
        print(f"Impossible de charger la page {page_url} :", e)
        return None

    if not reponse.ok:
        print(f"Erreur HTTP pour la page {page_url} (code {reponse.status_code})")
        return None

    reponse.encoding = "utf-8"
    page = BeautifulSoup(reponse.text, "html.parser")

    # Titre du livre
    titre_tag = page.find("h1")
    titre = titre_tag.text.strip() if titre_tag else "Titre inconnu"

    # Description
    desc_tag = page.select_one("#product_description + p")
    description = desc_tag.get_text(strip=True) if desc_tag else "Pas de description"

    # Catégorie
    cat_tag = page.select_one("ul.breadcrumb li:nth-of-type(3) a")
    categorie = cat_tag.text.strip() if cat_tag else "Inconnue"

    # Note (étoiles)
    rating_tag = page.find("p", class_="star-rating")
    rating_txt = rating_tag["class"][1] if rating_tag else "Zero"
    conversion_note = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    note = conversion_note.get(rating_txt, 0)

    # Image
    img_tag = page.find("img")
    url_image = requests.compat.urljoin(page_url, img_tag["src"]) if img_tag else ""

    # Tableau de détails
    details_livre = {}
    for ligne in page.find_all("tr"):
        cle = ligne.find("th").text.strip()
        valeur = ligne.find("td").text.strip()
        details_livre[cle] = valeur

    # Ajout des champs principaux
    details_livre["Title"] = titre
    details_livre["Category"] = categorie
    details_livre["Description"] = description
    details_livre["Rating"] = note
    details_livre["Image_url"] = url_image
    details_livre["Page_url"] = page_url

    # Petit message pour montrer que la page a été traitée
    print(f"Infos récupérées pour : {titre}")

    return details_livre
