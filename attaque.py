class Attaque:
    def __init__(self,nom,type_attaque,categorie,precision,puissance,pp):
        self.nom=nom,
        self.type_attaque=type_attaque,
        self.categorie=categorie,
        self.precision=precision,
        self.puissance=puissance,
        self.pp=pp,
    
    def calculer_degats(self):
        print