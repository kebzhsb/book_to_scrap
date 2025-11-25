from scrap import recuperer_infos_livre
from scrap_category import recuperer_liens_livres,recuperer_toutes_categories
from save_csv import enregistrer_donnees_csv
from download_img import telecharger_image
import os

# Programme principal
if __name__ == "__main__":
    base_url = "https://books.toscrape.com/"
    print("On commence par récupérer toutes les catégories...\n")

    categories = recuperer_toutes_categories(base_url)
    print(f"{len(categories)} catégories trouvées.\n")

    for nom_categorie, url_categorie in categories.items():
        print(f"Catégorie en cours : {nom_categorie}")
        liens_livres = recuperer_liens_livres(url_categorie)
        print(f"   → {len(liens_livres)} livres détectés")

        livres_categorie = []

        for url_livre in liens_livres:
            print(f"   Récupération des infos pour : {url_livre}")
            infos_livre = recuperer_infos_livre(url_livre)
            if infos_livre:
                livres_categorie.append(infos_livre)
                telecharger_image(infos_livre["Image_url"], dossier=f"images/{nom_categorie}")
            else:
                print(f"   Impossible de récupérer ce livre : {url_livre}")

        # Création du dossier CSV si nécessaire
        os.makedirs("csv", exist_ok=True)
        nom_fichier_csv = f"csv/{nom_categorie.replace(' ', '_').lower()}.csv"
        enregistrer_donnees_csv(nom_fichier_csv, livres_categorie)

        print(f"Catégorie '{nom_categorie}' terminée.\n")

    print("Scraping terminé pour toutes les catégories !")
