import requests

def poke_profile(a_poke):
    url = f'https://pokeapi.co/api/v2/pokemon/{a_poke.lower()}'
    response = requests.get(url).json()
    s_url = f'https://pokeapi.co/api/v2/pokemon-species/{a_poke.lower()}'
    s_response = requests.get(s_url).json()
    poke_deets = {}
    poke_deets['name'] = a_poke.title()
    poke_deets['types'] = [response['types'][i]['type']['name'] for i in range(len(response['types'])) ]
    poke_deets['capture_rate'] = s_response['capture_rate']
    poke_deets['held_items'] = [response['held_items'][i]['item']['name'] for i in range(len(response['held_items'])) ] 
    response_stat_block = response['stats']
    poke_deets['stats'] = {response_stat_block[i]['stat']['name'] : response_stat_block[i]['base_stat'] for i in range(len(response_stat_block))}
    return poke_deets
    
print(poke_profile('ditto'))
