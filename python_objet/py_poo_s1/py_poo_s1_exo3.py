# class CompteBancaire:
#     def __init__(self, solde):
#         self.__solde = solde
#     @property
#     def solde(self):
#         return self.__solde
#     def depot(self, montant):
#         self.__solde = self.__solde + montant
#         return self.__solde
#     def retrait(self, montant):
#         self.__solde = self.__solde - montant
#         return self.__solde
#     def afficher_solde(self):
#         reponse = f"Votre compte est maintenant "
#         if self.__solde > 0:
#             reponse += f"créditeur de {self.__solde} €"
#         elif self.__solde < 0:
#             reponse += f"débiteur de {-self.__solde} €"
#         else:
#             reponse +=f"{reponse} vide."
#         return reponse
# compte = CompteBancaire(100)
# compte.depot(100)
# compte.retrait(50)
# print(compte.afficher_solde())
# compte.solde = 0
# print(compte.afficher_solde())

# class Voiture:
#     def __init__(self, kilometrage):
#         self._kilometrage = kilometrage
#     @property
#     def kilometrage(self):
#         return self._kilometrage
#     def ajouter_kilometrage(self, kmhs):
#         self._kilometrage += kmhs
#         return self._kilometrage
#     def get_kilometrage(self):
#         return self._kilometrage
# voiture = Voiture(100)
# voiture.ajouter_kilometrage(100)
# print(voiture.get_kilometrage())
#
# class Utilisateur:
#     def __init__(self, mot_de_passe):
#         self.__mot_de_passe = mot_de_passe
#     @property
#     def changer_mot_de_passe(self):
#         new_mdp = input("Changer mot de passe")
#         self.__mot_de_passe = new_mdp
#     def verifier_mot_de_passe(self):
#         check = input("Verifier mot de passe")
#         if check == self.__mot_de_passe:
#             reponse = f"Vous avez le bon mot de passe"
#         else:
#             reponse = f"Mot de passe incorrect"
#         return reponse
# user = Utilisateur("dzat'ze")
# print(user.verifier_mot_de_passe())

# class Article:
#     def __init__(self, prix):
#         self.__prix = prix
#     @property
#     def prix(self):
#         return self.__prix
#     @prix.setter
#     def prix(self, value):
#         value = input(float("entrez une valeur"))
#         self.__prix = value
# valeur = Article(100)
# print(valeur.prix)
# print(valeur.prix)