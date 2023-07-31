# Description: Consume the API created in app.py
# Usage: python consumeapi.py
# Output: {'prediction': 'adult'}
# Requirements: 
# 1. pip install requests
# 2. pip install fastapi
# 3. pip install uvicorn
# 4. pip install pydantic


from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    age: int

app = FastAPI()

@app.get("/predict")
def predict_model(d:Input):    
    if d.age < 18:
        return {"prediction": "child"}
    elif d.age < 65:
        return {"prediction": "adult"}
    else:
        return {"prediction": "elderly"}