import sqlite3
import pandas as pda
import re

df = pda.read_excel("R1.xlsx")

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
    poids = re.sub(r"[^0-9,.]", "", poids)
    poids = poids.replace(",", ".")

    poids = float(poids) 

    if poids.is_integer():
        return int(poids)

    return poids 

def nettoyer_colonne(nom_table, nom_colonne, fonction_nettoyage): #nettoyer les colonnes 

    cursor.execute(
        f'SELECT rowid, "{nom_colonne}" FROM "{nom_table}"'  # Sélectionne ma colonne de ma table 
    )
    lignes = cursor.fetchall() #Selection intérmediaire

    for identifiant, valeur in lignes:        #Identifiant prend la valeur de row_id et valeur c'est ce que je trie
        valeur_nettoyee = fonction_nettoyage(valeur)   #Mes nettoyages, toi même tu sais 

        cursor.execute(  #puis je modifie ma base
            f'UPDATE "{nom_table}" '
            f'SET "{nom_colonne}" = ? WHERE rowid = ?',
            (valeur_nettoyee, identifiant)
        )

    conn.commit()

def nettoyage_tableau(nom_table):  #nettoyage de toutes les colonnes de ma base
    nettoyer_colonne(nom_table, "Poids", nettoyer_poids)
    nettoyer_colonne(nom_table, "Longueur bras ( haut de l'épaule jusqu'au bas des doigts) ( en cm)", nettoyer_taille)
    nettoyer_colonne(nom_table, "Longueur jambe ( bassin à la cheville)", nettoyer_taille)
    nettoyer_colonne(nom_table, "Age", nettoyer_poids)
    nettoyer_colonne(nom_table, "Squat", nettoyer_poids)
    nettoyer_colonne(nom_table, "Bench( développé couché)", nettoyer_poids)
    nettoyer_colonne(nom_table, "Deadlift", nettoyer_poids)
    nettoyer_colonne(nom_table, "Arraché (Snatch)", nettoyer_poids)
    nettoyer_colonne(nom_table, "Clean and jerk ( epaulé Jeté)", nettoyer_poids)



nettoyage_tableau("utilisateurs_brut")









# Travail de valeur unique, et utilisation d'un moyen de débug
# cursor.execute("""
#     UPDATE utilisateurs_brut
#     SET Squat = ?, "Clean and jerk ( epaulé Jeté)" = ?
#     WHERE Prénom = ?
# """, (168, 130, "Dino"))

# print("Nombre de lignes modifiées :", cursor.rowcount) 
# conn.commit()














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
