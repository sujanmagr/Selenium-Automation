#scripts to post data to api
import requests
import json

api="https://reqres.in/api"
authorization_token="token any.token"

def post_multiple(user_names):
    url=api+"/users"
    headers={"Authorization": authorization_token}
    user_ids=[]
    for name in user_names:
        data={
        "name":name,
        "job":"QA tester"
        
            }
        response=requests.post(url, json=data, headers=headers)
        json_data=response.json()
        json_str=json.dumps(json_data, indent=4)
    # assert response.status_code==201

        user_id=json_data["id"]
        print("the data is:", json_str)
    # print("the id is :", user_id)
        if user_id:
            user_ids.append(user_id)
            assert response.status_code==201
            assert "name" in json_data
            print("post multiple user is success", name)
    return user_ids
user_names=["sujan", "sachin", "saroj"]
user_id=post_multiple(user_names)
print("the uer id created are: ", user_id)
    


