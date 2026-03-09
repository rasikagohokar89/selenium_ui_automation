import requests
import json


base_url = "https://dummyjson.com"
end_point = "/auth/login"
url = base_url + end_point

headers = {
    "Content-Type": "application/json"
}

payload = {
    "username":"kminchelle",
    "password":"0lelplr",
    "expiresInMins":30
}

json_data = json.dumps(payload)

response = requests.post(url,headers=headers,json=payload)
print(response)
print(response.json())