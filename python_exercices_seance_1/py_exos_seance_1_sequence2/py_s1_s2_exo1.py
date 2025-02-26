# listeNombres = [3, 2, 5, 1, 4]
# somme = 0
# for i in range(len(listeNombres)):
#     somme += listeNombres[i]
# print(f"La somme des éléments du tableau est {somme}")
# listeNombresOrdonnee = listeNombres.copy()
# listeNombresOrdonnee.sort()
# print(f"Le plus petit élément du tableau est {listeNombresOrdonnee[0]}")
# print(f"Le plus grand élément du tableau est {listeNombresOrdonnee[-1]}")
#
# test = 6
# if test in listeNombres:
#     print(f"Oui, {test} est bien dans la liste")
# else:
#     print(f"Non, {test} n'est pas dans la liste")

# listeMots = []
# for i in range(5):
#     listeMots.append(input("Veuillez entrer un mot dans la liste"))
# listeMotsOrdonnes = listeMots.copy()
# listeMotsOrdonnes.sort(reverse=True)
# print(listeMotsOrdonnes)

# listeAvecDoublons1 = ['banabe', 5, 9, 7, 71]
# listeAvecDoublons2 = ['banabe', 6, 1, 71, 78]
# for i in range(len(listeAvecDoublons1)-1):
#     if listeAvecDoublons1[i] in listeAvecDoublons2:
#         del listeAvecDoublons1[i]
# resultat = listeAvecDoublons1 + listeAvecDoublons2
# print(resultat)

# listeAvecDoublons = ['banabe', 5, 9, 7, '71', 5, 'banabe']
# listeDeDoublons = []
# for i in range(len(listeAvecDoublons)):
#     if listeAvecDoublons[i] in listeAvecDoublons[:i]:
#         listeDeDoublons.append(listeAvecDoublons[i])
# print(listeDeDoublons)

# listeNegatif = [1, 81, -2, 9, -297, 12, -9]
# for i in range(len(listeNegatif)):
#     if listeNegatif[i] < 0:
#         listeNegatif[i] = 0
# print(listeNegatif)

# listeComprehension = [i for i in range(0, 21, 2) if i % 2 == 0]
# print(listeComprehension)

# listeAInverser = [1, 2, 3, 4, 5]
# print(listeAInverser)
# dernierElement = listeAInverser.pop()
# listeAInverser.reverse()
# premierElement = listeAInverser.pop()
# listeAInverser.append(dernierElement)
# listeAInverser.reverse()
# listeAInverser.append(premierElement)
# print(listeAInverser)

# listeATrier = [5, 45, 1, 96, 3, 754, 13]
# taille = len(listeATrier)
# listeTriee = []
# while len(listeTriee) < taille:
#     listeTriee.append(min(listeATrier))
#     listeATrier.remove(min(listeATrier))
# print(listeTriee)