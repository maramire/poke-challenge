import utils.http as http
import sys

BASE_URL = 'https://pokeapi.co/api/v2/'


def count_compatible_species(specie_name):
    """Return number of compatible pokemon species that can interbreed
    """

    specie = http.get(BASE_URL + f'pokemon-species/{specie_name}')
    egg_groups = [group.get('url') for group in specie.get('egg_groups')]

    compatible_species = set()
    for url in egg_groups:
        # request egg group species
        egg_group_detail = http.get(url)
        egg_group_species = egg_group_detail.get('pokemon_species')
        # update set of compatible species discarding 'specie_name' param
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
