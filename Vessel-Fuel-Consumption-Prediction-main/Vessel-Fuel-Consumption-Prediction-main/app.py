import streamlit as st
import pickle
import pandas as pd

# Load the model and scaler
model = pickle.load(open('model/model.pkl', 'rb'))
scaler = pickle.load(open('scaler/scaler.pkl', 'rb'))

# Function to make a prediction based on input parameters
def make_prediction(model, scaler, rpm, stw, wind, draft_aft, draft_for, obs_dist):
    # Create a DataFrame from the input parameters
    df = pd.DataFrame({
        "RPM": [rpm],
        "STW": [stw],
        "WIND": [wind],
        "DRAFT FOR": [draft_for],
        "DRAFT AFT": [draft_aft],
        "OBS DIST": [obs_dist]
    })
    # Scale the input data
    df = scaler.transform(df)
    # Make a prediction
    prediction = model.predict(df)
    return prediction[0]

# Streamlit - Set custom CSS styles for the app
st.markdown(
    """
    <style>
    body {
        font-family: 'Verdana', Geneva, sans-serif;
    }     
    * {
    }
    .centered {
        text-align: center;
    }
    .title {
        font-size: 70px; 
        font-weight: bold; 
        margin-bottom: 0px; 
        color: rgb(118, 171, 174); 
    }
    .input-header {
        font-size: 25px; 
        margin-top: 10px; 
        margin-bottom: 20px; 
        font-weight: bold; 
        color: rgb(118, 171, 174); 
    }
    br {
        display: block; 
        margin: 400px 0; 
    }
    .stButton button {
        width: 225px; 
        height: 45px; 
        font-size: 20px; 
        background-color: rgb(118, 171, 174); 
        color: rgb(238, 238, 238); 
        border: none; 
        border-radius: 12px; 
        cursor: pointer; 
        text-align: center; 
    }
    .stButton button:hover {
        background-color: rgba(95, 145, 148, 1); 
    }
    .credit {
        font-size: 15px; 
        margin-top: 0px; 
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the application
st.markdown(
    '''
    <div class="centered title">Fuel Consumption Prediction Panel</div>
    ''',
    unsafe_allow_html=True
)

# Display an image related to the project
st.image('images/ship_image.jpg', width=400, use_column_width=True, caption=None)

# Header for the input section
st.markdown(
    """<div class="centered input-header"> Please input the following parameters:</div>""", unsafe_allow_html=True
)

# Input fields for the model parameters
col1, col2, col3 = st.columns(3)
with col1:
    rpm = st.number_input("**RPM:**", 0.00)
with col2:
    stw = st.number_input("**STW:**", 0.00)
with col3:
    wind = st.number_input("**WIND:**", 0.00)

col4, col5, col6 = st.columns(3)
with col4:
    draft_for = st.number_input("**DRAFT FOR:**", 0.00)
with col5:
    draft_aft = st.number_input("**DRAFT AFT:**", 0.00)
with col6:
    obs_dist = st.number_input("**OBS DIST:**", 0.00)

st.markdown('<br>', unsafe_allow_html=True)

# Prediction button
col7, col8, col9 = st.columns(3)
with col8:
    if st.button("**PREDICT**"):
        predict = True
    else:
        predict = False

# Prediction result
if predict:
    # Call the make_prediction function with the input values
    prediction = make_prediction(model, scaler, rpm, stw, wind, draft_aft, draft_for, obs_dist)
    st.markdown(f"<h3 class='centered'>Fuel Consumption Prediction: {abs(prediction):.2f}</h3>", unsafe_allow_html=True)

# Credits section
st.markdown(
    """
    <div class="centered credit">By: Amit Rozen, Omri Shmuel, Shani Zicher, Shirly Avrahamoff, Yahav Gabay.</div>
    """, unsafe_allow_html=True
)
