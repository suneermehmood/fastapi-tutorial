from fastapi import FastAPI

# Requirement - 
#   1. You should have fastapi installed - pip install fastapi
#   2. You should have uvicorn installed - pip install uvicorn


app = FastAPI()

@app.get("/predict")
def predict_model(age: int, sex: str):    
    if age < 18:
        return {"prediction": "child"}
    elif age < 65:
        return {"prediction": "adult"}
    else:
        return {"prediction": "elderly"}