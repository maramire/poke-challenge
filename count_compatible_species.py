import utils.http as http
import sys

BASE_URL = 'https://pokeapi.co/api/v2/'


def count_compatible_species(specie_name):
    """Return number of compatible pokemon species that can interbreed
    """

    specie = http.get(BASE_URL + f'pokemon-species/{specie_name}')
    egg_groups = specie.get('egg_groups')

    compatible_species = set()
    for egg_group_url in map(lambda e: e.get('url'), egg_groups):
        egg_group_species = http.get(egg_group_url).get('pokemon_species')
        compatible_species.update(
            [pokemon.get('name') for pokemon in egg_group_species if pokemon.get('name') != specie_name])
    return len(compatible_species)


if __name__ == "__main__":
    try:
        specie_name = sys.argv[1]
    except IndexError:
        print('Please insert a valid command line.')
    else:
        print(count_compatible_species(specie_name))
