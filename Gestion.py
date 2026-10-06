






def recherche_info():
    #Gestion de demande de données provisoires
    profil= {}
    sportif =["nom","prenom","age","taille","tailebras","taillejambe","squat","bench","deadlift"]
   

    for i in range(len(sportif)):
        profil[sportif[i]] = input(f"Entrez votre {sportif[i]} : ")

    return profil


mon_profil = recherche_info()

print("Voici votre profil :", mon_profil)



