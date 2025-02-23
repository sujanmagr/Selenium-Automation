#scripts to post data to api
import requests
import json

api="https://reqres.in/api"
authorization_token="token any.token"

def post_api():
    url=api+"/users"
    headers={"Authorization": authorization_token}
    data=[{
        "name":"sujan",
        "job":"QA tester",
        "email":"aaa@gmail.com"
    },{
        "name":"sujjan",
        "job":"mayalu",
        "email":"mayalu@gmail.com"

    }]
    response=requests.post(url, json=data, headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data, indent=4)
    assert response.status_code==201
    # user_id=json_data["id"]
    print("the data is:", json_str)
    # print("the id is :", user_id)
post_api()