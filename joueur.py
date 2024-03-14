from pokemon import Pokemon

class Joueur:
    
    def __init__(self, nom, manche_win, argent):
        self.nom = nom
        self.manche_win = manche_win
        self.argent = argent
        self.listPokemons = [
            Pokemon(nom="Noml", price=100, types="Feu", pv=100, niveau=1, attaque=50, attaqueSpe=60, defence=40, defenceSpe=30, vitesse=70),
            Pokemon(nom="No", price=100, types="Feu", pv=100, niveau=1, attaque=50, attaqueSpe=60, defence=40, defenceSpe=30, vitesse=70),
            Pokemon(nom="Le", price=100, types="Feu", pv=100, niveau=1, attaque=50, attaqueSpe=60, defence=40, defenceSpe=30, vitesse=70)
        ]
        self.pokemons_choisis = []  # Initialisation de la liste des Pokémons choisis
    
    def choisir_pokemon(self):
        # Afficher la liste des Pokémons disponibles.
        print("Pokémons disponibles :")

        for pokemon in self.listPokemons:
            print(f"{pokemon}. {pokemon.nom} - PV: {pokemon.pv} - Attaque: {pokemon.attaque}")
        
        # Permettre au joueur de choisir jusqu'à 3 Pokémons.
        while len(self.pokemons_choisis) < 3:
            try:
                choix = int(input("Choisis ton Pokémon (numéro) : ")) - 1
                if 0 <= choix < len(self.listPokemons):
                    pokemon_choisi = self.listPokemons[choix]
                    if pokemon_choisi not in self.pokemons_choisis:
                        self.ajouter_pokemon(pokemon_choisi)
                    else:
                        print("Ce Pokémon a déjà été choisi.")
                else:
                    print("Choix invalide, veuillez réessayer.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    def ajouter_pokemon(self, pokemonChoisi):
        # Ajout du Pokémon choisi à la liste des Pokémons du joueur.
        self.pokemons_choisis.append(pokemonChoisi)
        print(f"{pokemonChoisi.nom} a été ajouté à votre équipe !")
        
    # Autres méthodes...
    def choisir_attaque(self, pokemonChoisi):        
        for attaque in pokemonChoisi.listAttaque:
            print(attaque)
        
    def recuperer_pokemon(self, numero_pokemon):
        if 0 <= numero_pokemon < len(self.pokemons_choisis):
            return self.pokemons_choisis[numero_pokemon]
        else:
            print("Numéro de Pokémon invalide.")
            return None
        
    def afficher_pokemons(self):
        for pokemon in self.pokemons_choisis:
            print(pokemon.nom)
            print(pokemon.types)
            print(pokemon.pv)
            print(pokemon.niveau)
            print(pokemon.attaque)
            print(pokemon.attaqueSpe)
            print(pokemon.defence)
            print(pokemon.defenceSpe)
            print(pokemon.vitesse)
        
    def afficher(self):
        print(self.nom)
        print(self.manche_win)
        print(self.argent)
        for pokemon in self.listPokemons:
            print(pokemon.nom)
