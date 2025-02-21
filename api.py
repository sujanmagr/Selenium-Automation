#api automation 
import requests
import json

api=api="https://reqres.in/api/users"
response=requests.get(api)

data=response.json()
data1=json.dumps(data, indent=4)
print(data1)