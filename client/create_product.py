import requests

endpoint = 'http://localhost:8000/api/V1/product/'  # vérifie bien ton URL
data = {
    "name": "patate",
    "price": 9.99,
    "description": "fruit",
    "Email": "user@example.com"
}

try:
    response = requests.post(endpoint, json=data)
    print("Status Code:", response.status_code)
    try:                                                                                    
        print("Response JSON:", response.json())
    except ValueError:
        print("Response Text:", response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
