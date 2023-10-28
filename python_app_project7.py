# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:41:05 2023

@author: Amena
"""

#In this project we will build explatory data analysis (EDA) web app using Python and Streamlit
#if you are ussing Streamlit for the firsttime in your computor, install it using
#Anaconda prompt, then type: pip install Streamlit , then enter
#you can also check demo apps of streamlit by tuping inthte prompt: 
    #streamlit hello
# Imports

import streamlit as st
import pandas as pd
import seaborn as sns

#title and subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

# in the prompt, to stop the running app you click: ctl+c
#then run ur app in the prompt by typing: streamlit run filename.py
#make sure you are in the desired working directory
# to change wd: cd C:\path\to\your\desired\directory

# 'if upload is not None:' statement, makes whaterver code after it runs only when there is a file uploaded 

#Upload dataset
upload = st.file_uploader("Upload Your Dataset! (in csv format)")
if upload is not None:
    data=pd.read_csv(upload)
    
#Show Dataset
if upload is not None:   
     if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head(5))
        if st.button("Tail"):
            st.write(data.tail(5))

#check dataype of each coulmn
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        if st.text("DataType"):
            st.write(data.dtypes)
            
#Find shape of our dataset (# of columns & # of rows)
if upload is not None:
    data_shape=st.radio("What Dimension Do You Want To Check?", ('Rows','Columns'))
        
    if data_shape=='Rows':
            st.text("Number of Rows")
            st.write(data.shape[0])
    if data_shape=='Columns': 
            st.text("Number of Columns")
            st.write(data.shape[1])


# check for null values in the dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("No Missing Values! :)")

# check for duplicates in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("!This Dataset Contains Duplicate Values!")
        dup=st.selectbox("Do you want to remove dupliacte values?", \
                         ("Select One","Yes", "No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate values are removed")
        if dup=="No":
            st.text("Okay, no problem :)")
  
# Get over all statistics
if upload is not None:
    if st.checkbox("Satistics Summary"):
        st.write(data.describe(include='all'))


# About section
if st.button("About App"):
    st.text("This app was built with Streamlit")
    
# By
if st.button("By"):
    st.success("Amena Mahdami! :)")
    

# until now this app was deployed locally, 
# but you can deploy it in the cloud so others can see and interact with it
# you can deploy in Heroku cloud

















