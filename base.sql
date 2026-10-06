-- 1. Création de la table pour stocker vos données
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    age INTEGER NOT NULL,
    ville TEXT
);

-- 2. Insertion de vos données manuelles
INSERT INTO utilisateurs (nom, age, ville) 
VALUES ('Alice', 25, 'Paris');

INSERT INTO utilisateurs (nom, age, ville) 
VALUES ('Thomas', 32, 'Lyon');

INSERT INTO utilisateurs (nom, age, ville) 
VALUES ('Chloé', 19, 'Marseille');

-- 3. Requête pour afficher le résultat et vérifier vos données
SELECT * FROM utilisateurs;
