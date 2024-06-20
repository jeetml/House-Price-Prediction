import streamlit as st
import pickle
import pandas as pd

# Load the trained pipeline
with open('model_pipeline.pkl', 'rb') as f:
    pipe = pickle.load(f)
data = pd.read_csv('data_house_clean.csv')
# Streamlit app
st.title('House Price Prediction')
location = sorted(data['location'].unique())
# Input fields
location = st.selectbox('Location',location)
size = st.number_input('Size (in square feet)', value=1000)
bath = st.number_input('Number of Bathrooms', value=2, step=1)
bhk = st.number_input('BHK', value=2, step=1)

# Predict button
if st.button('Predict'):
    # Create a DataFrame for the input
    input_data = pd.DataFrame([[location, size, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    # Make a prediction
    prediction = pipe.predict(input_data)[0]*100000
    # Display the prediction
    st.write(f'Predicted House Price: {prediction}')

