import streamlit as st

st.set_page_config(layout="wide")

import pandas as pd



uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')

if uploaded_data:
    st.markdown("<h1 style='text-align: center; color: red;'>A look into the data</h1>", unsafe_allow_html=True)
    df= pd.read_csv(uploaded_data)

    with open('style1.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    Kpi1, Kpi2, Kpi3, Kpi4 =st.columns(4)

    col = df.columns

        #creating KPI metrics

    Kpi1.metric(label ="Number of Columns", value = len(col))

    Kpi2.metric(label="Number of rows", value = len(df))

    Kpi3.metric(label="Null values", value = df.isnull().sum().sum())

    Kpi4.metric(label="Duplicates", value =df.duplicated().sum().sum())
    

    st.markdown("<h1 style='text-align: center; color: green;'>Health references and Risk factors</h1>", unsafe_allow_html=True)


    b1, b2, b3, b4 = st.columns(4)
    with st.container():
        b1.metric("BMI healthy Range","18.5 - 24.9")
    b2.metric("Normal glucose Level","Below 140")
    b3.metric("Women","More deadly")
    b4.metric("Men","More likely")


    st.sidebar.header("filter through")
    gender=st.sidebar.multiselect("select Gender:",options=df["gender"].unique(),default= df["gender"].unique())
    Marriage=st.sidebar.multiselect("select Marital Status:",options=df["ever_married"].unique(),default= df["ever_married"].unique())
    Smoking=st.sidebar.multiselect("select Smoking status:",options=df["smoking_status"].unique(),default= df["smoking_status"].unique())

    df_selection = df.query("gender == @gender & ever_married == @Marriage & smoking_status ==@Smoking")
    
    st.dataframe(df_selection,width=1200, height=300)


        

