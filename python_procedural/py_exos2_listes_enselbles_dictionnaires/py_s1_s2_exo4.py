from random import randint

# ensembleDe5Nombres = {1, 2, 3, 4, 5}
# nombreRecherche = int(input("Entrez un nombre"))
# if nombreRecherche in ensembleDe5Nombres:
#     print(f"{nombreRecherche} est dans la liste")
# else:
#     print(f"{nombreRecherche} n'est pas dans la liste")

# ensemble1 = {"pomme", "banane", "cerise"}
# ensemble2 = {"ananas", "cerise", "orange"}
# union = ensemble1.union(ensemble2)
# print(f"Union : {union}")
# inter = ensemble1.intersection(ensemble2)
# print(f"Intersection : {inter}")
# difference1 = ensemble1.difference(ensemble2)
# difference2 = ensemble2.difference(ensemble1)
# print(f"Différence : {difference1} et {difference2}")

# mot = ""
# phrase = input("Choisissez un phrase.")
# phrase += "."
# print(phrase)
# ensembleDeMots = set()
# for i in range(len(phrase)):
#     if phrase[i] != " " and phrase[i] != ".":
#         mot += phrase[i]
#     else:
#         if mot:
#             ensembleDeMots.add(mot)
#             mot = ""
# print(ensembleDeMots)

# ensembleASupprimer = {"item1", "item2", "item3", "item4"}
# ensembleASupprimer.discard("item4")
# ensembleASupprimer.discard("item5")
# print(ensembleASupprimer)

# ensemble1 = {1, 2, 3, 4}
# ensemble2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# if ensemble1.issubset(ensemble2):
#     print(f"L'ensemble1 fait bien partie de l'ensemble2")
# else:
#     print(f"L'ensemble1 ne fait pas partie de l'ensemble2"

# listeVersEnsemble = ["pomme", "banane", "samsung", "banane", "aspirateur", "pomme"]
# ensemble = set(listeVersEnsemble)
# print(ensemble)

# ensemble1 = {1, 2, 3, 4, 5, 6, 7}
# ensemble2 = {6, 7, 8, 9, 10, 11, 12}
# print(f"{ensemble1 - ensemble2} {ensemble2 - ensemble1}")

ensemble = set()
for i in range(11):
    ensemble.add(randint(1,50))
print(ensemble)
for element in ensemble:
    if element %2 == 0:
        print(element)