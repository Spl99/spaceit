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
    system_names = []
    
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
        system_names.append(symbol)

    #Plottig to graph
    plt.scatter(x_locations, y_locations)
    plt.xlabel('X Location')
    plt.ylabel('Y Location')
    plt.title("Space Stuff")
    plt.grid(True)
    

    # Add names when hover over system on map
    for i in range(len(system_names)):
        plt.annotate(system_names[i], (x_locations[i], y_locations[i]), textcoords="offset points", xytext=(0, 10), ha='center')


    plt.show()


def list_ships():
    url = f'{API_BASE_URL}/my/ships'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    
    ships = data['data']
    system_symbols = []
    for ships in ships:
        #symbol = ships['symbol']
        name = ships['registration']['name']
        role = ships['registration']['role']
        system_name = ships['nav']['systemSymbol']
        system_symbols.append(system_name)
        exact_location = ships['nav']['waypointSymbol']
        current_status = ships['nav']['status']

        print(f"Ship Name: {name}, Role: {role}, Current System: {system_name}, Exact Location: {exact_location}, Current Status: {current_status}")
    for system_symbol in system_symbols:

        show_system(system_symbol)

# Try to plot current system
def show_system():
    url = f'{API_BASE_URL}/systems'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    
    system_names = []
    x_cords = []
    y_cords = []
    for system in data['systems']:
        system_name = system['symbol']
        x = system['x']
        y = system['y']
        system_names.append(system_name)
        x_cords.append(x)
        y_cords.append(y)

    plt.figure(figsize=(10, 6))
    plt.scatter(x_cords, y_cords)
    for i, system_name in enumerate(system_names):
        plt.annotate(system_name, (x_cords[i], y_cords[i]))
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('System Locations')
    plt.grid(True)
    plt.show()



#universe_status()
list_ships()
show_system()
