import joblib
import pandas as pd

model = joblib.load("../models/random_forest_model.pkl")

preprocessor = joblib.load("../models/preprocessor.pkl")


def predict_churn(data):

    df = pd.DataFrame([data])

    processed_data = preprocessor.transform(df)

    prediction = model.predict(processed_data)[0]

    probability = model.predict_proba(processed_data)[0][1]

    return prediction, probability