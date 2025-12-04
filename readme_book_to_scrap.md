# Book to Scrap – Projet ETL (Extraction, Transformation, Chargement)

Ce projet récupère  et organise des données sur les livres du site *Books to Scrape*.

Le programme va :  
1. **Extraire** les pages de chaque catégorie  
2. **Extraire** les données de chaque livre  
3. **Télécharger les images associées**  
4. **Enregistrer les données dans un fichier CSV** (un CSV par catégorie)

---

## Installation

### 1. Cloner le projet  
```bash
git clone https://github.com/<mon_profil>/book_to_scrap.git
cd book_to_scrap
```

### 2. Créer un environnement virtuel 
```bash
python3 -m venv env
source env/bin/activate      # Mac / Linux
env\Scripts\activate       # Windows
```

### 3. Installer les dépendances  
```bash
pip install -r requirements.txt
```

---

## Lancer le script

À la racine du projet, exécuter :  
```bash
python main.py
```

Le programme va alors :  
- récupérer toutes les catégories du site  
- scraper chaque livre  
- télécharger les images dans un dossier `images/`  
- créer un fichier CSV par catégorie dans le dossier `csv/`

---

## Structure du projet

```
book_to_scrap/
│
├── main.py                    # Script principal qui lance le pipeline ETL
├── scrap.py                   # Scraping des informations d’un livre
├── scrap_category.py          # Récupération des catégories + liens de chaque livre
├── download_img.py            # Téléchargement des images
├── save_csv.py                # Sauvegarde des données dans un CSV
├── requirements.txt           # Liste des dépendances
└── README.md                  # Documentation du projet
```

---

## 📈 Résultat final

À la fin de l’exécution, vous obtiendrez :  
- Un dossier **csv/** contenant un fichier CSV par catégorie  
- Un dossier **images/** contenant toutes les images des livres triées par catégorie

---