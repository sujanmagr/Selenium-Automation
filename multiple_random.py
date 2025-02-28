#scripts to post data to api
import requests
import json
import string
import random

api="https://reqres.in/api"
authorization_token="token any.token"
#to generate random email
def generate_random_email():
    domain="gmail.com"
    email_length=5
    random_string=''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email=random_string+"@"+domain
    return email
#to generate random name
def generate_name():
    return ''.join(random.choices(string.ascii_lowercase, k=7))

#to generate random phone numbers
def generate_number():
    return "980"+''.join(random.choices(string.digits, k=7))
#to chose a random job
def chose_job():
    job=["QA", "web designer", "cyber security", "data scientist"]
    return random.choice(job)
def post_multiple():
    url=api+"/users"
    headers={"Authorization": authorization_token}
   

    data={
        "name":generate_name(),
        "job":chose_job(),
        "email":generate_random_email(),
        "phone":generate_number()

        
        }
    response=requests.post(url, json=data, headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data, indent=4)
    assert response.status_code==201
    user_id=json_data["id"]
    print("the detai of created user is:", json_str)
    print("the id is :", user_id)

for _ in range (5):
    newuser=post_multiple()
    