print("Hello, Python avec VS code !")

nom = "Alice" #Chaîne de caractères
age = 25 # Nombre entier
taille = 1.75 #Nombre à virgule flottante
est_etudiant = True #Booléen

#Vérifier le type d’une variable

nombre = 42
print(type(nombre)) #<class 'int'>

texte = "Bonjour"
print(type(texte)) #<class 'str'>

#Conversion d’un entier en chaîne de caractères
age = 30
age_str = str(age) #"30"
print (type(age_str)) # <class 'str'>

#Conversion d’une chaîne en entier
nombre_str = "42"
nombre_int = int(nombre_str) #42
print (type(nombre_str)) #<class 'int'>

#Conversion d’un entier en flottant
x = 5
x_float = float(x) #5.0
print(type(x_float)) #>class 'float'>

#Pour voir dans le terminal toujours faire (python script.py et ce qu'on veut voir) 

#Print est une fonction ne pas oublier les ()
print(x) # Permet de voir la valeur de mon 'X' qui est de 5
# Et print = echo 
print(age)

#Conversion d’une chaîne en liste de caractères
mot = "Python"
liste_caracteres = list(mot) # ['P', 'y', 't','h','o','n'] ça le met en format tableau

#Exemple si je veux voir "Alice 25 1.75 et si oui ou non avec un booléen"
print(nom,age,taille,est_etudiant)
#Afficher ma liste du mot
print(mot,liste_caracteres)

#Concaténation
prenom ="Alice"
nom ="Dupont"
nom_complet = prenom + " " + nom
print(nom_complet)

# Pour la Répétition
texte = "Python"
print(texte*3) #Python Python Python 

#Accès aux caractères
mot = "Python"
print(mot[0])  #P (Première lettre)
print(mot[-1]) # n (dernière lettre)

#Longueur d’une chaîne avec 'len'
mot = "Programmation"
print(len(mot)) #13

#Convertir en majuscule / minuscule
texte = "Bonjour"
print(texte.upper()) #BONJOUR
print(texte.lower()) #bonjour

