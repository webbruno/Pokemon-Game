import random

from pokemon import *


NOMES = ['Jessie','James','Proton','Petrel','Ariana','Archer'
            ,'Pierce','Zager','Namba','Cassidy','Butch','Madame Boss']

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Flarion'),
    PokemonFogo('Vulpix'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonEletrico('Pichu'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Magicarp')
]

class Pessoa:
    
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome
    
    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}')
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} não tem nenhum pokemon')


class Jogador(Pessoa):
    tipo = 'jogador'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)
