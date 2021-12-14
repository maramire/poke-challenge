import utils.http as http

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'


def count_special_pokemon():
    """Return all pokemon that contains 'at' and have 2 a's
    """

    # make the first request to find total number of pokemon
    pokemon_count = http.get(BASE_URL).get('count')

    # fetch all pokemon
    all_pokemon = http.get(BASE_URL + f'?limit={pokemon_count}').get('results')

    count = 0
    for pokemon in map(lambda p: p.get('name'), all_pokemon):
        # check if pokemon name contains 'at' and it has exactly two a's
        if "at" in pokemon and pokemon.count('a') == 2:
            count += 1
    return count


print(count_special_pokemon())
