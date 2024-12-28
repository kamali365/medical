import streamlit as st
import pandas as pd

# Placeholder for the model
# Since the model file is not available, we'll simulate predictions with a dummy function.
def dummy_predict(data):
    # Example logic for demonstration
    base_cost = 1000
    age_factor = 50 * data['age']
    bmi_factor = 30 * data['bmi']
    smoker_factor = 2000 if data['smoker'] == 'yes' else 0
    return base_cost + age_factor + bmi_factor + smoker_factor

# Streamlit app
st.title("Medical Insurance Cost Prediction")

st.write("Enter the details below to predict the insurance cost.")

# Input fields
age = st.number_input("Age", min_value=0, step=1)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=0.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, step=1)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Prediction
if st.button("Predict"):
    try:
        # Prepare the input data
        input_data = {
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "children": children,
            "smoker": smoker,
            "region": region
        }

        # Simulate the prediction
        prediction = dummy_predict(input_data)

        # Display the result
        st.success(f"Predicted Insurance Cost: ${prediction:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
