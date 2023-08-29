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


if __name__ =='__main__':
    print('------------------------------------')
    print('Bem-vindo ao Pokemon RPG de terminal')
    print('------------------------------------')

    nome = input('Olá, qual é o seu nome?: ')
    player = Jogador(nome)
    print(f'Olá {player}, esse é um mundo habitado por pokemons,'
          'a partir de agora sua missão é se tornar um mestre pokemon!!!')
    print('Capture o maximo de pokemons que conseguir e lute com seus inimigos')
    player.mostrar_dinheiro()

    if player.pokemons:
        print('Já vi que você tem alguns pokemons')
        player.mostrar_pokemons()
    else:
        print('Você não tem nenhum pokemon, você precisa escolher um')
        escolher_pokemon_inicial(player)

    print('Pronto, agora que você já possui um pokemon, enfrente seu arqui-rival desde o jardim de infância, Gary')
    gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle',nivel=1)])
    player.batalhar(gary)
    
    while True:
        print('------------------------------------')
        print('O que deseja fazer?')
        print('1 - Explorar o mapa')
        print('2 - Lutar com um inimigo')
        print('0 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo...')
            break
        elif escolha == '1':
            player.explorar()
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
        else:
            print('Escolha inválida')