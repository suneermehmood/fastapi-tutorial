import requests,json

payload = json.dumps({
    "age": 15
})

response = requests.put('http://localhost:8000/predict', data=payload)
print(response.json())