from fastapi import FastAPI
from pydantic import BaseModel



class Personne(BaseModel):
    nom: str
    prenom: str
    age: int
    taille : float
    proportionBras: float
    proportionJambes: float

app = FastAPI()

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
        "somme_proportions": round(somme_proportions, 2),
        "details": {
            "bras": personne.proportionBras,
            "jambes": personne.proportionJambes
        }
    }




