from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

class Personne(BaseModel):
    nom: str
    prenom: str
    age: Optional[int] = None
    mail: Optional[str] = None

    poids:  float
    taille:  float

    taillebras:  float
    taillejambe:  float

    squat: Optional[float] = None
    bench: Optional[float] = None
    deadlift: Optional[float] = None
    snatch: Optional[float] = None
    clean_and_jerk: Optional[float] = None

app = FastAPI()

# Configuration CORS pour permettre les requêtes 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les sources à envoyer des données pour les tests
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

personnes = []

@app.get("/")

def accueil():
    return {"message": "Bienvenue sur mon API !"}

@app.post("/personnes")
def ajouter_personne(personne: Personne):
    personnes.append(personne)
    return {
        "message": "Personne ajoutée avec succès",
        "personne": personne.model_dump()
    }

@app.get("/personnes")
def lire_personnes():
    return [personne.model_dump() for personne in personnes]

@app.get("/personnes/{index}")
def lire_personne(index: int):
    if index < 0 or index >= len(personnes):
        return {"erreur": "Personne introuvable"}

    return personnes[index].model_dump()




