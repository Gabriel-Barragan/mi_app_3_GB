import pandas as pd
import streamlit as st

# Load Data
Data = pd.read_csv('Data/california_housing_train.csv')

# Create app
st.title('California Housing Data')

# Display correlation matrix
st.write('Correlation matrix:')
st.dataframe(Data.corr())
