import streamlit as st
import requests

st.title("🏥 Insurance Premium Category Predictor")

# Input form
with st.form("user_input_form"):
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    weight = st.number_input("Weight (kg)", min_value=1.0)
    height = st.number_input("Height (meters)", min_value=0.5, max_value=2.5, step=0.01)
    income = st.number_input("Annual Income (in LPA)", min_value=0.0)
    smoker = st.selectbox("Smoker?", options=["Yes", "No"])
    city = st.text_input("City")
    occupation = st.selectbox(
        "Occupation",
        options=[
            "retired", "freelancer", "student", "government_job",
            "business_owner", "unemployed", "private_job"
        ]
    )
    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income": income,
        "smoker": True if smoker == "Yes" else False,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=input_data)

        if response.status_code == 201:
            result = response.json()
            st.success(f"✅ Predicted Premium Category: **{result['predicted_category']}**")
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"🚫 Could not connect to API: {e}")
