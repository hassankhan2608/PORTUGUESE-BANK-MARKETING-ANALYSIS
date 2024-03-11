import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the LabelEncoder
with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

# Load the XGBoost model
with open('xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the UI
st.set_page_config(page_title="Marketing Prediction", layout="wide")
st.header("Portuguese Bank TeleMarketing Prediction App")
st.write("This app predicts whether a customer is likely to subscribe to a term deposit based on their demographic and campaign information.")
# Define the categorical feature mappings
categorical_mappings = {
    'job': ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed'],
    'marital': ['divorced', 'married', 'single'],
    'education': ['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree'],
    'default': ['no', 'yes'],
    'housing': ['no', 'yes'],
    'loan': ['no', 'yes'],
    'contact': ['cellular', 'telephone'],
    'day_of_week': ['mon', 'tue', 'wed', 'thu', 'fri'],
    'month': ['mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'],
    'poutcome': ['failure', 'nonexistent', 'success']
}

# Input widgets for categorical features
col1, col2, col3, col4, col5 = st.columns(5)
selected_category = {feature: col1.selectbox(f'{feature}', options, index=None) for feature, options in list(categorical_mappings.items())[:2]}
selected_category.update({feature: col2.selectbox(f'{feature}', options, index=None) for feature, options in list(categorical_mappings.items())[2:4]})
selected_category.update({feature: col3.selectbox(f'{feature}', options, index=None) for feature, options in list(categorical_mappings.items())[4:6]})
selected_category.update({feature: col4.selectbox(f'{feature}', options, index=None) for feature, options in list(categorical_mappings.items())[6:8]})
selected_category.update({feature: col5.selectbox(f'{feature}', options, index=None) for feature, options in list(categorical_mappings.items())[8:]})

# Input widgets for numerical features
col6, col7 = st.columns(2)
age = col6.slider('Age', 18, 100, 30)
campaign = col7.slider('Campaign', 1, 20, 1)
    

# Button to predict
if st.button('Predict'):
    if None in selected_category.values():
        missing_categories = [key for key, value in selected_category.items() if value is None]
        missing_categories_str = ", ".join(missing_categories)
        st.error(f"Please select values for the following categorical features: {missing_categories_str}")
    else:
        # Create a DataFrame with the selected data
        data = {
            'Feature': list(selected_category.keys()) + ['Age', 'Campaign'],
            'Value': list(selected_category.values()) + [age, campaign]
        }
        df = pd.DataFrame(data)
        
        # Transpose the DataFrame for horizontal display
        df_transposed = df.T
        df_transposed.columns = df_transposed.iloc[0]
        df_transposed = df_transposed.drop('Feature')
        
        st.table(df_transposed)
        
        encoded_features = []
        for feature, value in selected_category.items():
            encoder = label_encoders[feature]
            encoded_value = encoder.transform([value])[0]
            encoded_features.append(encoded_value)
        
        # Prepare input data for prediction
        input_data = np.array(encoded_features + [age, campaign]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction_text = 'Yes' if prediction == 1 else 'No'
        if prediction_text == 'Yes':
            styled_prediction = '<span style="font-size: 20px; color: green; font-weight: bold;">Yes</span>'
        else:
            styled_prediction = '<span style="font-size: 20px; color: red; font-weight: bold;">No</span>'
        
        # Display prediction with a subheader
        st.subheader("Prediction Result")
        st.markdown(f"The Customer is likely to Say {styled_prediction} to the Term Deposit", unsafe_allow_html=True)

