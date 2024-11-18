
import requests

url = "http://127.0.0.1:5000/predict"
data = {"ticker": "AAPL"} 
response = requests.post(url, json=data)

try:
    print(response.json()) 
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON. Response content:", response.text)