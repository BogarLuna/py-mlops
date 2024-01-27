import requests
from requests.exceptions import HTTPError
from typing import Dict, List, Any

# # https://rickandmortyapi.com/documentation
# rick= requests.get('https://rickandmortyapi.com/api')
# print(rick.json())

# rick= requests.get('https://rickandmortyapi.com/api/character')
# print(rick.json())


# #https://openlibrary.org/dev/docs/api/search
# open_library= requests.get('https://openlibrary.org/search.json')
# print(open_library.status_code)
# print(open_library.json())

def get_web_data(url:str,params:Dict={}):
    response= requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()
    
