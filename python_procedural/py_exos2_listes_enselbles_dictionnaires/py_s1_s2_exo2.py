from http.client import responses
from random import randint

# personne = ('Élodie', '36', 'Vierzon')
# print(personne)

# print(f"1ere entrée : {personne[0]}; derniere entrée : {personne[len(personne)-1]}")
# if 'Vierzon' in personne:
#     print("Oui, c'est là")
# else:
#     print("Non")

# tupleVersListe = list(personne)
# print(tupleVersListe)
# listeVersTuple = tuple(tupleVersListe)
# print(listeVersTuple)

# tupleDe4Elements = ('un', 'deux', 'trois', 'quatre')
# un, deux, trois, quatre = tupleDe4Elements
# print(un, deux, trois, quatre)

# tupleUn = ("j'aime", " les moches ")
# tupleDeux = ("Parce qu'on", " se fait pas quitter")
# tupleFinal = tupleUn + tupleDeux
# print(tupleFinal)

# tupleNumeraire = (2, 4, 6, 8)
# somme = 0
# moyenne = 0
# for numeraire in tupleNumeraire:
#     somme += numeraire
# print(f"Somme des éléments : {somme}")
# print(f"Moyenne de éléments : {somme/len(tupleNumeraire)}")

# tuplePourFrequence = (1, 2, 4, 6, 4, 2, 2, 8, 7, 1, 4)
# tableau = []
# for i in range(len(tuplePourFrequence)):
#     compteur = tuplePourFrequence.count(tuplePourFrequence[i])
#     tableau.append(compteur)
# index_max = tableau.index(max(tableau))
# print(tuplePourFrequence[index_max])

# tupleNombresAleatoires = (
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10),
#     randint(1,10)
# )
# print(f"Témoin : {tupleNombresAleatoires}")
# for i in range(len(tupleNombresAleatoires)):
#     if tupleNombresAleatoires[i] % 2 == 0:
#         print(tupleNombresAleatoires[i])

# nombreRandom = randint(0, 9)
# tupleOccurencesACompter = (1, 3, 5, 7, 9, 9, 6, 4, 2, 0)
# nombreOccurences = tupleOccurencesACompter.count(tupleOccurencesACompter[nombreRandom])
# print(f"Il y a {nombreOccurences} occurrences de l'élément {tupleOccurencesACompter[nombreRandom]}")