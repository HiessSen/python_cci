class CompteBancaire:
    def __init__(self, solde=0):
        self.solde = solde
    def depot(self, montant):
        self.solde += montant
    def retrait(self, montant):
        self.solde -= montant

    def afficher_solde(self):
        reponse = "Le compte du client est "
        if self.solde > 0:
            reponse+= f"crediteur de {self.solde} €."
        elif self.solde < 0:
            reponse+= f"debiteur de {-self.solde} €."
        else:
            reponse += "vide, allez travailler chez Via"
        return reponse

compte_de_ilan = CompteBancaire(800)
print(compte_de_ilan.afficher_solde())
compte_de_ilan.retrait(5000)
print(compte_de_ilan.afficher_solde())
compte_de_ilan.depot(6400)
print(compte_de_ilan.afficher_solde())
compte_de_imran = CompteBancaire()
print(compte_de_imran.afficher_solde())
compte_de_romain = CompteBancaire(400)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
compte_de_romain.retrait(9)
print(compte_de_romain.afficher_solde())

class CompteEpargne(CompteBancaire):
    def __init__(self, solde, taux_interet):
        super().__init__(solde)
        self.taux_interet = taux_interet
    def ajouter_interets(self, montant):
        self.taux_interet += montant

    def afficher_informations(self):
        super().afficher_solde()
        self.solde += (self.solde * self.taux_interet) / 100
        reponse = f"Le taux d'interet est de {self.taux_interet} %, ce qui fait un solde total de {self.solde}"
        return reponse

compte_epargne_de_ilan = CompteEpargne(8000, 1.5)
print(compte_epargne_de_ilan.afficher_solde())
compte_epargne_de_ilan.ajouter_interets(2.3)
print(compte_epargne_de_ilan.afficher_informations())