#Exemple : Opérations mathématiques
a = 10
b = 3
print (a + b) #13
print (a - b) #7
print (a * b) #30
print (a / b) #3.33333333333335
print (a // b) #3
print (a % b) #1
print (a ** b) #1000

#Exemple : Utilisation des booléens dans une condition
age = 18
majeur = age >= 18 #True
print(majeur)

#Les opérateurs (arithmétiques, logiques, comparaisons, etc.)
#Les opérateurs de comparaison

x = 10
y = 5
print(x == y) #False
print(x != y) #True
print(x > y) #True
print(x < y) #False
print(x >= y) #True
print(x <= y) #False

#Les opérateurs logiques
a = True
b = False

print(a and b) #False
print(a or b) #True
print(not a) #False

#Exemple avec des conditions
age = 20
revenu = 3000

if age > 18 and revenu > 2000:
    print("Éligible au prêt") #Affiché
    
#Les opérateurs d'affectation
x = 5
print(x)
x += 3 # x = x + 3 -> 8
print(x)
x -= 2 # x = x - 2 -> 6
print(x)
x *= 4 # x = x * 4 -> 24
print(x)
x /= 2 # x = x / 2 -> 12.0
print(x)
x **= 2 # x = x ** 2 -> 144.0
print(x)

#Les opérateurs d'appartenance
liste = [1, 2, 3, 4, 5]
print(3 in liste) #True
print (10 in liste) #False
print (10 not in liste) #True

#Les opérateurs d'identité comparent les références mémoire de deux objets.
a = [1, 2, 3]
b = a # b référence le même objet que a
c = [1, 2, 3] # c'est une noubelle liste avec les mêmes valeurs

print(a is b) #True (même objet)
print(a is c) #False (objets différents malgré le même contenu)
print(a == b) #True (même contenu)

#Les entrées (Input) avec input()$
#La fonction input() est utilisée pour récupérer une entrée utilisateur sous forme de chaîne de caractères (str).
variable = input("Message affiché à l'utilisateur :")

#Exemple : 
# input() retourne toujours une chaîne de caractères (str), même si l'utilisateur entre un nombre.
nom = input("Quel est votre nom ? ")
print("Bonjour, " + nom + " !")

#Exemple avec conversion (int et float )
age = int(input("Entrez votre âge : ")) # Conversion en entier
taille = float(input("Entrez votre taille en mètres : ")) # Conversion en flottant

print("Vous avez", age, "ans et mesurez", taille, "m.")

# Si l'utilisateur entre du texte au lieu d'un nombre, Python déclenchera une erreur ValueError. 
# Solution : Utiliser try-except pour capturer les erreurs. 
try:
    age = int(input("Entrez votre âge : "))
    print("Votre âge est", age)
except ValueError:
    print("Erreur : Vous devez entrer un nombre entier.")
    
#Affichage de plusieurs éléments :
#print() accepte plusieurs valeurs séparées par des virgules, ce qui évite la concaténation avec +.
nom = "Tanguy"
age = 27
print("Nom :",nom, "- Âge :", age)

#Personnalisation du séparateur (sep)
print("Python", "est", "génial", sep="-")
# Résultat : Python-est-génial

#Suppression du retour à la ligne (end)
#Par défaut, print() ajoute un retour à la ligne (\n). On peut le modifier avec end="...".)
print("Bonjour", end=" ")
print("le monde !")
# Résultat : Bonjour le monde !

#Formatage des chaînes (f-string, .format(), %)
#Utilisation de f-string (Méthode recommandée - Python 3.6+)
nom = "Tanguy"
age = 27
print(f"Bonjour {nom}, vous avez {age} ans.")

#Utilisation de .format() 
nom = "Tanguy"
age = 27
print("Bonjour {}, vous avez {} ans.".format(nom,age))

#Lecture et écriture dans un fichier
#Ouverture d’un fichier (open())
mode = "r"
fichier = open("nom_du_fichier.txt", mode)

#Modes d’ouverture :
# "r" = Lecture seule (par défaut)
# "w" = Écriture (efface le contenu existant)
# "a" = Ajout à la fin du fichier
# "r+" = Lecture et écriture

# Lecture d'un fichier
f = open("exemple.txt", "r") # Ouvrir en mode lecture
contenu = f.read() # Lire tout le fichier
print(contenu)
f.close() # Fermer le fichier

#Autres méthodes de lecture :
f = open("exemple.txt", "r")
print(f.readline()) # Lire une seule ligne
print(f.readlines()) # Lire toutes les lignes sous forme de liste
f.close() # Ferme le fichier

#Utiliser with open() (ferme automatiquement le fichier) : 
with open ("exemple.txt", "r") as f:
    contenu = f.read()
    print(contenu) # Affichage du contenu
    
    
#Écriture dans un fichier
f = open("exemple.txt", "w") # Mode écriture (efface le ocntenu existant)
f.write("Ceci est une ligne de texte. \n")
f.write("Une deuxième ligne. \n")
f.close()

#Ajout de contenu sans écraser ("a") : 
with open("exemple.txt", "a") as f:
    f.write("Ajout de cette ligne. \n")
    
#Lire et écrire (r+)
with open("exemple.txt", "r+") as f:
    print(f.read()) # Lire le contenu existant
    f.write("\n Nouvelle ligne ajoutée.") # Ajouter du texte

#Les structures de contrôle
#Les conditions (if, elif, else) 
if condition:
    print("Ok")
    # Code exécuté si la condition est vrai
elif autre_condition:
    print("autre condition")
    #Code exécuté si la première condition est fausse et celle-ci est vraie
    
else:
    print("condition else")
    #Code exécuté si toutes les conditions précédentes sont fausses

#Exemple simple : Vérification de l'âge    
age = int(input("Entrez votre âge :"))

if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

#Utilisation de elif (plusieurs conditions)
note = int(input("Entrez votre note : "))

if note >= 90:
    print("Excellent")
elif note >= 70:
    print("Bien")
elif note >= 50:
    print("Passable")
else:
    print("Échec")

#Exemple avec == et != 
reponse = input("Voulez-vous continuer ? (oui/non) ")

if reponse == "oui":
    print("Programme en cours...")
elif reponse == "non":
    print("Arrêt du programme.")
else:
    print("Réponse invalide.")

#Opérateurs logiques (and, or, not)
#and = vrai si toutes les conditions sont vraies
#or = Vrai si au moins un condition est vraie
#not = Inverse la condition

# Exemple avec and et or 
age = int(input("Entrez votre âge : "))
revenu = int(input("Entrez votre revenu mensuel : "))

if age > 18 and revenu >= 2000:
    print("Vous êtes éligible à un prêt.")
else:
    print("Vous ne remplissez pas les conditions.")

#Condition simplifiée (if sur une ligne)
#On peut écrire une condition sur une seule ligne avec une expression ternaire.
age = 20
statut = "Majeur" if age >= 18 else "Mineur"
print(statut) #Majeur

#Conditions imbriquées
#On peut imbriquer plusieurs conditions dans un if
age = int (input("Entrez votre âge : "))

if age >= 18:
    if age >= 65:
        print("Vous êtes retraité.")
    else:
        print("Vous êtes adulte.")
else:
    print("Vous êtes mineur.")
    
#Vérification des valeurs vides (None, "", 0, False
#Exemple : Tester si une variable est vide
nom = input("Entrez votre nom : ")

if nom:
    print("Bonjour,", nom)
else:
    print("Vous n'avez rien saisi.")
    
#Utilisation des match-case
#Match-case permet une alternative plus lisible aux if-elif-else

jour = input("Entrez un jour de la semaine : ")

match jour:
    case "lundi":
        print("Début de la semaine !")
    case "vendredi":
        print("C'est bientôt le week-end !")
    case "samedi" | "dimanche":
        print("C'est le week-end!")
    case _:
        print("Jour inconnu.")
        
#Les structures de contrôle
#Les boucles (for, while) 
# La Syntaxe de base
sequence = [1,2,3,4]

#for variable in sequence
    #Code à exécuter
 
#Parcourir une liste
fruits = ["pomme","banane","cerise"]

for fruit in fruits:
    print(fruit)
    
#Utilisation de range()
range(début,fin,pas)
#début : Valeur de départ (optionnel, par défaut 0)
#fin : Valeur finale non incluse
#pas : Incrémentation (optionnel, par défaut 1)

# Exemple :
for i in range(5): # 0 à 4
    print(i)

for i in range(2,10,2): # De 2 à 8, pas de 2
    print(i)

#Parcourir une chaîne de caractères
mot = "Python"

for lettre in mot:
    print(lettre)
#Résultat = Python en colonne

#Parcourir un dictionnaire
#Les dictionnaires contiennent des paires clé-valeur.
etudiant = {"nom": "Siri", "age": 27, "note": 18}

for cle, valeur in etudiant.items():
    print(f"{cle} : {valeur}")

#Boucles imbriquées
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

#Le résulat de la boucle imbriqué sera
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3

#La boucle while
#La boucle while exécute du code tant qu’une condition est vraie.
condition = "true"
while condition:
    #Code exécuté tant que la condition est vraie

#Compter jusqu’à 5
i = 1
while i <= 5:
    print(i)
    i +=1

#Éviter une boucle infinie
#Si la condition ne devient jamais fausse, la boucle tourne indéfiniment.
x = 10
while x > 0:
    print(x)
    x -= 1 # Sans cette ligne la boucle ne s'arrêterait jamais ! 
# Toujours s'assure qu'un condition de sortie existe !!!!

# While avec input() (exemple interactif) 
reponse = ""

while reponse != "exit":
    reponse = input("Tapez 'exit' pour quitter : ")
    print("Vous avez tapé :", reponse)
#La boucle continue jusqu’à ce que l’utilisateur entre "exit".


#Les instructions break, continue, pass
# break : Quitter une boucle immédiatement
for i in range(10):
    if i == 5:
        break # Sort de la boucle dès que i == 5
    
#continue : Passer à l'itération suivante 
for i in range(5):
    if i == 2:
        continue # Ignore l'itération où i == 2
    print(i)
    
#pass : Ne rien faire (utile pour les blocs vides) 
#pass permet de laisser du code vide sans générer d’erreur.
for i in range(5):
    if i == 2:
        pass # Place-holder
    else:
        print(i)
        
#else après une boucle
#L’instruction else peut être utilisée avec for ou while. Elle s’exécute uniquement si aucun break ne stoppe la boucle.
#else avec for
for i in range(3):
    print(i)
else:
    print("La boucle est terminée.")
# 0 / 1 / 2 et au 3 ça met "La boucle est terminée."

#else avec while 
x = 5
while x > 0:
    print(x)
    x -= 1
else:
    print("Boucle terminée.")
# Décompte 5/4/3/2/1 et boucle terminée.

# ------------------------------------------------------
# 25/02/25

# Création d’une liste vide
ma_liste = [] # Liste vide

#Création d’une liste avec des valeurs
fruits = ["pomme","banane","cerise"]
nombre = [1,2,3,4,5]
mixte = ["Python", 3.14, True, 42]

#Accéder aux éléments d’une liste grâce à son index qu'il soit positif ou en négatif (1 / -1)
fruits = ["pomme","banane","cerise"]
print(fruits[0]) #Affiche "pomme"
print(fruits[1]) #Affiche "banane"
print(fruits[-1]) #Affiche "cerise" (Dernier élément)

#Modifier un élément
fruits = ["pomme","banane","cerise"]
fruits[1] = "orange"

print(fruits) #["pomme", "orange", "cerise"]
# Les liste sont modifiable : on peut le modifier grâce a l'index

#AJOUTER DES ÉLÉMENTS À UNE LISTE
#AJOUTER UN ÉLÉMENT À LA FIN (APPEND())
fruits = ["pomme", "banane"]
fruits.append("cerise")

print(fruits)  # ["pomme", "banane", "cerise"]

#INSÉRER UN ÉLÉMENT À UNE POSITION SPÉCIFIQUE (INSERT())
fruits = ["pomme", "banane"]
fruits.insert(1, "orange")

print(fruits) # ["pomme", "orange", "banane"]
#insert(index, valeur) insère un élément à l’index donné sans écraser les autres. 


#SUPPRIMER DES ÉLÉMENTS D’UNE LISTE
#SUPPRIMER UN ÉLÉMENT PAR VALEUR (REMOVE())
fruits = ["pomme","banane","cerise"]
fruits.remove("banane")

print(fruits) # ["pomme", "cerise"]
#Attention : Si la valeur n’existe pas, Python affichera une erreur.


#SUPPRIMER UN ÉLÉMENT PAR INDEX (DEL) 
fruits = ["pomme","banane","cerise"]
del fruits[1] # Supprime "banane"

print(fruits) # pomme et cerise du coup 

#SUPPRIMER ET RÉCUPÉRER UN ÉLÉMENT (POP())
fruits = ["pomme","banane","cerise"]
dernier_fruit = fruits.pop() # Supprime le dernier élément

print(dernier_fruit) # "cerise"
print(fruits) # ["pomme", "banane"]

#SUPPRIMER TOUS LES ÉLÉMENTS (CLEAR()) 
fruits = ["pomme","banane","cerise"]
fruits.clear() # Vide la liste

print(fruits) # []

#PARCOURIR UNE LISTE AVEC UNE BOUCLE FOR
fruits = ["pomme","banane","cerise"]

for fruit in fruits:
    print(fruit)
# Cette méthode affiche chaque élément un par un

#PARCOURIR UNE LISTE AVEC ENUMERATE() (INDEX + VALEUR)
fruits = ["pomme","banane","cerise"]

for index, fruit in enumerate(fruits): # enumerate() permet d'obtenir à la fois l’index et la valeur. 
    print(f"Index {index} : {fruit}")
    
#PARCOURIR UNE LISTE AVEC RANGE() ET LEN() 
fruits = ["pomme","banane","cerise"]

for i in range(len(fruits)):
    print(f"Index {i} : {fruits[i]}") #Utile pour accéder aux éléments par leur index.

# VÉRIFIER LA PRÉSENCE D’UN ÉLÉMENT (IN) 
fruits = ["pomme","banane","cerise"]

if "pomme" in fruits:
    print("Oui, 'pomme' est dans la liste") #in permet de vérifier si un élément existe dans une liste. 

#TRIER ET INVERSER UNE LISTE
#TRIER UNE LISTE (SORT())
nombres = [5, 2, 9, 1]
nombres.sort()

print(nombres) # [1, 2, 5, 9]
#sort() trie la liste par ordre croissant. 


#Trier en ordre décroissant
nombres = [5, 2, 9, 1]
nombres.sort(reverse=True)

print(nombres) # [9,5,2,1]

#INVERSER L’ORDRE (REVERSE()) 
fruits = ["pomme","banane","cerise"]
fruits.reverse()

print(fruits) # ["cerise", "banane", "pomme"]

#COPIE ET CONCATÉNATION DES LISTES
#COPIER UNE LISTE (COPY())
fruits = ["pomme", "banane"]
copie_fruits = fruits.copy()

print(copie_fruits) # ["pomme", "banane"]
#Ne pas utiliser copie_fruits = fruits car cela créera une référence (les deux listes seront liées). 


#CONCATÉNER DEUX LISTES (+) 
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
resultat= liste1 + liste2

print(resultat) # [1,2,3,4,5,6]

#ÉTENDRE UNE LISTE (EXTEND())
fruits = ["pomme", "banane"]
autres_fruits = ["cerise", "orange"]

fruits.extend(autres_fruits)
print(fruits) # ["pomme", "banane", "cerise", "orange"]


#GÉNÉRATION DE LISTES AVEC LIST COMPREHENSION
#Le list comprehension est une méthode efficace pour générer des listes.

#Exemple
nombres = [x for x in range(10)]
print(nombres) # [0,1,2,3,4,5,6,7,8,9]

#Filtrer une liste

nombres_pairs = [x for x in range(10) if x % 2 == 0]
print(nombres_pairs) # [0,2,4,6,8]

#Les tuples
#Les tuples sont une structure de données similaire aux listes, mais immuables.
# Cela signifie qu’une fois créés, leurs éléments ne peuvent pas être modifiés.

#Créer un tuple vide
mon_tuple = ()
print(mon_tuple) # ()

#Créer un tuple avec des valeurs
fruits = ("pomme","banane","cerise")
nombres = (1, 2, 3, 4)
mixte = ("Python", 3.14, True)

#Créer un tuple avec un seul élément
tuple_unique = ("Python",) # Virgule obligatoire
print(type(tuple_unique)) # <class 'tuple'>

tuple_erreur = ("Python") # Ce n'est PAS un tuple !
print(type(tuple_erreur)) # <class 'str>

#Accéder aux éléments d’un tuple
#Les tuples sont indexés comme les listes.
fruits = ("pomme","banane","cerise")

print(fruits[0]) # Pomme
print(fruits[1]) # Banane
print(fruits[-1]) # cerise (dernier élément)

#ACCÉDER À UNE TRANCHE (SLICING)
fruits = ("pomme", "banane", "cerise", "orange", "kiwi")

print(fruits[1:4]) # ('banane','cerise','orange')
print(fruits[:3]) # ('pomme','banane','cerise)
print(fruits[2:]) # ('cerise','orange','kiwi')
print(fruits[-3:]) # ('cerise','orange','kiwi')
# Sachant que cerise et l'index 2 mais également l'index -3

#Les tuples sont immuables
#Contrairement aux listes, on ne peut pas modifier un tuple après sa création
#Tentative de modification (génère une erreur)
fruits = ("pomme", "banane", "cerise")
fruits[1] = "orange" #Erreur car il ne trouve pas "orange"
#Les tuples ne permettent ni modification, ni ajout, ni suppression d’éléments.

#Solution : Convertir en liste, modifier, puis reconvertir
fruits = ("pomme", "banane", "cerise")

# Convertir en liste
fruits_liste = list(fruits)
fruits_liste[1] = "orange"

# Reconvertir en tuple
fruits = tuple(fruits_liste)
print(fruits) # ('pomme', 'orange', 'cerise')

#PARCOURIR UN TUPLE AVEC UNE BOUCLE FOR 
fruits = ("pomme", "banane", "cerise")

for fruit in fruits:
    print(fruit)
# Ça affiche pomme/banane/cerise en colonne

#VÉRIFIER LA PRÉSENCE D’UN ÉLÉMENT (IN) 
fruits = ("pomme", "banane", "cerise")

if "banane" in fruits:
    print("Banane est dans le tuple !")

#OPÉRATIONS SUR LES TUPLES
#CONCATÉNER DEUX TUPLES (+)
tuple1 = (1,2,3)
tuple2 = (4,5,6)
resultat = tuple1 + tuple2

print(resultat) # (1,2,3,4,5,6)

#Répéter un tuple (*)
fruits = ("pomme", "banane")
repetition = fruits * 3

print(repetition) # ('pomme', 'banane', 'pomme', 'banane', 'pomme', 'banane') 

#NOMBRE D’OCCURRENCES (COUNT()) 
nombres = (1,2,3,2,4,2,5)
print(nombres.count(2)) # 3 (Le nombre 2 apparaît 3 fois dans le tuple)

#TROUVER L’INDEX D’UN ÉLÉMENT (INDEX()) 
fruits = ("pomme", "banane", "cerise")
print(fruits.index("banane")) # 1

#Convertir un tuple en liste et vice versa
# Convertir un tuple en liste
fruits = ("pomme", "banane", "cerise")
liste_fruits = list(fruits)

print(liste_fruits) # ['pomme','banane','cerise']

#Convertir une liste en tuple
liste_fruits = ["pomme","banane","cerise"]
fruits = tuple(liste_fruits)

print(fruits) #('pomme','banane','cerise')

#Déballer (unpacking) un tuple
personne = ("Alice", 25, "Paris")

nom, age, ville = personne
print(nom) #Alice
print(age) # 25
print(ville) # Paris

#DÉBALLAGE AVEC * (RESTANT DES VALEURS) 
nombres = (1,2,3,4,5)

premier, *milieu, dernier = nombres
print(premier) # 1
print(milieu) #[2,3,4] # *milieu stocke tous les éléments entre premier et dernier sous forme de liste. 
print(dernier) #[5]

#Les dictionnaires
#Les dictionnaires sont une structure de données clé-valeur permettant de stocker des informations de manière rapide et organisée
#Contrairement aux listes et tuples, chaque élément est associé à une clé unique, ce qui permet un accès très rapide aux données.

# Créer un dictionnaire vide
mon_dico = {}
mon_dico_vide = dict()
print(mon_dico) # {}

#Créer un dictionnaire avec des valeurs
etudiant = {
    "nom": "Alice",
    "age": 22,
    "ville": "Paris"
}

print(etudiant) #{'nom': 'Alice','age': 22, 'ville}
# Les clés sont uniques.
#Les valeurs peuvent être de n’importe quel type (int, str, list, tuple, dict…).
#Les clés doivent être immuables (str, int, tuple mais pas list ou dict).


#ACCÉDER AUX VALEURS D’UN DICTIONNAIRE
#ACCÉDER À UNE VALEUR PAR SA CLÉ (DICO[CLÉ])

etudiant = {"nom": "Alice", "age": 22, "ville": "Paris"}
print(etudiant["nom"]) # Alice

# Ça affichera un ERREUR si la clé n'existe pas !!
print(etudiant["email"]) # KeyError

#ACCÉDER À UNE VALEUR EN ÉVITANT L’ERREUR (GET()) 
print(etudiant.get("nom")) #Alice
print(etudiant.get("email", "Non renseigné")) # Non renseigné

#get(clé, valeur_par_defaut) retourne "Non renseigné" si la clé n’existe pas. 


#Ajouter ou modifier des éléments
#Ajouter une nouvelle clé-valeur
etudiant["email"] = "alice@email.com"
print(etudiant)

#Modifier une valeur existante
etudiant["age"] = 23
print(etudiant) # {'nom': 'Alice', 'age': 23, 'ville': 'Paris', 'email': 'alice@email.com}

#SUPPRIMER DES ÉLÉMENTS
# Suppimer un élément par clé (DEL)
del etudiant["ville"]
print(etudiant) # {'nom': 'Alice', 'age': 23, 'email': 'alice@email.com}

# Pour supprimer et récupérer une valeur (Pop())
email = etudiant.pop("email")
print(email) # alice@email.com
print(etudiant) # {'nom': 'Alice', 'age': 23}

# Pour supprimer tous les éléments (clear())
etudiant.clear()
print(etudiant) # {}

# Afin de parcourir un dictionnaire
# Parcourir les clés (keys())
for cle in etudiant.keys():
    print(cle)
    
# Parcourir les valeurs (values())
for valeur in etudiant.values():
    print(valeur)
    
# Parcourir les clés et valeutrs (items())
for cle, valeur in etudiant.items():
    print(f"{cle} : {valeur}")
# Ça affichera nom : Alice et age : 23

# Vérifier l'existence d'une clé (in)
if "age" in etudiant:
    print("L'âge est renseigné.")
    
# Pour copier un dictionnaire (copy())
dico_original = {"a" : 1, "b" : 2}
dico_copie = dico_original.copy()

print(dico_copie) # {'a' : 1, 'b' : 2}
# Ne pas utiliser =, car cela crée une référence (les modifications affectent les deux dictionnaires). 

# Fusionner deux dictionnaires (update())
dico1 = {"nom": "Alice", "age": 22}
dico2 = {"ville": "Paris", "email":"alice@email.com"}

dico1.update(dico2)
print(dico1)
#Les clés existantes sont mises à jour, les nouvelles sont ajoutées

# Pour trier un dictionnaire (SORTED())

# Trier par clé
notes = {"Alice" : 15, "Bob": 12, "Chalie": 18}
notes_tries = dict(sorted(notes.items()))

print(notes_tries) # Ça affiche {'Alice':15, 'Bob' : 12', 'Charlie': 18}
# Tier par valeur
notes_tries = dict(sorted(notes.items(), key=lambda x: x[1]))
print(notes_tries) #{'Bob': 12, 'Alice': 15, 'Charlie' : 18}

#Dictionnaire imbriqué (dictionnaire dans un dictionnaire)
etudiants = {
    "Alice": {"age" : 22, "note":15},
    "Bob": {"age": 23,"note": 12}
}

print(etudiants["Alice"]["note"]) # 15

#Les ensembles (sets)
#Les ensembles (set) sont une structure de données en Python permettant de stocker des éléments uniques de manière désordonnée.
#Ils sont particulièrement utiles pour éviter les doublons et effectuer des opérations ensemblistes (union, intersection, etc.). 

#CRÉER UN ENSEMBLE VIDE
mon_ensemble = set()
print(mon_ensemble) # set()
# Ne pas utiliser {} car ça crée un dictionnaire vide

#Créer un ensemble avec des valeurs
fruits = {"pomme","banane","cerise"}
print(fruits) # {'banane','cerise','pomme'}
# L'ordre des éléments peut changer, car les ensembles sont désordonnés


#Élimination automatique des doublons
nombres = {1,2,2,3,4,4,5}
print(nombres) # {1,2,3,4,5}
#Les ensembles ne stockent pas de doublons

#CRÉER UN ENSEMBLE À PARTIR D’UNE LISTE (SET()) 
liste = [1,2,3,4,5,5]
ensemble = set(liste)
print(ensemble) # {1,2,3,4,5}
# Convertir une liste en set permet d'éliminer les doublons !!

#VÉRIFIER LA PRÉSENCE D’UN ÉLÉMENT (IN) 
fruits = {"pomme","banane","cerise"}

if "pomme" in fruits:
    print("Pomme est dans l'ensemble ! ")
    
# Les ensembles permmettent un recherche très rapide (0(1))

#AJOUTER DES ÉLÉMENTS À UN ENSEMBLE
#Ajouter un élément (add())
fruits = {"pomme","banane"}
fruits.add("cerise")
print(fruits) #{'banane','cerise','pomme'}

#AJOUTER PLUSIEURS ÉLÉMENTS (UPDATE()) 
fruits = {"pomme","banane"}
fruits.update(["cerise","orange"])
print(fruits) # {'pomme','banane','cerise','orange'}

#SUPPRIMER DES ÉLÉMENTS D’UN ENSEMBLE
#Supprimer un élément (remove())
fruits = {"pomme","banane","cerise"}
fruits.remove("banane")
print(fruits) # ça supprime banane est ça donne {'pomme','cerise'}

#Erreur (KeyError) si l’élément n’existe pas ! 


#SUPPRIMER UN ÉLÉMENT SANS ERREUR (DISCARD()) 
fruits = {"pomme","banane","cerise"}
fruits.discard("banane")
fruits.discard("fraise") # Ne génère pas d'erreur
print(fruits) #{'pomme','cerise'}

#SUPPRIMER ET RÉCUPÉRER UN ÉLÉMENT ALÉATOIRE (POP()) 
fruits = {"pomme","banane","cerise"}
element = fruits.pop()
print(element) # Affiche un élément supprimé (aléatoire)
print(fruits) # Ensemble mis à jour

#SUPPRIMER TOUS LES ÉLÉMENTS (CLEAR()) 
fruits = {"pomme","banane","cerise"}
fruits.clear()
print(fruits) # set()

#PARCOURIR UN ENSEMBLE AVEC UNE BOUCLE FOR 
fruits = {"pomme","banane","cerise"}
for fruit in fruits:
    print(fruit)
    
# L'odre d'affichage est aléatoire !!


#OPÉRATIONS ENSEMBLISTES
#Union (| ou union())
#Retourne un ensemble contenant tous les éléments des deux ensembles (sans doublons).
set1 = {1,2,3}
set2 = {3,4,5}

union1 = set1 | set2
union2 = set1.union(set2)

print(union1) #{1,2,3,4,5}
print(union2) #{1,2,3,4,5}

#Les ensembles (sets)
#INTERSECTION (& OU INTERSECTION())
#Retourne les éléments communs entre deux ensembles.
set1 = {1,2,3}
set2 = {3,4,5}

inter =set1 & set2
print(inter) # {3}

#DIFFÉRENCE (- OU DIFFERENCE())
#Retourne les éléments présents dans le premier ensemble mais pas dans le second.
set1 = {1,2,3}
set2 = {3,4,5}

diff = set1 - set2
print(diff) #{1, 2}

#DIFFÉRENCE SYMÉTRIQUE (^ OU SYMMETRIC_DIFFERENCE())
#Retourne les éléments présents dans l’un des ensembles mais pas dans les deux.
set1 = {1,2,3}
set2 = {3,4,5}

diff_sym = set1 ^ set2
print(diff_sym) # {1,2,4,5}

#VÉRIFIER LES RELATIONS ENTRE ENSEMBLES
#VÉRIFIER SI UN ENSEMBLE EST UN SOUS-ENSEMBLE (ISSUBSET())
set1 = {1, 2}
set2 = {1,2,3,4}

print(set1.issubset(set2)) # True
#set1 est contenu dans set2. 

#VÉRIFIER SI UN ENSEMBLE EST UN SUR-ENSEMBLE (ISSUPERSET()) 
print(set2.issuperset(set1)) #True
#set2 contient set1


#VÉRIFIER SI DEUX ENSEMBLES SONT DISJOINTS (ISDISJOINT()) 
set1 = {1,2,3}
set2 = {4,5,6}

print(set1.isdisjoint(set2)) # True (aucun élément en commun)

#COPIER UN ENSEMBLE (COPY()) 
set1 = {1,2,3}
set2 = set1.copy()

print(set2) # {1,2,3}
# Ne pas utiliser set2=set1, car cela crée un référence, pas UNE COPIE


#Définition et appel de fonctions
#Une fonction est définie avec le mot-clé def, suivi du nom de la fonction et des parenthèses ().

def nom_de_fonction():
    #Instructions à exécuter
    print("Bonjour, ceci est une fonction ! ")

#APPEL D’UNE FONCTION
#Pour exécuter une fonction, il suffit de l’appeler par son nom, suivi de ().
def saluer():
    print("Bonjour ! ")
#Appel de la fonction
saluer() # Bonjour !

#Fonctions avec paramètres
#Les paramètres permettent de passer des valeurs à une fonction.
def saluer(nom):
    print(f"Bonjour, {nom} !")
    
saluer("Alice")
saluer("Bob")
# Cela affichera Bonjour, Alice ! et Bonjour, Bob !

#Fonction avec plusieurs paramètres
def additionner(a, b):
    print(f"Résultat : {a + b}")

additionner(5, 3) # Résultat : 8
additionner(10, 2) # Résultat : 12

#RETOURNER UNE VALEUR (RETURN)
#Une fonction peut renvoyer un résultat avec return.
def carre(nombre):
    return nombre **2
resultat = carre(4)
print(resultat) # 16
#return renvoie la valeur, qui peut être stockée ou utilisée directement

#Fonction avec plusieurs valeurs retournées
def calculs(a, b):
    somme = a + b
    produit = a * b
    return somme, produit

res_somme, res_produit = calculs(3, 4)
print(res_somme) # 7
print(res_produit) # 12

#Paramètres par défaut
#On peut définir des valeurs par défaut pour les paramètres.
def saluer(nom="Utilisateur"):
    print(f"Bonjour, {nom} !")

saluer()    # Bonjour, Utilisateur !
saluer("Alice") # Bonjour, Alice !
#Si aucun argument n’est donné, la valeur par défaut est utilisée.

#NOMBRE VARIABLE DE PARAMÈTRES
#Python permet de passer un nombre variable d’arguments avec *args et **kwargs.
#*ARGS (ARGUMENTS POSITIONNELS MULTIPLES)
def additionner_tout(*nombres):
    return sum(nombres)

print(additionner_tout(1, 2, 3)) # 6
print(additionner_tout(10, 20, 30, 40)) # 100
#*args regroupe les arguments en un tuple. 

#**KWARGS (ARGUMENTS NOMMÉS MULTIPLES) 
def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")
afficher_infos(nom="Alice", age=25, ville="Paris") # Le résultat sera nom : Alice / age : 25 / ville : Paris
#**kwargs regroupe les arguments en un dictionnaire. 

#Portée des variables
#*Les variables définies dans une fonction sont locales et n’existent qu’à l’intérieur de cette fonction.
#Variable locale (accessible uniquement dans la fonction)
def fonction():
    x = 10 # Variable locale
    print(x)

fonction()
#print(x) #Erreur : x n'existe pas hors de la fonction

#Variable globale
#On peut définir une variable globale pour qu’elle soit accessible partout.
y = 5 # Variable globale

def afficher():
    print(y) # Accessible dans la fonction
    
afficher()
#!Les variables globales sont accessibles partout, mais leur modification doit être évitée.

#Fonction lambda (fonction anonyme)
#Une fonction lambda est une fonction courte définie en une seule ligne.
#Syntaxe : lambda arguments : expression 
carre = lambda x: x**2
print(carre(5)) # 25

#Exemple avec plusieurs arguments :
addition = lambda x, y: x + y
print(addition(3, 7)) #10

#MODULES ET BIBLIOTHÈQUES STANDARDS (MATH, RANDOM, DATETIME, ETC.) 
#*Les modules et bibliothèques standards de Python permettent d’accéder à des fonctionnalités avancées sans avoir à les coder soi-même.
#* Python offre une grande variété de modules intégrés pour effectuer des calculs mathématiques, manipuler des dates, générer des nombres 
#* aléatoires, etc.

#Importer un module en Python
#Importer un module entier
import math
print(math.sqrt(16)) # 4.0 #*sqrt = racine carré
#On doit préciser le nom du module avant la fonction (math.sqrt()). 

#Importer une seule fonction
from math import sqrt
print(sqrt(16)) #4.0
#* Plus court, mais peut entraîne des conflits de noms


#RENOMMER UN MODULE (AS) as = alias
import math as m
print(m.sqrt(16)) # 4.0
#Utile pour raccourcir un module avec un alias

#MODULE MATH (MATHÉMATIQUES AVANCÉES)
#Le module math propose des fonctions pour des opérations mathématiques avancées.

import math
print(math.sqrt(25)) #5.0 (racine carrée)
print(math.pow(2, 3)) #8.0 (puissance)
print(math.factorial(5)) #120 (factorielle)

#Constantes mathématiques
print(math.pi) # 3.141592653589793
print(math.e) # 2.71828182845905  #* e = expodentielle


#Arrondis et valeurs absolues
print(math.floor(3.7)) # 3 (arrondi vers le bas)
print(math.ceil(3.2)) #4 (arrondi vers le haut)
print(math.fabs(-7)) # 7.0 (valeur absolue)

#MODULE RANDOM (GÉNÉRATION DE NOMBRES ALÉATOIRES)
#*Le module random permet de générer des nombres aléatoires, utiles pour les jeux, les simulations, les tests aléatoires, etc..
#GÉNÉRER UN NOMBRE ALÉATOIRE ENTRE 0 ET 1
import random
print(random.random()) # Ex: 0.678493

#Générer un nombre entier aléatoire dans un intervalle
print(random.randint(1, 10)) # Nombre entier entre 1 et 10 inclus
print(random.randrange(1,10,2)) #Nombre impair entre 1 et 10

#Choisir un élément aléatoire dans une liste
fruits = ["pomme","banane","cerise","orange"]
print(random.choice(fruits)) #Ex : "Banane"

#Mélanger une liste aléatoirement
nombres = [1,2,3,4,5]
random.shuffle(nombres)
print(nombres) # Ex: [3,5,1,4,2]

#Générer plusieurs nombres aléatoires
print(random.sample(range(1,50),5)) #Ex : [12,33,5,45,20]


#MODULE DATETIME (GESTION DES DATES ET HEURES)
#Le module datetime permet de manipuler les dates et les heures.
#*OBTENIR LA DATE ET L’HEURE ACTUELLE
from datetime import datetime

now = datetime.now()
print(now) # Ex: 2025-02-26  14:30:10.345678

#Afficher la date sous un format spécifique
print(now.strftime("%d/%m/%Y")) # 26/02/2025
print(now.strftime("%H:%M:%S")) # 12:04:54

#*Principaux formats :
#%Y → Année complète (2025)
#%m → Mois (02)
#%d → Jour (07)
#%H → Heure (14)
#%M → Minute (30)
#%S → Seconde (10)


#Créer une date spécifique
date_anniversaire = datetime(1997, 5, 12)
print(date_anniversaire) # 1997-05-12 00:00:00


#Calculer la différence entre deux dates
date1 = datetime(2025,1,1)
date2 = datetime(2025,12,31)

difference = date2 - date1
print(difference.days) # 364 jours


#MODULE OS (GESTION DES FICHIERS ET DU SYSTÈME D’EXPLOITATION)
#Le module os permet d’interagir avec le système de fichiers.
#OBTENIR LE RÉPERTOIRE DE TRAVAIL ACTUEL

import os
print(os.getcws()) #Ex : "/Users/nom_utilisateur/Documents"

#Lister les fichiers d’un dossier
print(os.listdir(".")) # Liste des fichiers dans le dossier actuel


#Créer un dossier
os.mkdir("nouvea_dossier")

#Vérifier si un fichier existe
print(os.path.exists("mon_fichier.txt")) # True ou False


#MODULE SYS (INFORMATIONS SUR L’INTERPRÉTEUR PYTHON)
#Le module sys permet d’interagir avec l’interpréteur Python.
#AFFICHER LA VERSION DE PYTHON
import sys
print(sys.version)

#Obtenir les arguments de la ligne de commande
print(sys.argv) # Liste des arguments passés au script


#MODULE TIME (GESTION DU TEMPS ET DES PAUSES)
#Le module time permet de gérer le temps et d’ajouter des pauses.
#PAUSE DANS UN PROGRAMME (SLEEP())
import time
print("Début")
time.sleep(3) # Pause de 3 secondes
print("Fin")


#Obtenir le temps actuel en secondes depuis 1970
print(time.time()) # Ex: 1707324123.2456

#MODULE JSON (GESTION DES FICHIERS JSON)
#Le module json permet de manipuler des fichiers JSON, souvent utilisés pour stocker des données.
#CONVERTIR UN DICTIONNAIRE EN JSON
import json

personne = {"nom": "Alice", "age": 25, "ville": "Paris"}
json_data = json.dumps(personne)
print(json_data) # {"nom": "Alice", "age":25, "ville":"Paris"}

#Charger des données JSON dans un dictionnaire
personne_dict = json.loads(json_data)
print(personne_dict["nom"]) # Alice

