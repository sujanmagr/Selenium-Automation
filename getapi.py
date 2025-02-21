#api automation with function
import requests
import json
#send api url
api="https://reqres.in"

def get_request():
    url=api+"/api/users"
    response=requests.get(url)
    assert response.status_code==200
    json_data=response.json()
    json_str = json.dumps(json_data, indent=4)
    print("ther returned users for the api are: ", json_str)
    print("----------------")

get_request()