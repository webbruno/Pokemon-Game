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
            for n,pokemon in enumerate(self.pokemons):
                print(n,f'- {pokemon}')
        else:
            print(f'{self} não tem nenhum pokemon')

    def escolher_pokemon(self):
        print('Escolha o seu pokemon para a batalha!')
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                try:
                    escolha_pokemon = int(input('Pokemon: '))
                    pokemon_escolhido = self.pokemons[escolha_pokemon]
                    print(f'{pokemon_escolhido.especie} eu escolho você!!!')
                    return pokemon_escolhido
                except ValueError:
                    print('Escolha inválida, digite o número do pokemon na lista')
                except IndexError:
                    print('Escolha inválida, pokemon não existe na lista')
        else:
            print('Esse jogador não possui nenhum pokemon para ser escolhido')

    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}!')
        pessoa.mostrar_pokemons()
        pessoa.escolher_pokemon()
        self.escolher_pokemon()


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

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
