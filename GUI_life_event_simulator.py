import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.image('title6.jpg', use_column_width=False)

st.sidebar.title('Make Choices')

customer_choice = st.sidebar.selectbox(
    "Type Customer:",
    ("Couple family without children", 
     "Single person without children")
)

event_choice = st.sidebar.selectbox(
    "Type Event:",
    ("Getting a child", "Living together", "Buying a house")
)

bucket_choice = st.sidebar.slider('Salary Bucket', 0, 8, 1)

@st.cache
def load_data():
    df = pd.read_csv('data_new.csv',sep = ',')
    return df

df = load_data()

cols = st.beta_columns((1,1,1,1))

cols[0].markdown('<br/><br/>', unsafe_allow_html=True)
cols[0].image('grocery2.png')
cols[0].image('subsidy2.png')
cols[0].image('energy2.png')

n11 = int(abs(df['nz_avg_boodschappen'][bucket_choice]))
n12 = int(abs(df['nz_avg_toeslagen'][bucket_choice]))
n13 = int(abs(df['nz_avg_energie_water'][bucket_choice]))
n21 = int(abs(df['nz_avg_boodschappen'][bucket_choice]))
n22 = int(abs(df['nz_avg_toeslagen'][bucket_choice]))
n23 = int(abs(df['nz_avg_energie_water'][bucket_choice]))
n31 = int(abs(df['nz_avg_boodschappen'][bucket_choice]))
n32 = int(abs(df['nz_avg_toeslagen'][bucket_choice]))
n33 = int(abs(df['nz_avg_energie_water'][bucket_choice]))

cols[1].subheader('Current:')
cols[1].markdown('<br/><br/>', unsafe_allow_html=True)
cols[1].markdown('<p style="font-family:Verdana; color:Red; font-size: 20px;">'+'€ '+str(n11)+'</p>', unsafe_allow_html=True)
cols[1].markdown('<br/><br/>', unsafe_allow_html=True)
cols[1].markdown('<p style="font-family:Verdana; color:Green; font-size: 20px;">'+'€ '+str(n12)+'</p>', unsafe_allow_html=True)
cols[1].markdown('<br/><br/>', unsafe_allow_html=True)
cols[1].markdown('<p style="font-family:Verdana; color:Red; font-size: 20px;">'+'€ '+str(n13)+'</p>', unsafe_allow_html=True)

cols[2].subheader('Delta:')
cols[2].markdown('<br/><br/>', unsafe_allow_html=True)
cols[2].markdown('<p style="font-family:Verdana; color:Red; font-size: 20px;">'+'€ '+str(n21)+'</p>', unsafe_allow_html=True)
cols[2].markdown('<br/><br/>', unsafe_allow_html=True)
cols[2].markdown('<p style="font-family:Verdana; color:Green; font-size: 20px;">'+'€ '+str(n22)+'</p>', unsafe_allow_html=True)
cols[2].markdown('<br/><br/>', unsafe_allow_html=True)
cols[2].markdown('<p style="font-family:Verdana; color:Red; font-size: 20px;">'+'€ '+str(n23)+'</p>', unsafe_allow_html=True)

cols[3].subheader('Future:')
cols[3].markdown('<br/><br/>', unsafe_allow_html=True)
cols[3].markdown('<p style="font-family:Verdana; color:Red; font-size: 20px;">'+'€ '+str(n31)+'</p>', unsafe_allow_html=True)
cols[3].markdown('<br/><br/>', unsafe_allow_html=True)
cols[3].markdown('<p style="font-family:Verdana; color:Green; font-size: 20px;">'+'€ '+str(n32)+'</p>', unsafe_allow_html=True)
cols[3].markdown('<br/><br/>', unsafe_allow_html=True)
cols[3].markdown('<p style="font-family:Verdana; color:Red; font-size: 20px;">'+'€ '+str(n33)+'</p>', unsafe_allow_html=True)

