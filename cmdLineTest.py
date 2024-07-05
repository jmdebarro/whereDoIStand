import requests


### Gets input from user and returns standing ###
def statCalc():
    state = input("State: ")
    gender = input("Gender: ")
    income = int(input("Income: "))
    url = "http://127.0.0.1:8000/stats"
    payload = {"income": income, "gender": gender, "state": state, "weight": 0, "height": 0}

    response = requests.post(url, json=payload)
    print(response.json())


statCalc()
