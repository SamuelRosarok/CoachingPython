-- La TABLE
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom Text,
    age INTEGER,
    taille integer,
    tailebras integer,
    taillejambe integer,
    squat float,
    bench float,
    deadlift float,
);

-- 2. demande de données
INSERT INTO utilisateurs (nom, age, ville) 
VALUES ('Alice', 25, 'Paris');

INSERT INTO utilisateurs (nom, age, ville) 
VALUES ('Thomas', 32, 'Lyon');

INSERT INTO utilisateurs (nom, age, ville) 
VALUES ('Chloé', 19, 'Marseille');

-- 3. Traitement des infos
SELECT * FROM utilisateurs;
