from pathlib import Path
import joblib

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model paths
model_path = BASE_DIR / "models" / "random_forest_model.pkl"

preprocessor_path = (
    BASE_DIR / "models" / "preprocessor.pkl"
)

# Load files
model = joblib.load(model_path)

preprocessor = joblib.load(preprocessor_path)


def predict_churn(data):

    df = pd.DataFrame([data])

    processed_data = preprocessor.transform(df)

    prediction = model.predict(processed_data)[0]

    probability = model.predict_proba(processed_data)[0][1]

    return prediction, probability