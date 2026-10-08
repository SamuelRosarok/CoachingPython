import sqlite3
import pandas as pda

df = pda.read_excel("Formulaire sans titre (réponses).xlsx")

# connection à ma base de données
conn = sqlite3.connect("MaBase.db") 
cursor = conn.cursor()

# Table principale où je stocke mes données
cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom Text,
    age INTEGER,
    taille integer,
    poids float,
    tailebras integer,
    taillejambe integer,
    squat float,
    bench float,
    deadlift float,
    snatch float,
    clean_and_jerk float,
    mail TEXT
    )
""")
df = pda.read_excel("Formulaire sans titre (réponses).xlsx")


cursor.execute("""
DROP TABLE IF EXISTS sqlite_sequence
 """) 
 #de quoi supprimer la table si besoin



# 4. Sauvegarde et fermeture
conn.commit()
conn.close()

print("Base de données initialisée avec succès !")
