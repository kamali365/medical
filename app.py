import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model_path = 'model.pkl'  # Update with the correct path to your model file
with open(model_path, 'rb') as file:
    model = pickle.load(file)

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
        input_data = pd.DataFrame([{
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "children": children,
            "smoker": smoker,
            "region": region
        }])

        # Make the prediction
        prediction = model.predict(input_data)[0]

        # Display the result
        st.success(f"Predicted Insurance Cost: ${prediction:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
