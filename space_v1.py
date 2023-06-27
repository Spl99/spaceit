import requests
import config


API_BASE_URL = 'https://api.spacetraders.io/v2'
API_TOKEN = config.API_TOKEN


def agent_details():

    url = f'{API_BASE_URL}/my/agent'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    symbol = data['data']['symbol']
    headquarters = data['data']['headquarters']
    credits = data['data']['credits']

    print(f"Symbol: {symbol}")
    print(f"Headquarters: {headquarters}")
    print(f"Credits: {credits}")


    #print(response.status_code)
    #print(response.json())
    

def contract_details():
    url = f'{API_BASE_URL}/my/contracts'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
       
    response = requests.get(url, headers=headers)
    data = response.json()
    for contract in data['data']:
        contract_id = contract['id']
        contract_type = contract['type']
        deadline = contract['terms']['deadline']
        payment_on_fulfilled = contract['terms']['payment']['onFulfilled']
        deliveries = contract['terms']['deliver']

        print()
        print(f"Contract ID: {contract_id}")
        print(f"Contract Type: {contract_type}")
        print(f"Contract Deadline: {deadline}")
        print(f"Payment: {payment_on_fulfilled}")
        print("Delivery Requirements: ")
        print("=======================")

        for delivery in deliveries:
            trade_symbol = delivery['tradeSymbol']
            destination = delivery['destinationSymbol']
            units_required = delivery['unitsRequired']
            units_fulfilled = delivery['unitsFulfilled']


            print(f"Trade Symbol: {trade_symbol}")
            print(f"Destination: {destination}")
            print(f"Units Required: {units_required}")
            print(f"Units Fulfilled: {units_fulfilled}")
        
    accept = input("Do you want to accept the contract? Press '1' to accept")

    if accept == "1":
        url = f'{API_BASE_URL}/my/contracts/{contract_id}/accept'
        print(f"Contract {contract_id} accepted!")
    else:
        print("Fail")

    #print (response.json())

# Waypoints + Ships

def waypoints():
    url = f'{API_BASE_URL}/my/status'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)

   


def menu():
    global choice
    print()
    print("Menu")
    print("1. Agent Details")
    print("2. Contact Details")
    print("3. Waypoints")
    print("0. To exit")
    print()
    choice = input("Enter an option: ")

    if choice == "1":
        agent_details()
        print()
    elif choice == "2":
        contract_details()
    elif choice == "3":
        waypoints()
    elif choice == "0":
        print("Exiting...")
        
    else:
        print("Invalid, try again")

while True:
    menu()
    if choice == "0":
        break




