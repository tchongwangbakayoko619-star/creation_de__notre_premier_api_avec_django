import requests
endpoint = 'http://localhost:8000/api/product/1/'
try:
    response = requests.put(endpoint, json={
        "name": "patate",
        "price": 20,
        "description": "fruit",
        "Email": "patate@example.com"
    })
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except ValueError:
        print("Response Text:", response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)