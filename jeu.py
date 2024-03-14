from joueur import Joueur
from pokemon import Pokemon


class Jeu:
    def __init__(self):
       self.listJoueur=[]
       
    def jouer(self):
        nom1=input("Entrez votre nom : ")
        joueur=Joueur(argent=500,nom=nom1,manche_win=0)
        nom2=input("Entrez votre nom joueur 2: ")
        joueur2=Joueur(argent=500,nom=nom2,manche_win=0)
        self.listJoueur=[joueur2,joueur]
        for joueur in self.listJoueur:
            joueur.choisir_pokemon(self.listJoueur)
            joueur.ajouter_pokemon(self.listJoueur)  

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()