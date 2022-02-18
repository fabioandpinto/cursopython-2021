import requests 
import json 


def getPokemon(limit):
    url = 'https://pokeapi.co/api/v2/pokemon'
    args = {
        'limit':limit
    }
    response = requests.get(url, params = args )
    
    if response.status_code == 200:
        data = response.json()
        resultados = data.get('results')
        
        for pokemon in resultados: 
            print(pokemon['name'])
      
def getPokemonByNumber(n):
    url = 'https://pokeapi.co/api/v2/pokemon/'+str(n)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()      
        print('El pokemon solicitado es ' + data['species']['name'])
        
        
getPokemonByNumber(280)
    
    
    