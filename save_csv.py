import csv

def enregistrer_donnees_csv(nom_fichier, liste_dictionnaires):
    """Enregistre une liste de dictionnaires dans un fichier CSV."""

    if not liste_dictionnaires:
        print("Aucune donnée à sauvegarder. Le fichier CSV ne sera pas créé.")
        return

    try:
        with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
            champs = liste_dictionnaires[0].keys()
            writer = csv.DictWriter(fichier, fieldnames=champs, delimiter=";")
            
            writer.writeheader()
            writer.writerows(liste_dictionnaires)
            
        print(f"Données enregistrées avec succès dans {nom_fichier} !")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement du fichier {nom_fichier} :", e)
