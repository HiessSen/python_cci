from random import randint

noteSur100 = int(input("Veuillez entrer une notre entre 0 et 100"))
if noteSur100 == 100:
    print("OK Tristan")
elif 100 > noteSur100 > 80:
    print("C'est excellent")
elif noteSur100 <= 80 > 50:
    print("Tu es sur la bonne voie")
elif noteSur100 <= 50 > 30:
    print("Continue à travailler ! L'effort paye toujours")
else:
    print("Merci de m'avoir emmené à la CCI quand j'étais en galère")

age = int(input("Veuillez entrer votre âge"))
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")

nombreRandom = randint(1, 10)
reponse = int(input("Veuillez entrer un nombre entre 1 et 10"))
while reponse != nombreRandom:
    reponse = int(input("Veuillez entrer un nombre entre 1 et 10"))
print(f"Bravo ! {reponse}")

salaire = float(input("Veuillez entrer un salaire"))
if salaire >= 1000000000:
    print("Tranche 7  : On va vous ouvrir en 2 juste par jalousie")
elif 1000000000 > salaire > 100000000:
    print("Tranche 6 : Pas mal, vous êtes riche (+ jalousie)")
elif 100000000 > salaire > 10000000:
    print("Tranche 5 : C'est l'aisance, on ne va pas le nier")
elif 10000000 > salaire > 1000000:
    print("Tranche 4 : En vrai vous êtes plus que bien")
elif 1000000 > salaire > 100000:
    print("Tranche 3 : Hmmmm toujours riche mdrrr. Apres je partais de 1 milliard, hein")
elif 100000 > salaire > 10000:
    print("Tranche 2 : Moins de 100000 ? Ça commence a être pas ouf hein!")
elif 10000 > salaire > 1000:
    print("Tranche 1 : Toujours imposable ?? Hahahaha quel pigeon.")
else:
    print("Vous êtes un clochard, vous pouvez circuler")

motDePasse = input("Veuillez créer un mot de passe")
tentative = input("Veuillez entrer votre mot de passe")
nombreEssais = 2
while tentative != motDePasse:
    nombreEssais -= 1
    tentative = input(f"Mdp erroné. Il vous reste {nombreEssais+1} tentatives.")
    if nombreEssais == 0:
        print("Vous n'avez pas le mot de passe")
        break
print("Mot de passe correct")
