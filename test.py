import sqlite3
import pandas as pda
import re

df = pda.read_excel("Formulaire sans titre (réponses).xlsx")

# connection à ma base de données
conn = sqlite3.connect("MaBase.db") 
cursor = conn.cursor()
 
# Table principale où je stocke mes données ( Float == REAL)
cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs3 ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom Text,
    age INTEGER,
    taille integer,
    poids REAL,
    tailebras integer,
    taillejambe integer,
    squat REAL,
    bench REAL,
    deadlift REAL,
    snatch REAL,
    clean_and_jerk REAL,
    mail TEXT
    )
""")
df = pda.read_excel("Formulaire sans titre (réponses).xlsx")

def nettoyer_taille(taille):   #Fnnction pour permettre de convertir tout en centimetre

    if taille is None:
        return None

    taille = str(taille).strip().lower()

    # Remplace la virgule par un point
    taille = taille.replace(",", ".")

    
    match = re.match(r"^(\d+)\s*m\s*(\d{1,2})$", taille)

    if match:
        metres = int(match.group(1))
        centimetres = int(match.group(2))

        return metres * 100 + centimetres

    # unités
    taille = taille.replace("cm", "")
    taille = taille.replace("m", "")

    # espce
    taille = taille.strip()

    try:
        taille = float(taille)
    except ValueError:
        return None

    # centimetre en metre
    if 0.5 <= taille <= 2.3:
        taille *= 100

    return int(taille)

def nettoyer_poids(poids):
    poids = str(poids).lower().strip() #tout mettre en minuscule et enlever les espaces

    poids = poids.replace("kg", "").strip() #remplacer kg en espace puis supprimer les espaces
    poids = poids.replace(",", ".") #remplacer la virgule par un point

    poids = float(poids) 

    if poids.is_integer():
        return int(poids)

    return poids 



#(COmmentaire global Ctrl+ K +C) pour commenter un bloc de code
# cursor.execute("""
# DROP TABLE IF EXISTS sqlite_sequence
#  """) 
#  #de quoi supprimer la table si besoin



# 4. Sauvegarde et fermeture
conn.commit()
conn.close()

print("Base de données initialisée avec succès !")
