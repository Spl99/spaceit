# Attempt at a graphical version of Space Traders

import requests
import config
import matplotlib.pyplot as plt

API_BASE_URL = 'https://api.spacetraders.io/v2'
API_TOKEN = config.API_TOKEN

def universe_status():
    url = f'{API_BASE_URL}/systems'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    x_locations = []
    y_locations = []

    response = requests.get(url, headers=headers)
    data = response.json()
    systems = data['data']

    for system in systems:
        symbol = system['symbol']
        planet_type = system['type']
        x_location = system['x']
        y_location = system['y']
        print(symbol, planet_type, x_location, y_location)

        x_locations.append(x_location)
        y_locations.append(y_location)

    #Plottig to graph
    plt.scatter(x_locations, y_locations)
    plt.xlabel('X Location')
    plt.ylabel('Y Location')
    plt.title("Space Stuff")
    plt.grid(True)
    plt.show()

universe_status()
