# Description: Consume the API created in app.py
# Usage: python consumeapi.py
# Output: {'prediction': 'adult'}
# Requirements: 
# 1. pip install requests
# 2. pip install fastapi
# 3. pip install uvicorn


import requests

age = 15

response = requests.get(f"http://localhost:8000/predict?age={age}")
output = response.json()
print(output)