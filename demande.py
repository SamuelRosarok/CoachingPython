from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Personne(BaseModel):
    nom: str
    prenom: str
    age: int
    taille: float
    proportionBras: float
    proportionJambes: float

app = FastAPI()

# 🔴 AJOUT SÉCURITÉ : Permet à votre page HTML de communiquer avec l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les sources à envoyer des données pour les tests
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de calcul des proportions corporelles !"}

@app.post("/analyser")
def analyser_proportions(personne: Personne):
    somme_proportions = personne.proportionBras + personne.proportionJambes
    
    return {
        "statut": "Données traitées avec succès",
        "nom_complet": f"{personne.prenom} {personne.nom}",
        "age": personne.age,
        "somme_proportions": round(somme_proportions, 2)
    }




