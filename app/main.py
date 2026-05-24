from fastapi import FastAPI
from app.schema import CustomerData
from app.predict import predict_churn

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API"
    }

@app.post("/predict")
def predict(data: CustomerData):

    prediction, probability = predict_churn(data.dict())

    return {
        "prediction": int(prediction),
        "churn_probability": float(probability)
    }