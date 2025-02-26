# def max_de_trois(a,b,c):
#     le_plus_grand = 0
#     liste = [a,b,c]
#     for x in liste:
#         if x > le_plus_grand:
#             le_plus_grand = x
#     return le_plus_grand
# print(max_de_trois(12, 7841, 5))
import math


# def verifier_age(age):
#     if age >= 22:
#         return f"A {age} ans, vous êtes majeur."
#     elif 18 <= age < 22:
#         return f"A {age} ans, vous êtes majeur, mais tout juste !"
#     elif 18 > age >= 16:
#         return f"A {age} ans, vous êtes mineur. Patience, ça arrive très bientôt"
#     else:
#         return f"A {age} ans, vous êtes mineur."
# print(verifier_age(12))
# print(verifier_age(16))
# print(verifier_age(18))
# print(verifier_age(23))

# def signe_nombre(n):
#     if n < 0:
#         return f"{n} est un nombre négatif"
#     elif n > 0:
#         return f"{n} est un nombre positif"
#     elif n == 0:
#         return f"{n} est littéralement {n}"
#     else:
#         return f"{n} n'est pas une valeur acceptée, petit polisson"
# print(signe_nombre(5))
# print(signe_nombre(-5))
# print(signe_nombre(0))
# print(signe_nombre(7/5))

# def factorielle(n):
#     # return math.factorial(n)
#     f = 0
#     for i in range(1, n):
#         n *= i
#     return n
# print(factorielle(5))

# def est_palindrome(mot):
#     motInverse = ''
#     for i in range(len(mot)-1, -1, -1):
#         motInverse += mot[i]
#     if motInverse == mot:
#         return f"{mot} est un palindrome"
#     else:
#         return f"{mot} n'est pas un palindrome"
# print(est_palindrome('rotor'))
# print(est_palindrome('objet'))

