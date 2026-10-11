import requests

reponse = requests.get("http://127.0.0.1:8000/personnes")

personnes = reponse.json()

for personne in personnes:
    print("Nom :", personne["nom"])
    print("Prénom :", personne["prenom"])
    print("Poids :", personne["poids"])
    print("Squat :", personne["squat"])
    print("Bench :", personne["bench"])
    print("Deadlift :", personne["deadlift"])
    print("Snatch :", personne["snatch"])
    print("Clean and Jerk :", personne["clean_and_jerk"])

#bonjour