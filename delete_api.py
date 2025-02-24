import requests
import json

api="https://reqres.in"
authorization_token="token token_value"
def delete_user(user_id):
    url=api+"/api/users/{user_id}"
    headers={"Authorization": authorization_token}
    response=requests.delete(url,headers=headers )
    assert response.status_code==204
    print(f"data is deleted for id {user_id} ", response)
delete_user(2)
    