import pandas as pd
import streamlit as st

# Title
st.title('Exploratory Data Analysis')
st.sidebar.write("## Data analysis :bar_chart:")

# Load Data
#Data = pd.read_csv('Data/california_housing_train.csv')
Uploaded_file = st.sidebar.file_uploader('Upload Data:', type =['csv'])

if Uploaded_file is not None:
  Data = pd.read_csv(Uploaded_file)

  # Create app
  st.title('California Housing Data')

  # Display summary
  st.write('Descriptive summary:')
  st.dataframe(Data.describe())

  # Display correlation matrix
  st.write('Correlation matrix:')
  st.dataframe(Data.corr())


