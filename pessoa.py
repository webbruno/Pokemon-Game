import random

from pokemon import *


NOMES = ['Jessie','James','Proton','Petrel','Ariana','Archer'
            ,'Pierce','Zager','Namba','Cassidy','Butch','Madame Boss']

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

