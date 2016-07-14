

class Pokemon:
    pokedex = []

    def __init__(self, name, pokemon_type):
        self.name = name
        self.pokemon_type = pokemon_type
        self.xp = 0
        Pokemon.pokedex.append(self)

    def __str__(self):
        return "name:{}, pokemon_type: {} and xp: {}".format(self.name, self.pokemon_type, self.xp)

    @classmethod
    def print_pokedex(cls):
        for pokemon in cls.pokedex:
            print(pokemon)

    @staticmethod
    def get_pokemon_object_name(pokemon_object):
        return pokemon_object.name
