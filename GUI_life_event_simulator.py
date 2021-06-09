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

@st.cache
def load_cbs_data():
    df = pd.read_csv('data_cbs.csv',sep = ';')
    return df

df_choice = pd.DataFrame([{'CustomerType': customer_choice,
                          'LifeEvent': event_choice}])

df_cbs = load_cbs_data()
df_selected_cbs = df_choice.merge(df_cbs, on =['CustomerType','LifeEvent'], how='left')

cols = st.beta_columns((1,1,1,1))

cols[0].markdown('<br/><br/>', unsafe_allow_html=True)
cols[0].image('grocery2.png')
cols[0].image('subsidy2.png')
cols[0].image('energy2.png')

n11 = df_selected_cbs[df_selected_cbs['Category'] == 'Groceries']['No kids'].values[0]
n12 = df_selected_cbs[df_selected_cbs['Category'] == 'Toeslagen']['No kids'].values[0]
n13 = df_selected_cbs[df_selected_cbs['Category'] == 'Energy']['No kids'].values[0]
n21 = df_selected_cbs[df_selected_cbs['Category'] == 'Groceries']['Delta'].values[0]
n22 = df_selected_cbs[df_selected_cbs['Category'] == 'Toeslagen']['Delta'].values[0]
n23 = df_selected_cbs[df_selected_cbs['Category'] == 'Energy']['Delta'].values[0]
n31 = df_selected_cbs[df_selected_cbs['Category'] == 'Groceries']['Plus 1 kid'].values[0]
n32 = df_selected_cbs[df_selected_cbs['Category'] == 'Toeslagen']['Plus 1 kid'].values[0]
n33 = df_selected_cbs[df_selected_cbs['Category'] == 'Energy']['Plus 1 kid'].values[0]

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

