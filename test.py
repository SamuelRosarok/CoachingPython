import sqlite3
import pandas as pda
import re

df = pda.read_excel("Formulaire sans titre (réponses).xlsx")

# connection à ma base de données
conn = sqlite3.connect("MaBase.db") 
cursor = conn.cursor()
 
# Table principale où je stocke mes données ( Float == REAL)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS utilisateurs4 ( 
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nom TEXT NOT NULL,
#     prenom Text,
#     age INTEGER,
#     taille integer,
#     poids REAL,
#     tailebras integer,
#     taillejambe integer,
#     squat REAL,
#     bench REAL,
#     deadlift REAL,
#     snatch REAL,
#     clean_and_jerk REAL
#     )
# """)


selection = df [[
    "Prénom",
    "Nom",
    "Age",
    "Poids",
    "Longueur bras ( haut de l'épaule jusqu'au bas des doigts) ( en cm)",
    "Longueur jambe ( bassin à la cheville)",
    "Squat",
    "Bench( développé couché)",
    "Deadlift",
    "Arraché (Snatch)",
    "Clean and jerk ( epaulé Jeté)"
]]

selection.to_sql(
    "utilisateurs_brut",
    conn,
    if_exists="replace",
    index=False
)




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

def nettoyer_poids(poids):  #Nettoyer les poids
    poids = str(poids).lower().strip() #tout mettre en minuscule et enlever les espaces

    poids = poids.replace("kg", "").strip() #remplacer kg en espace puis supprimer les espaces
    poids = poids.replace(",", ".") #remplacer la virgule par un point

    poids = float(poids) 

    if poids.is_integer():
        return int(poids)

    return poids 

def nettoyer_colonne(nom_table, nom_colonne, fonction_nettoyage): #nettoyer les colonnes 

    cursor.execute(
        f'SELECT rowid, "{nom_colonne}" FROM "{nom_table}"'
    )
    lignes = cursor.fetchall()

    for identifiant, valeur in lignes:
        valeur_nettoyee = fonction_nettoyage(valeur)

        cursor.execute(
            f'UPDATE "{nom_table}" '
            f'SET "{nom_colonne}" = ? WHERE rowid = ?',
            (valeur_nettoyee, identifiant)
        )

    conn.commit()

nettoyer_colonne("utilisateurs_brut", "Longueur jambe ( bassin à la cheville)", nettoyer_taille)




print(df.columns.tolist())















# poids_jacky = df.loc[df["Prénom"] == "Jacky", "Poids"] #utiisation de df pour faire un test unique 

# true_poids_jacky = nettoyer_poids(poids_jacky.iloc[0])  # Utilisation de .iloc[0] pour obtenir la valeur réelle

# cursor.execute(
#     "  INSERT INTO utilisateurs3 (nom,poids) VALUES (?, ?)",
#     ("Jacky", true_poids_jacky)
#    )











#(COmmentaire global Ctrl+ K +C) pour commenter un bloc de code
# cursor.execute("""
# DROP TABLE IF EXISTS sqlite_sequence
#  """) 
#  #de quoi supprimer la table si besoin



# 4. Sauvegarde et fermeture
conn.commit()
conn.close()

print("Base de données initialisée avec succès !")
