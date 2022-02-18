# marvel 
# pip install marvel 

from asyncio import proactor_events
from marvel import Marvel
from numpy import character 
import pandas as pd 

public_key = '80ce30cf06c3205a2ebb63006623c42a'
private_key = '75a8f454c65a49c7f66015c8e107b26cae05946a'

m = Marvel(public_key, private_key)

# Llamada 
character = m.characters

name = 'Spiderman'

personajes = m.characters.all(nameStartsWith = 'Doctor')

# for i in range(len(personajes['data']['results'])):
#     print(personajes['data']['results'][i]['name'])

per = personajes['data']['results']
    
data_personajes = pd.DataFrame(per)
data_personajes.to_excel('doctores.xlsx')
