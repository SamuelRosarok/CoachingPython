import sqlite3

# 1. Connexion à la base de données (elle va utiliser votre fichier MaBase.db)
conn = sqlite3.connect("MaBase.db")
cursor = conn.cursor()

# 2. Création d'une table de test "utilisateurs"
cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    age INTEGER
)
""")

# 3. Insertion d'une ligne de test pour vérifier
cursor.execute("INSERT INTO utilisateurs (nom, age) VALUES ('Samuel', 25)")

# 4. Sauvegarde et fermeture
conn.commit()
conn.close()

print("Base de données initialisée avec succès !")
