import requests
import os

def telecharger_image(url_image, dossier="images"):
    """Télécharge une image depuis une URL et la sauvegarde dans un dossier."""

    if not url_image:
        print("Aucune URL fournie pour l'image, téléchargement annulé.")
        return

    # Crée le dossier si nécessaire
    os.makedirs(dossier, exist_ok=True)

    nom_fichier = url_image.split("/")[-1]
    chemin_complet = os.path.join(dossier, nom_fichier)

    try:
        reponse = requests.get(url_image)
        reponse.raise_for_status()
        with open(chemin_complet, "wb") as f:
            f.write(reponse.content)
        print(f"Image téléchargée : {nom_fichier}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement de {url_image} :", e)
