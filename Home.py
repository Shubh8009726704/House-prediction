import numpy as np
import pandas as pd
import streamlit as st
from prediction import predict
import matplotlib.pyplot as plt

st.set_page_config(
    page_title= 'Home',    
)
if st.sidebar.button('Home'):
    st.markdown('''<h1 style='color:black;background:yellow;padding:15px;border-radius:10px'>Predicting the price of a house in Ramanthapur(Hyderabad).</h1>''',unsafe_allow_html=True)

    st.markdown('''<h3>Model to predict the price of a house based on its features</h3>''',unsafe_allow_html=True)

st.header('House features')
col1, col2, col3, col4= st.columns(4)
with col1:
    area = st.slider('Area: ', 1650, 16200, 50)
    bedrooms = st.radio('No. of bedrooms: ', [1, 2, 3, 4, 5, 6],horizontal=True)
    bathrooms = st.radio('No. of bathrooms: ', [1, 2, 3, 4],horizontal=True)
with col2:
    stories = st.radio('No. of stories: ', [1, 2, 3, 4],horizontal=True)
    parking = st.radio('Parking: ', [0, 1, 2, 3],horizontal=True)
    mainroad = st.radio('Main road: ', [0, 1],horizontal=True)
with col3: 
    guestroom = st.radio('Guest room: ', [0, 1],horizontal=True)
    basement = st.radio('Basement: ', [0, 1],horizontal=True)
    hotwaterheating = st.radio('Hot water heating: ', [0, 1],horizontal=True)
with col4:
    airconditioning = st.radio('Air conditioning: ', [0, 1],horizontal=True)
    prefarea = st.radio('Preferred area: ', [0, 1],horizontal=True)
    furnishingstatus = st.radio('Furnishing status: furn, Semi-Fur, Unfurnished ', [0, 1, 2],horizontal=True)

if st.button("Predict Price of House"):
    data = np.array([area, bedrooms	, bathrooms	, stories, parking, mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus])
    data = pd.DataFrame(data.reshape(-1, len(data)), columns=['area', 'bedrooms', 'bathrooms', 'stories', 'parking','mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'])
    st.write(data)
    prediction = predict(data)
    st.header('Predicted price of house is : Rs. ' + str(round(prediction[0],2)))
    
st.success('Note : If you are facing any problem related to my App contact with me.')

if st.sidebar.button('Contact us'):
    st.write('<h4>Name : Shubham Sharma</h4>',unsafe_allow_html=True)
    st.write('<h4>Email ID : shbh8055@gmail.com</h4>',unsafe_allow_html=True)
    st.write('<h4>Mobile No : 8112301399</h4>',unsafe_allow_html=True)
    st.write('<h4>Address : Ramanthapur Hyderabad 500013</h4>',unsafe_allow_html=True)
    
if st.sidebar.button('About Me'):
    st.markdown('''<h3 style='text-align:justify;color:blue'>Hey guys, My name is Shubham Sharma.I am student of Advanced Diploma and Information Technology(ADIT) from Ramanthapur(Hyderabad) and I am a Web Developer.</h3>''',unsafe_allow_html=True)

