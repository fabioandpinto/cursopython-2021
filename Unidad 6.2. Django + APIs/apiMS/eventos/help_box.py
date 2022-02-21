import requests
import json
from .auth_helper import load_cache, get_msal_app


graph_url = 'https://graph.microsoft.com/v1.0/'

def get_user(token):
    # Hacer peticion get
    user = requests.get('{0}/me'.format(graph_url),
                                headers={
                                    'Authorization': 'Bearer {0}'.format(token)
                                },
                                params={
                                    '$select': 'displayName,mail,userPrincipalName'
                                }
                        )
    return user.json()

