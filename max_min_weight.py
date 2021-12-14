import utils.http as http
import utils.async_http as async_http
import asyncio

BASE_URL = 'https://pokeapi.co/api/v2/'


async def max_min_weight():
    # request first generation pokemon resource urls
    first_gen = http.get(BASE_URL + f'pokemon?limit=151').get('results')
    first_gen = [p.get('url') for p in first_gen]
    # request fighting pokemon resource urls
    fighting_pokemon = http.get(BASE_URL + f'type/fighting').get('pokemon')
    fighting_pokemon = [p.get('pokemon').get('url') for p in fighting_pokemon]

    # filter fighting first gen pokemon
    pokemon_urls = [url for url in first_gen if url in fighting_pokemon]

    # collect pokemon data asynchronously from pokemon urls
    pokemons = await async_http.get(pokemon_urls)
    # filter only weights
    weights = [p.get('weight') for p in pokemons]

    print([max(weights), min(weights)])


asyncio.run(max_min_weight())
