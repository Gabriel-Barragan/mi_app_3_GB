import pandas as pd
import streamlit as st

# Load Data
#Data = pd.read_csv('Data/california_housing_train.csv')
Upload_file = st.sidebar.file_uploader('Upload Data:', type =['csv'])
Data = pd.read_csv(Upload_file)

# Create app
st.title('California Housing Data')

# Display summary
st.write('Descriptive summary:')
st.dataframe(Data.describe())

# Display correlation matrix
st.write('Correlation matrix:')
st.dataframe(Data.corr())
