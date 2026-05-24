import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Inputs

gender = st.selectbox("Gender", ["Male", "Female"])

senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])

partner = st.selectbox("Partner", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure_months = st.number_input("Tenure Months", min_value=0)

phone_service = st.selectbox("Phone Service", ["Yes", "No"])

multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input("Monthly Charges")

total_charges = st.number_input("Total Charges")

# Prediction button

if st.button("Predict Churn"):

    data = {
        "Gender": gender,
        "Senior_Citizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure_Months": tenure_months,
        "Phone_Service": phone_service,
        "Multiple_Lines": multiple_lines,
        "Internet_Service": internet_service,
        "Online_Security": online_security,
        "Online_Backup": online_backup,
        "Device_Protection": device_protection,
        "Tech_Support": tech_support,
        "Streaming_TV": streaming_tv,
        "Streaming_Movies": streaming_movies,
        "Contract": contract,
        "Paperless_Billing": paperless_billing,
        "Payment_Method": payment_method,
        "Monthly_Charges": monthly_charges,
        "Total_Charges": total_charges
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.subheader("Prediction Result")

    if result["prediction"] == 1:
        st.error(f"Customer likely to churn")
    else:
        st.success(f"Customer not likely to churn")

    st.write(f"Churn Probability: {result['churn_probability']:.2f}")