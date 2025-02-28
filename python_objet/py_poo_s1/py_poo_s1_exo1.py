# class Personne:
#     def __init__(self, nom, age):
#         self.__nom = nom
#         self.__age = age
#     @property
#     def nom(self):
#         return self.__nom
#     @property
#     def age(self):
#         return self.__age
#     def se_presenter(self):
#         reponse = f"Bonjour, je m'appelle {self.__nom} et j'ai {self.__age} ans"
#         return reponse
# ilan = Personne("Ilan", 32)
# elodie = Personne("Élodie", 36)
# print(ilan.se_presenter())
# print(elodie.se_presenter())

# class Voiture:
#     def __init__(self, marque, modele, annee):
#         self.__marque = marque
#         self.__modele = modele
#         self.__annee = annee
#     @property
#     def marque(self):
#         return self.__marque
#     @property
#     def modele(self):
#         return self.__modele
#     @property
#     def annee(self):
#         return self.__annee
#     def afficher_infos(self):
#         reponse = f"Cette voiture est une {self.__marque} {self.__modele} de {self.__annee}"
#         return reponse
# c4 = Voiture("Citröen", "C4", 2007)
# megane = Voiture("Renault", "Mégane 3", 2012)
# dacia = Voiture("Dacia", "Sandero 3 (GPL ma gueule)", 2012)
# print(c4.afficher_infos())
# print(megane.afficher_infos())
# print(dacia.afficher_infos())

# class CompteBancaire:
#     def __init__(self, solde=0):
#         self.__solde = solde
#     @property
#     def solde(self):
#         return self.__solde
#     def depot(self, montant):
#         self.__solde += montant
#     def retrait(self, montant):
#         self.__solde -= montant
#     def afficher_infos(self):
#         reponse = f"Votre compte est maintenant "
#         if self.__solde > 0:
#             reponse += f"créditeur de {self.__solde} €"
#         elif self.__solde < 0:
#             reponse += f"débiteur de {-self.__solde} €"
#         else:
#             reponse +=f"{reponse} vide."
#         return reponse
# compte_de_ilan = CompteBancaire(950)
# compte_de_ilan.depot(6500)
# print(compte_de_ilan.afficher_infos())
# print(compte_de_ilan.retrait(5000))
# print(compte_de_ilan.afficher_infos())

# class Livre:
#     def __init__(self, titre, auteur, annee_publication):
#         self.__titre = titre
#         self.__auteur = auteur
#         self.__annee_publication = annee_publication
#     @property
#     def titre(self):
#         return self.__titre
#     @property
#     def auteur(self):
#         return self.__auteur
#     @property
#     def annee_publication(self):
#         return self.__annee_publication
#     def afficher_infos(self):
#         reponse = f"Voici {self.__titre}. Un livre écrit par {self.__auteur} en {self.__annee_publication}"
#         return reponse
# harry = Livre("Harry Potter et le prince de sang melé", "J.K. Rowling", 1998)
# print(harry.afficher_infos())
# merci = Livre("H2G2 : Le guide du voyageur intergalactique","Douglas Adams", 1978)
# print(merci.afficher_infos())
# ile = Livre("La possibilité d'une ile", "Michel Houellebecq", 2005)
# print(ile.afficher_infos())

# class Etudiant:
#     def __init__(self, nom, notes=None):
#         self.__nom = nom
#         self.__notes = notes
#     def calculer_moyenne(self):
#         somme = 0
#         if self.__notes is None:
#             reponse = f"Il n'y a pas de note à calculer chez {self.__nom}"
#             return reponse
#         else:
#             for note in self.__notes:
#                 somme += note
#         return f"La moyenne est de {self.__nom} est de {somme / len(self.__notes)}"
# ilan = Etudiant("patrick avec 15 i", [15, 15, 15])
# tanguy = Etudiant("assa", )
# print(ilan.calculer_moyenne())
# print(tanguy.calculer_moyenne())
