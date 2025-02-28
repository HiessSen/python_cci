for i in range(1, 11):
    print(i)

n = 5
j = 0
for i in range(1, n):
    print(f"{j} + {i} = {j + i}")
    j += i

nombreDonne = int(input("Veuillez entrer votre nombre entre 1 et 10"))
for i in range(1, 11):
    print(f"{nombreDonne} x {i} = {i * nombreDonne}")

compteur = 10
while compteur > 0:
    print(compteur)
    compteur -= 1

saisie = input("Veuillez entrer votre saisie")
while saisie != "Oui" and saisie != "Non":
    print("Vous n'avez pas repondu correctement")
    saisie = input("Veuillez entrer votre saisie")
print(f"Vous avez répondu {saisie}")

nombreN = 75
for i in range(0, nombreN, 2):
    print(i)