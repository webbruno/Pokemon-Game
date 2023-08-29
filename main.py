from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(jogador):
    print(f'Olá {jogador}, você pode escolher o seu Pokemon que irá lhe acompanhar nessa jornada!')

    pikachu = PokemonEletrico('Pikachu', nivel=1)
    charmander = PokemonFogo('Charmander', nivel=1)
    squirtle = PokemonAgua('Squirtle', nivel=1)

    print('Você possui 3 escolhas: ')
    print('1 - ', pikachu)
    print('2 - ', charmander)
    print('3 - ', squirtle)

    while True:
        escolha = input('Escolha o seu Pokemon: ')

        if escolha == '1':
            jogador.capturar(pikachu)
            break
        elif escolha == '2':
            jogador.capturar(charmander)
            break
        elif escolha == '3':
            jogador.capturar(squirtle)
            break


jogador1 = Jogador('Bruno',pokemons=[PokemonAgua('Squirtle',nivel=1)])
jogador1.mostrar_dinheiro()
# inimigo = Inimigo(nome='Gary',pokemons=[PokemonFogo('Charmander',nivel=1)])

# jogador1.batalhar(inimigo)

jogador1.explorar()