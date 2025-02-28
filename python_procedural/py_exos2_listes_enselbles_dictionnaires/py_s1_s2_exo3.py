# etudiants = {
#     "Ilan": 18.5,
#     "Élodie": 17.5,
#     "Hugo": 0.5
# }
# print(etudiants)
#
# etudiants["Tristan"] = "20"
# print(etudiants)
#
# etudiants["Hugo"] = "20"
# print(etudiants)
#
# if "Romain" in etudiants:
#     print("Romain")
# else:
#     print("Pas romain")
#
# for cle in etudiants.keys():
#     print(cle)
#
# for valeur in etudiants.values():
#     print(valeur)
#
# etudiants2 = {
#     "Imran": 2.5,
#     "Romain": 18,
#     "Imane": 16
# }
# etudiants.update(etudiants2)
# print(etudiants)

# phrases = {
#     "phrase": "aux Champs Élysées palam palam pam"
# }
# dejaComptes = []
# for phrase in range(len(phrases["phrase"])):
#     if phrases["phrase"][phrase] in dejaComptes:
#         continue
#     else:
#         print(f"Nombre de {phrases["phrase"][phrase]} : {phrases["phrase"].count(phrases["phrase"][phrase])}")
#         dejaComptes.append(phrases["phrase"][phrase])
#

# motDemande = input("Entrez un mot : ")
# dictionnaire = {
#     "mot": motDemande
# }
# dejaComptes = []
# for lettre in range(len(dictionnaire["mot"])):
#     if dictionnaire["mot"][lettre] in dejaComptes:
#         continue
#     else:
#         print(f"Nombre de {dictionnaire["mot"][lettre]} : {dictionnaire["mot"].count(dictionnaire["mot"][lettre])}")
#         dejaComptes.append(dictionnaire["mot"][lettre])

# produits = {
#     "Produit1": 12.50,
#     "Produit2": 59.99,
#     "Produit3": 95.00
# }
# produitEntre = input("Choisissez un produit.")
# if produitEntre in produits:
#     print(f"{produits[produitEntre]} €")
# else:
#     print("La produit n'existe pas")