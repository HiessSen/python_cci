# from random import randint
#
# for i in range(1,21):
#     if i % 3 == 0:
#         print(f"{i} : Fizz")
#     elif i % 5 == 0:
#         print(f"{i} : Buzz)")
#     elif i % 3 == 0 and i % 5 == 0:
#         print(f"{i} : FizzBuzz")
#     else:
#         break
#
# nombreMystere = randint(1,11)
# tentative = int(input("Veuillez entrer votre nombre"))
# nombreEssais = 4
# while tentative != nombreMystere:
#     nombreEssais -= 1
#     tentative = input(f"Nombre erroné. Il vous reste {nombreEssais+1} tentatives.")
#     if nombreEssais == 0:
#         print("Vous n'avez pas le bon nombre")
#         break
#     else:
#         print("Vous avez trouvé le nombre correct")
#         break

# longueur = int(11)
# espace = ' '
# ligne = ''
# for i in range(1,longueur):
#     print((espace * 5) + ('*' * i))

# nombre = int(input("Donne un nombre entre 5 et 10 : "))
# etoiles = '*'
# for i in range(1, nombre+1):
#     print((nombre - 1) * ' ', etoiles)
#     etoiles += '**'
#     nombre -= 1