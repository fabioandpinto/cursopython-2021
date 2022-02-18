# pip install requests 

import requests 

# GET  - POST - PUT - DELETE 
def getSimple(): 
    url = 'https://www.google.com.co'
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content
        
        file = open('google.html', 'wb')
        file.write(content)    
    
def getService1(): 
    url = 'http://httpbin.org/get'
    response = requests.get(url)
    print(response.text)
    
def getServiceArgs():
    url = 'http://httpbin.org/get?nombre=eliana'
    response = requests.get(url)
    print(response.text)
    
def getServiceArgs2():
    url = 'http://httpbin.org/get'
    args = {
        'nombre': 'eliana', 
        'curso': 'python', 
        'empresa': 'Agrosavia'
    }
    
    response = requests.get(url, params= args)
    
    if response.status_code == 200: 
        content = response.text
        print(response.url)
    

def getServiceJson():
    url = 'http://httpbin.org/get'
    args = {
        'nombre': 'eliana', 
        'curso': 'python', 
        'empresa': 'Agrosavia'
    }
    response = requests.get(url, params= args)
    if response.status_code == 200: 
        json = response.json()
        print( "El origen de la peticion es " + str(json['origin']))

       
        
getServiceJson()
