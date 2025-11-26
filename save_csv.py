import csv

def enregistrer_donnees_csv(nom_fichier, liste_dictionnaires):
    """Enregistre les infos en CSV."""

    if not liste_dictionnaires:
        print("Pas de donnees")
        return

    try:
        with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
            champs = liste_dictionnaires[0].keys()
            writer = csv.DictWriter(fichier, fieldnames=champs, delimiter=";")
            
            writer.writeheader()
            writer.writerows(liste_dictionnaires)
            
        print(f"Données enregistrées {nom_fichier} !")
    except Exception as e:
        print("Erreur de telechargement")
