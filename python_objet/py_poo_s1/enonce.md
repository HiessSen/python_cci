## Exercice 1 :
### Exercices de Base (Classes et Objets)
1. Créer une classe Personne avec les attributs nom et âge. Ajouter une méthode se_presenter() qui affiche le nom et l’âge de la personne.
2. Créer une classe Voiture avec les attributs marque, modèle et année. Ajouter une méthode afficher_infos() qui affiche ces informations.
3. Créer une classe CompteBancaire avec :
    - Un attribut solde (initialisé à 0).
    - Une méthode depot(montant).
    - Une méthode retrait(montant).
    - Une méthode afficher_solde().
4. Créer une classe Livre avec les attributs titre, auteur, et année_publication. Ajouter une méthode description() qui affiche les informations du livre.
5. Créer une classe Etudiant qui stocke nom, note1, note2. Ajouter une méthode moyenne() qui retourne la moyenne des notes.

## Exercice 2 :
### Exercices sur l’Héritage
1. Créer une classe Animal avec une méthode parler(), puis créer :
    - Une classe Chien qui redéfinit parler() en affichant "Woof !".
    - Une classe Chat qui redéfinit parler() en affichant "Miaou !".
    - Tester le polymorphisme avec une liste d’animaux et appeler parler() sur chacun.
2. Créer une classe Employe avec nom et salaire. Puis :
    - Une classe Manager qui hérite de Employe et ajoute bonus.
    - Une méthode calculer_salaire_total() qui additionne salaire + bonus.
3. Créer une classe Vehicule avec marque et moteur(), puis :
    - Une classe Voiture qui redéfinit moteur() en affichant "Moteur essence".
    - Une classe Moto qui redéfinit moteur() en affichant "Moteur électrique".
4. Créer une classe Employe et une sous-classe Developpeur qui ajoute un attribut langage et une méthode coder().
5. Créer une classe Personne et une sous-classe Etudiant avec un attribut supplémentaire niveau (Licence, Master, Doctorat).

## Exercice 3 :
### Exercices sur l’Encapsulation
1. Créer une classe CompteBancaire avec :
    - Un attribut privé __solde.
    - Des méthodes depot(montant), retrait(montant), et afficher_solde().
    - Vérifier qu’on ne peut pas modifier __solde directement.
2. Créer une classe Voiture avec :
    - Un attribut protégé _kilometrage (modifiable uniquement via une méthode ajouter_km(km)).
    - Une méthode get_kilometrage() qui retourne _kilometrage.
3. Créer une classe Utilisateur avec un attribut privé __mot_de_passe :
    - Une méthode changer_mdp(nouveau_mdp) qui met à jour le mot de passe.
    - Une méthode verifier_mdp(mdp) qui retourne True si le mot de passe est correct.
4. Créer une classe Article avec un prix privé __prix :
    - Une méthode set_prix(nouveau_prix) qui modifie __prix si nouveau_prix > 0.
    - Une méthode get_prix() qui retourne __prix.

## Exercice 4 :
### Exercices sur le Polymorphisme
1. Créer une classe Instrument avec une méthode jouer(), puis :
    - Une classe Guitare qui redéfinit jouer() en affichant "Joue de la guitare".
    - Une classe Piano qui redéfinit jouer() en affichant "Joue du piano".
    - Une liste contenant des objets Guitare et Piano, et appeler jouer() sur chacun.
2. Créer une classe Transport avec une méthode se_deplacer() :
    - Une classe Voiture qui redéfinit se_deplacer() en affichant "Se déplace sur la route".
    - Une classe Avion qui redéfinit se_deplacer() en affichant "Se déplace dans le ciel".
Tester le polymorphisme en appelant se_deplacer() sur chaque objet.
3. Créer une classe Media avec une méthode afficher_info() :
    - Une classe Livre qui redéfinit afficher_info().
    - Une classe Film qui redéfinit afficher_info().
    - Une fonction qui prend un objet Media et affiche les informations.


## Exercice 5 :
### Exercices sur les Classes Abstraites et Interfaces
1. Créer une classe abstraite Forme avec :
    - Une méthode calculer_aire() (abstraite).
    - Des sous-classes Cercle et Rectangle qui implémentent calculer_aire().
    - Tester avec plusieurs objets.
2. Créer une classe abstraite Employe avec :
    - Une méthode calculer_salaire().
    - Des sous-classes EmployeHoraire et EmployeSalarie qui redéfinissent calculer_salaire().
3. Créer une interface VehiculeInterface avec demarrer() et arreter(), puis :
    - Une classe Voiture qui implémente demarrer() et arreter().
    - Une classe Moto qui implémente demarrer() et arreter().
4. Créer une interface Jouable avec une méthode jouer(), et :
    - Une classe Footballeur qui l’implémente.
    - Une classe Musicien qui l’implémente.
    - Une fonction faire_jouer(objet) qui utilise le polymorphisme.
5. Créer une classe abstraite Animal avec :
    - Une méthode abstraite se_deplacer().
    - Des sous-classes Poisson (nage), Oiseau (vole), Serpent (rampe).
    - Une liste d’animaux et un appel à se_deplacer() pour chacun.
