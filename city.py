import urllib.request
from pokemon import Pokemon

class City():
    available_cities_objects = []

    def __init__(self, name,available_pokemon_object=None):
        self.name = name
        self.available_pokemon_object = available_pokemon_object
        City.available_cities_objects.append(self)

    def get_distance_from(self, city_object):
        url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}".format(self.name, city_object.name)
        web_obj = urllib.request.urlopen(url)
        results_string = str(web_obj.read())
        web_obj.close()
        asd = results_string.split(" ")[87].replace('"', '')
        return asd

    @classmethod
    def print_available_cities_with_pokemon(cls):
        for city in cls.available_cities_objects:
            if city.available_pokemon_object != None:
                print("There is a {} in {}".format(city.available_pokemon_object, city.name))
            else:
                print("There is no pokémon here :D")


budapest = City("Budapest", Pokemon("charizard","fire/flying"))
kaposvar = City("Kaposvar")

x = budapest.get_distance_from(kaposvar)

print(x)
City.print_available_cities_with_pokemon()
