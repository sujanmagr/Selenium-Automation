import requests
import json

api="https://reqres.in"
def login():
    url=api+"/api/login"
    data={
        "email": "eve.hot@reqres.in",
        "password": "cityslicka"
    }
    response=requests.post(url, json=data)
    json_data=response.json()
    json_str=json.dumps(json_data, indent=3)
    assert response.status_code==200
    print("login succssful as:", json_str)
login()