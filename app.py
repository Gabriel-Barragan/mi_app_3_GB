import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title('Exploratory Data Analysis')
st.sidebar.write("## Data analysis :bar_chart:")
st.sidebar.write("Autor: Gabriel Barragán")

# Load Data
Data = pd.read_csv('Data/california_housing_train.csv')
#Uploaded_file = st.sidebar.file_uploader('Upload Data:', type =['csv'])
#if Uploaded_file is not None:
#  Data = pd.read_csv(Uploaded_file)

tab_titles = ['Data summary','Graphics','Pairplot']
tabs = st.tabs(tab_titles)

with tabs[0]:

  if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(Data)
  
  # Display summary
  st.write('Descriptive summary:')
  st.dataframe(Data[Data.columns.difference(["longitude", "latitude"])].describe())

  # Display correlation matrix
  st.write('Correlation matrix:')
  st.dataframe(Data[Data.columns.difference(["longitude", "latitude"])].corr())

with tabs[1]:
  st.write('Visualization of data')

  column = st.selectbox("Variable:", list(Data[Data.columns.difference(["longitude", "latitude"])].columns))

  # Create a histogram with custom color and title
  fig_1, ax = plt.subplots()
  plt.hist(Data[column], color='skyblue', edgecolor='black')
  plt.title('Histogram')
 
  # Display the plot in Streamlit
  st.pyplot(fig_1)

  fig_2 = plt.boxplot(Data[Data.columns.difference(["longitude", "latitude"])])
  st.pyplot(fig_2) 

with tabs[2]:  
  fig_3 = sns.pairplot(Data[Data.columns.difference(["longitude", "latitude"])])
  st.pyplot(fig_3.fig)
