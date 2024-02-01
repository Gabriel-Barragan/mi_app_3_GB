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

  if st.checkbox('Show first observations:'):
    st.write('# First observations',5)
    st.write(Data.head(5))

  if st.checkbox('Show last observations:'):
    st.write('# Last observations',5)
    st.write(Data.tail(5))
  
  if st.checkbox('Show raw data'):
    st.write('# Raw data')
    st.write(Data)

  if st.checkbox('Show missing data'):
    st.write('# Missing data')
    st.write(Data.isnull().sum())
    # Display a bar chart of the missing values
    st.bar_chart(Data.isnull().sum())
  
  # Display summary
  st.write('# Descriptive summary:')
  st.dataframe(Data[Data.columns.difference(["longitude", "latitude"])].describe())

  # Display correlation matrix
  st.write('# Correlation matrix:')
  Data_corr = Data[Data.columns.difference(["longitude", "latitude"])].corr()
  #st.dataframe(Data_corr)

  fig, ax = plt.subplots(figsize=(10, 8))
  sns.heatmap(Data_corr, annot=True, cmap='coolwarm', center=0, ax=ax)
  st.pyplot(fig)

with tabs[1]:
  st.write('# Visualization of data')

  column = st.selectbox("Variable:", list(Data[Data.columns.difference(["longitude", "latitude"])].columns))

  # Create a histogram with custom color and title
  plt.subplots()
  plt.title('Histogram')
  plt.hist(Data[column], color='skyblue', edgecolor='black')
  plt.xlabel(column)
  # Display the plot in Streamlit
  st.pyplot(plt)

  plt.subplots()
  plt.title('Boxplot')
  plt.boxplot(Data[column])
  plt.xlabel(column)
  plt.xticks([])
  st.pyplot(plt)

with tabs[2]:  
  fig_3 = sns.pairplot(Data[Data.columns.difference(["longitude", "latitude"])])
  st.pyplot(fig_3.fig)
