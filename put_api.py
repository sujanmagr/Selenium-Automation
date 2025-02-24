import requests
import json

api="https://reqres.in"
authorization_token="token token_value"

def put_request(user_id):
    url=api+ "/api/users/{user_id}"
    headers={"Authorization":authorization_token}
    data={
        "name":"sujan",
        "job":"QA",
        "email":"sjdf@gmail.com"
        }
    response=requests.put(url, json=data, headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data, indent=3)
    assert response.status_code==200
    print("the updated data is:", json_str)
 
put_request(2)
