largeur = int(input("Largeur : "))
longueur = int(input("Longueur : "))
print(f"Votre rectangle a une longueur de {longueur}, une largeur de {largeur}. Son  aire est donc de {longueur * largeur}")

nombreDemande = int(input("Veuillez entrer un nombre"))
if nombreDemande % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")

nombre1 = input("Veuillez entrer un nombre")
nombre2 = input("Veuillez entrer un autre nombre")
if nombre1 < nombre2:
    print(f"{nombre2} est plus grand que {nombre1} nombre2 est le nombre le plus grand")
elif nombre2 < nombre1:
    print(f"{nombre1} est plus grand que {nombre2} nombre1 est le nombre le plus grand")
else:
    print("les deux nombres sont de taille égale, ou il y a eu une erreur dans vos entrées")