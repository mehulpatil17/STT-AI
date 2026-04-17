import streamlit as st
import pickle
import pandas as pd
import sys
import numpy as np


def ensure_numpy_core_modules():
    if 'numpy._core' in sys.modules:
        return
    if hasattr(np, 'core'):
        sys.modules['numpy._core'] = np.core
        sys.modules['numpy._core.numeric'] = np.core.numeric
        sys.modules['numpy._core.multiarray'] = np.core.multiarray
        sys.modules['numpy._core.umath'] = np.core.umath


def load_pickle(path):
    try:
        with open(path, 'rb') as f:
            return pickle.load(f)
    except ModuleNotFoundError as exc:
        if 'numpy._core' in str(exc) or 'numpy._core.numeric' in str(exc):
            ensure_numpy_core_modules()
            with open(path, 'rb') as f:
                return pickle.load(f)
        raise


model = load_pickle('models/best_rf_model.pkl')
encoders = load_pickle('models/encoders.pkl')

st.title("UrbanNest Analytics - Dynamic House Rent Prediction")
st.write("Enter the property details to predict the rent.")

city = st.selectbox("City", encoders['city'].classes_)
location = st.selectbox("Location", encoders['location'].classes_)
latitude = st.number_input("Latitude", value=19.0, step=0.01)
longitude = st.number_input("Longitude", value=72.0, step=0.01)
numBathrooms = st.number_input("Number of Bathrooms", min_value=1, value=1)
numBalconies = st.number_input("Number of Balconies", min_value=0, value=0)
isNegotiable = st.selectbox("Is Negotiable", [0, 1])
SecurityDeposit = st.number_input("Security Deposit", min_value=0, value=0)
Status = st.selectbox("Status", encoders['Status'].classes_)
Size_ft_sq = st.number_input("Size in ft²", min_value=100, value=1000)
BHK = st.number_input("BHK", min_value=0, value=1)
rooms_num = st.number_input("Number of Rooms", min_value=1, value=1)
property_type = st.selectbox("Property Type", encoders['property_type'].classes_)
verification_days = st.number_input("Verification Days", min_value=0, value=0)

if st.button("Predict Rent"):
    input_data = {
        'location': [location],
        'city': [city],
        'latitude': [latitude],
        'longitude': [longitude],
        'numBathrooms': [numBathrooms],
        'numBalconies': [numBalconies],
        'isNegotiable': [isNegotiable],
        'SecurityDeposit': [SecurityDeposit],
        'Status': [Status],
        'Size_ft²': [Size_ft_sq],
        'BHK': [BHK],
        'rooms_num': [rooms_num],
        'property_type': [property_type],
        'verification_days': [verification_days]
    }
    input_df = pd.DataFrame(input_data)

    for col in ['city', 'location', 'Status', 'property_type']:
        input_df[col] = encoders[col].transform(input_df[col])

    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Rent: ₹{prediction:.2f}")
