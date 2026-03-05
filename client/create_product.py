import requests

endpoint = 'http://localhost:8000/api/'  # vérifie bien ton URL
data = {
    "name": "Product 1",
    "price": 9.99,
    "description": "This is a sample product"
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
