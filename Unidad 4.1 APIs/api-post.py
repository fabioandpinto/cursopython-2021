from email import header
import requests
import json 

def metodoPostSimple(): 
    url = 'http://httpbin.org/post'
    payload = {
        'nombre': 'Juan',
        'curso': 'Python'
    }
    
    response = requests.post(url)
    
    if response.status_code == 200:
        print(response.text)
        
def metodoPostArgs():
    url = 'http://httpbin.org/post'
    payload = {
        'nombre': 'Juan',
        'curso': 'Python'
    }
    
    response = requests.post(url, data= json.dumps(payload))
    
    if response.status_code == 200:
        print(response.text)

def metodoPostEncabezado():
    url = 'http://httpbin.org/post'
    payload = {
        'nombre': 'Juan',
        'curso': 'Python'
    }
    headers = {
        'content-type': 'application/json',
        'access-token': '12345', 
        'secret_id': 'yu98lo6789'
    }
    
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers
    )
    
    if response.status_code == 200:
        print(response.text)
    
    
    
metodoPostEncabezado()