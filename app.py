import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import io

web_apps = st.sidebar.selectbox("Select Web Apps",
                                ("Exploratory Data Analysis", "Distributions"))


if web_apps == "Exploratory Data Analysis":

  uploaded_file = st.sidebar.file_uploader("Choose a file")

  if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    show_df = st.checkbox("Show Data Frame", key="disabled")

    if show_df:
      st.write(df)
    
    st.header("Relevant Statistics of Dataset:")
    st.write("Number of Rows:", df.shape[0])
    st.write("Number of Columns:", df.shape[1])
    st.write("Number of Categorical Variables:", len(df.select_dtypes(include='object').columns))
    st.write("Number of Numerical Variables:", len(df.select_dtypes(include=['int64', 'float64']).columns))
    st.write("Number of Boolean Variables:", len(df.select_dtypes(include='bool').columns))

    column_type = st.sidebar.selectbox('Select Data Type', ("Numerical", "Categorical", "Bool", "Date"))

    if column_type == "Numerical":
      numerical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)
      
      st.header("Numerical Column Analysis: " + numerical_column)

      st.write("Five Number Summary:")
      st.write(df[numerical_column].describe())
      
      st.write("Distribution Plot:")
      fig, ax = plt.subplots()
      sns.histplot(df[numerical_column], kde=True, ax=ax)
      st.pyplot(fig)

    elif column_type == "Categorical":
      categorical_column = st.sidebar.selectbox('Select a Column', df.select_dtypes(include='object').columns)
      
      st.header("Categorical Column Analysis: " + categorical_column)

      st.write("Proportions of each category level:")
      st.write(df[categorical_column].value_counts(normalize=True))

      st.write("Bar Plot:")
      fig, ax = plt.subplots()
      sns.countplot(x=categorical_column, data=df, ax=ax)
      st.pyplot(fig)
