class Pokemon:
    def __init__(self, tipo, especie,nivel=1,nome=None):
        self.tipo = tipo
        self.especie = especie
        self.nivel = nivel
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return f'{self.nome}({self.nivel})'.capitalize()
    
    def atacar(self, pokemon):
        print(f'{self} atacou {pokemon}')


class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print(f'{self} lançou um choque do trovão em {pokemon}')


meu_pokemon = Pokemon('fogo','charmander')
outro_pokemon = PokemonEletrico('eletrico','pikachu')

outro_pokemon.atacar(meu_pokemon)
meu_pokemon.atacar(outro_pokemon)


