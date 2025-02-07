import requests

base_url = "https://pokeapi.co/api/v2/"



def get_pokemon_info(name):
    pass
    print("hello")
    url = f"{base_url}/pokemon/{name}"
    #use get method from requests to access the url
    response = requests.get(url)
    print(response)
    # response = 200 -> means ok
    if response.status_code == 200:
        print("data retrieved")
        # a response is a json format
        # use json method of response object to access key value pairs of response json
        pokemon_data = response.json()
        #print(pokemon_data)
        #return that json dictionary to fn output
        return pokemon_data
    else:
        print(f"failed to retrieve data {response.status_code}")



#pokemon_name = "pikachu"
pokemon_name = "typhlosion"

pokemon_info = get_pokemon_info(pokemon_name)

pokemon_info

if pokemon_info:
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["height"]}")
    print(f"{pokemon_info["weight"]}")
    