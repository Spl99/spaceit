import requests

API_BASE_URL = 'https://api.spacetraders.io/v2'
API_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiRUNITzIxOSIsInZlcnNpb24iOiJ2MiIsInJlc2V0X2RhdGUiOiIyMDIzLTA2LTI0IiwiaWF0IjoxNjg3ODA1MTAxLCJzdWIiOiJhZ2VudC10b2tlbiJ9.BolqyES2MSRS-UxmUGrNvG4xjqtHuy16kP7IpuKSF95R1p79PgV0f275AozyGy1CtgWw83dqpo1tEzDw1DneBQLO7ZcZGQLdE5anhZ6w0aJhjc2ZGO7Xk0nFn_Qv39EoCcQDvk5zlwGhXmcGc6RoXS3FF5Q4ER8zluubux-r6gxMGjImYIAif1XX4czfmNIy9MmoGx13TyZ-bG8U2YnJkJcIzXWPH7pa6f4p4ca9OcgVDZLO_7CP-5PVm4HBvNBcyqzxJsGuGD1aKGz4lMjEUC4S6XTtrurlyBmBM7OBxaY5fJKkOAcG0nqgXGphGh1gRWiUxtU6wp3-KbbAb9xUeQ'

def agent_details():

     url = f'{API_BASE_URL}/my/agent'
     headers = {
            'Authorization': f'Bearer {API_TOKEN}'
     }

     response = requests.get(url, headers=headers)

     print(response.status_code)
     print(response.json())
    

def contract_details():

     url = f'{API_BASE_URL}/my/contracts'
     headers = {
            'Authorization': f'Bearer {API_TOKEN}'
                }
     response = requests.get(url, headers=headers)
     print (response.json())


def menu():
    global choice
    print("Menu")
    print("1. Agent Details")
    print ("2. Contact Details")

    choice = input("Enter an option")

    if choice == "1":
        agent_details()
    elif choice == "2":
        contract_details()
    elif choice == "0":
        print("Exiting....")

    else:
        print("Invalid, try again")

while True:
    menu()
    if choice == "0":
        break




