import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Land Price Prediction App")

st.write("Enter your data:")

Land_area = st.number_input("Land Area")

if st.button("Predict"):
    input_data = np.array([[Land_area]])
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")