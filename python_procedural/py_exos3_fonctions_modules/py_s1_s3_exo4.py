from random import randint

def table_multiplication(n):
    reponse = ''
    for i in range(11):
        reponse += f"{i} x {n} = {i*n}\n"
    print(reponse)
table_multiplication(10)

def compter_voyelles(chaine):
    nombre_voyelles = 0
    for lettre in chaine:
        if lettre in 'aeiouy':
            nombre_voyelles += 1
    return nombre_voyelles
print(compter_voyelles('baka'))

def generer_mot_de_passe(longueur):
    mot_de_passe = ""
    liste_caracteres = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "X", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "?", ",", "&", "!", "§", ":", "/", ";" '=', '+', '}', ')', "°", "]", "à", "@", "^", "ç", "_"
    ]
    while len(mot_de_passe) < longueur:
        mot_de_passe += liste_caracteres[randint(0, len(liste_caracteres)-1)]
    return mot_de_passe
print(generer_mot_de_passe(999))

liste1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
liste2 = [12, 21, 21, 29, 514, 78, 98, 35, 21]
def nombre_occurences(liste, valeur):
    if valeur in liste:
        return f"valeur se trouve {liste.count(valeur)} fois dans cette liste"
    else:
        return "La valeur n'apparait pas dans la liste"
print(nombre_occurences(liste1, 5))

def inverse_chaine(chaine):
    mot_inverse = ""
    for i in range(len(chaine)-1, -1, -1):
        mot_inverse += chaine[i]
    return mot_inverse
mot = input("Veuillez entrer un mot")
print(inverse_chaine(mot))

def convertir_temps(secondes):
    trotteuse = 0
    minutesTemp = 0
    heuresTemp = 0
    for i in range(secondes):
        trotteuse += 1
        if trotteuse == 60:
            minutesTemp += 1
            trotteuse = 0
        if minutesTemp == 60:
            heuresTemp += 1
            minutesTemp = 0
    print(f"Temps réel : {heuresTemp}h{minutesTemp}:{trotteuse}")
convertir_temps(12684)

liste1 = [2, 3, 13, 8, 5, 2, 7, 6]
liste2 = [27, 98, 152, 23, 78, 12, 85]
def trier_liste(liste, ordre="asc"):
    if ordre == "asc":
        return sorted(liste)
    elif ordre == "desc":
        return sorted(liste, reverse=True)
print(trier_liste(liste1, ordre="asc"))
print(trier_liste(liste2, ordre="desc"))