import requests 
import json 

def metodoPut():
    url='http://httpbin.org/put'
    payload = {
        'nombre': 'Juan',
        'curso': 'Python'
    }
    
    response = requests.put(
        url,
        params= payload,
    )
    print(response)
    
    if response.status_code == 200:
        print('hola')
        print(response.text)
        
        
def metodoDelete():
    url='http://httpbin.org/delete'
    payload = {
        'nombre': 'Juan',
        'curso': 'Python'
    }
    
    response = requests.delete(
        url,
        params= payload,
    )
    print(response)
    
    if response.status_code == 200:
        print(response.text)
        
metodoDelete()