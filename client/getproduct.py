import requests
endpoint = 'http://localhost:8000/api/product/2/'
try:
    response = requests.get(endpoint)
    print("Status Code:", response.status_code)
    try:                                                                                    
        print("Response JSON:", response.json())
    except ValueError:
        print("Response Text:", response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)