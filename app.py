import pandas as pd
import streamlit as st
import seaborn as sns

def explore_raw_data(df):
   st.subheader('Raw Data')
   if st.checkbox('Show Raw Data'):
       st.dataframe(df)

# Title
st.title('Exploratory Data Analysis')
st.sidebar.write("## Data analysis :bar_chart:")

# Load Data
#Data = pd.read_csv('Data/california_housing_train.csv')
Uploaded_file = st.sidebar.file_uploader('Upload Data:', type =['csv'])
if Uploaded_file is not None:
  Data = pd.read_csv(Uploaded_file)

tab_titles = ['Data summary','Graphics']
tabs = st.tabs(tab_titles)

with tabs[0]:
  # Explore raw data
  explore_raw_data(Data)
  
  # Display summary
  st.write('Descriptive summary:')
  st.dataframe(Data.describe())

  # Display correlation matrix
  st.write('Correlation matrix:')
  st.dataframe(Data.corr())

with tabs[1]:
  st.write('Visualization of data')
  #plot_1 = sns.pairplot(data = Data, palette='Set2')
  #st.pyplot(plot_1.fig)
