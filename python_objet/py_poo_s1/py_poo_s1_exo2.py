from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def parler(self):
#         pass
# class Chien(Animal):
#     def parler(self):
#         reponse = "Wouf wouf !"
#         return reponse
# class Chat(Animal):
#     def parler(self):
#         reponse = "Miaou miaou !"
#         return reponse
# def faire_parler(animal):
#     return animal.parler()
# babouche = Chien()
# print(faire_parler(babouche))
# ades = Chien()
# print(faire_parler(ades))
# neo = Chat()
# print(faire_parler(neo))
# fefe = Chat()
# print(faire_parler(fefe))


# class Employe:
#     def __init__(self, nom, salaire):
#         self._nom = nom
#         self._salaire = salaire
#     @property
#     def nom(self):
#         return self._nom
#     @property
#     def salaire(self):
#         return self._salaire
#     def afficher_salaire(self):
#         return f"Vous gagnez {self._salaire}"
# class Manager(Employe):
#     def __init__(self, nom, salaire, bonus):
#         super().__init__(nom, salaire)
#         self.__bonus = bonus
#     @property
#     def bonus(self):
#         return self.__bonus
#     def calculer_salaire_total(self):
#         salaire = self._salaire + self.__bonus
#         return salaire
#     def afficher_salaire(self):
#         return f"Vous gagnez {self.calculer_salaire_total()}"
# ilan = Employe("Ilan", 2500)
# print(ilan.afficher_salaire())
# florian = Manager("Florian", 3500, 450)
# print(florian.afficher_salaire())

# class Vehicule(ABC):
#     def __init__(self, marque):
#         self._marque = marque
#     @property
#     def marque(self):
#         return self._marque
#     @abstractmethod
#     def moteur(self):
#         pass
# class Voiture(Vehicule):
#     def __init__(self, marque):
#         super().__init__(marque)
#     def moteur(self):
#         return "Moteur essence"
# class Moto(Vehicule):
#     def __init__(self, marque):
#         super().__init__(marque)
#     def moteur(self):
#         return "Moteur éléctrique ?"
# megane = Voiture("Renault")
# mt07 = Moto("Kawa")
# print(megane.moteur())
# print(mt07.moteur())

class Employe:
    def __init__(self, nom, salaire):
        self._nom = nom
        self._salaire = salaire
    @property
    def nom(self):
        return self._nom
    @property
    def salaire(self):
        return self._salaire
    def afficher_informations(self):
        reponse = f"{self._nom} touche {self._salaire} €"
        return reponse
class Developpeur(Employe):
    def __init__(self, nom, salaire, langages=None):
        super().__init__(nom, salaire)
        self._langages = langages
    def afficher_informations(self):
        reponse = f"{self._nom} touche {self._salaire} €"
        return reponse
    def coder(self):
        liste_langages = ""
        if self._langages is None:
            reponse = f"{self.afficher_informations()} sans coder"
            return reponse
        else:
            if len(self._langages) == 1:
                liste_langages += self._langages[0]
            else:
                for i in range(len(self._langages)):
                    if i < len(self._langages)-1:
                        liste_langages += f"{self._langages[i]}, "
                    else:
                        liste_langages += f"et {self._langages[i]}"
            reponse = f"{self.afficher_informations()} en travaillant avec {liste_langages}"
            return reponse
alicia = Employe("alicia", 5151)
print(alicia.afficher_informations())
patrick = Developpeur("patrick", 4050)
print(patrick.afficher_informations())
alain = Developpeur("Alain", 1550, ["javascript",])
print(alain.coder())
sophie = Developpeur("Sophie", 7000, ["javascript", "PHP", "Python"])
print(sophie.coder())

class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age
    @property
    def nom(self):
        return self._nom
    @property
    def age(self):
        return self._age
    def afficher_informations(self):
        reponse = f"Je m'appelle {self.nom} et j'ai {self.age}"
        age = "ans" if self._age > 1 else "an"
        return f"{reponse} {age}"
class Etudiant(Personne):
    def __init__(self, nom, age, niveau):
        super().__init__(nom, age)
        self._niveau = niveau
    @property
    def niveau(self):
        return self._niveau
    def afficher_informations(self):
        informations_generales = super().afficher_informations()
        reponse = f"{informations_generales}. Je suis en {self.niveau}"
        return reponse
caroline = Personne("Caroline", 24)
print(caroline.afficher_informations())
nova = Personne("Nova Leia", 1)
print(nova.afficher_informations())
jeannine = Etudiant("Jeannine", 25, "licence")
print(jeannine.afficher_informations())