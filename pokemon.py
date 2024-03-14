class Pokemon:
    def __init__(self,nom,price,types,pv,niveau,attaque,attaqueSpe,defence,defenceSpe,vitesse):
        self.nom=nom
        self.price=price
        self.types=types
        self.pv=pv
        self.niveau=niveau
        self.attaque=attaque
        self.attaqueSpe=attaqueSpe
        self.defence=defence
        self.defenceSpe=defenceSpe
        self.vitesse=vitesse
        self.listAttaque=[]

    def ajouter_attaque(self,attaque):
        self.listAttaque.append(attaque)
    
    def attaquer(self,attque,pokemonEnnemi):
        print(f"{pokemonEnnemi} utilise {pokemonEnnemi}!")
        print(f"{self.attaque} inflige des dégâts à l'adversaire!")

        
    def est_ko(self,pv):
        if(pv<0):
            return True
    
    def afficher_attaques(self):
        for i in self.listAttaque:
            print(i)
        
    def afficher(self):
        print(self.nom)
        print(self.niveau)
        print(self.price)
        print(self.defence)
        print(self.attaque)
        print(self.pv)