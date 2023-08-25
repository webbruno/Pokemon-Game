class Pokemon:

    def __init__(self, especie,nivel=1,nome=None):
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
    tipo = 'Elétrico'
    def atacar(self, pokemon):
        print(f'{self} lançou um choque do trovão em {pokemon}')


class PokemonFogo(Pokemon):
    tipo = 'Fogo'

    def atacar(self, pokemon):
        print(f'{self} lançou uma bola de fogo em {pokemon}')


class PokemonAgua(Pokemon):
    tipo = 'Água'

    def atacar(self, pokemon):
        print(f"{self} lançou um jato d'água em {pokemon}")

