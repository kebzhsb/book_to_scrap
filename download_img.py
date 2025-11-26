import requests
import os

def telecharger_image(url_image, dossier="images"):
    """Téléchargement dimage et sauve dans un dossier."""

    if not url_image:
        print("pas d'url")
        return

    # création de dossier si besoin
    os.makedirs(dossier, exist_ok=True)

    nom_fichier = url_image.split("/")[-1]
    chemin_complet = os.path.join(dossier, nom_fichier)

    try:
        reponse = requests.get(url_image)
        reponse.raise_for_status()
        with open(chemin_complet, "wb") as f:
            f.write(reponse.content)
    except requests.exceptions.RequestException as e:
        print("Erreur de telechargement")
