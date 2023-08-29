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
    
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

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
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
        
    def mostrar_dinheiro(self):
        print(f'Você possui $ {self.dinheiro}')
    
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'Você ganhou $ {quantidade}')
        self.mostrar_dinheiro()


    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}!')
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon_jogador = self.escolher_pokemon()

        if pokemon_inimigo and pokemon_jogador:
            while True:
                vitoria = pokemon_jogador.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha')
                    self.ganhar_dinheiro(pokemon_inimigo.nivel * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon_jogador)
                if vitoria_inimiga:
                    print(f'{pessoa} ganhou a batalha')
                    break
        else:
            print('Essa batalha não pode ocorrer')



class Jogador(Pessoa):
    tipo = 'jogador'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')

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

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f'Um pokemon selvagem apareceu: {pokemon}')
            
            escolha = input('Deseja capturar o pokemon? (s/n): ')
            if escolha == 's':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print('Pokemon fugiu')
            else:
                print('OK, boa viagem')
        else:
            print('Nenhum pokemon encontrado')

class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)
    
