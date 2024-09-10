import streamlit as st
import pandas as pd
import pickle

# Load the saved pipeline
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.title('Customer Churn Prediction')

# Sidebar for user input features
st.sidebar.header('Input Features')

def user_input_features():
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    senior_citizen = st.sidebar.selectbox('Senior Citizen', ('No', 'Yes'))
    partner = st.sidebar.selectbox('Partner', ('No', 'Yes'))
    dependents = st.sidebar.selectbox('Dependents', ('No', 'Yes'))
    tenure = st.sidebar.slider('Tenure (Months)', 0, 72, 24)
    phone_service = st.sidebar.selectbox('Phone Service', ('No', 'Yes'))
    multiple_lines = st.sidebar.selectbox('Multiple Lines', ('No', 'Yes', 'No phone service'))
    internet_service = st.sidebar.selectbox('Internet Service', ('DSL', 'Fiber optic', 'No'))
    online_security = st.sidebar.selectbox('Online Security', ('No', 'Yes', 'No internet service'))
    online_backup = st.sidebar.selectbox('Online Backup', ('No', 'Yes', 'No internet service'))
    device_protection = st.sidebar.selectbox('Device Protection', ('No', 'Yes', 'No internet service'))
    tech_support = st.sidebar.selectbox('Tech Support', ('No', 'Yes', 'No internet service'))
    streaming_tv = st.sidebar.selectbox('Streaming TV', ('No', 'Yes', 'No internet service'))
    streaming_movies = st.sidebar.selectbox('Streaming Movies', ('No', 'Yes', 'No internet service'))
    contract = st.sidebar.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
    paperless_billing = st.sidebar.selectbox('Paperless Billing', ('No', 'Yes'))
    payment_method = st.sidebar.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
    monthly_charges = st.sidebar.slider('Monthly Charges', 18.0, 120.0, 50.0)
    total_charges = st.sidebar.slider('Total Charges', 18.0, 8000.0, 1000.0)

    data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Get user input data
input_df = user_input_features()

st.subheader('User Input Features')
st.write(input_df)

# Make predictions
try:
    prediction = pipeline.predict(input_df)
    prediction_proba = pipeline.predict_proba(input_df)
    
    st.subheader('Prediction')
    churn_status = 'Churn' if prediction[0] == 1 else 'No Churn'
    st.write(f'The customer is likely to: {churn_status}')
    
    st.subheader('Prediction Probability')
    st.write(f'Probability of churn: {prediction_proba[0][1]:.4f}')
    st.write(f'Probability of no churn: {prediction_proba[0][0]:.4f}')
except ValueError as e:
    st.error(f"Error: {e}")
