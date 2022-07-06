import pandas as pd
import streamlit as st
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


st.markdown("<h1 style='text-align: center; color: Blue;'>Dashboard</h1>", unsafe_allow_html=True)



uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
df = pd.read_csv(uploaded_data)

if uploaded_data:

    selected= option_menu(menu_title=None, options=["Overview","Dataset specific",'General','General 2'],icons=['book','book','book','book'],orientation='horizontal')

    if selected == "Overview":

        st.sidebar.header("filter through")
        gender=st.sidebar.multiselect("select Gender:",options=df["gender"].unique(),default= df["gender"].unique())
        Marriage=st.sidebar.multiselect("select Marital Status:",options=df["ever_married"].unique(),default= df["ever_married"].unique())
        Smoking=st.sidebar.multiselect("select Smoking status:",options=df["smoking_status"].unique(),default= df["smoking_status"].unique())

        df_selection = df.query("gender == @gender & ever_married == @Marriage & smoking_status ==@Smoking")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(label='Patients with heart disease',value=df_selection[df_selection['heart_disease']==1].value_counts().sum())
            st.markdown("""
        <style>
    div[data-testid="metric-container"] {
    background-color: rgba(95, 204, 218, 0.8);
    border: 1px solid rgba(95, 204, 218, 0.8);
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
    color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red;
}
</style>
"""
, unsafe_allow_html=True)

        with col2:
            st.metric(label='Patients with hypertension', value=df_selection[df_selection['hypertension']==1].value_counts().sum())
            
    
        with col3:
            st.metric(label='smokers',value=df_selection[df_selection['smoking_status']=='smokes'].value_counts().sum())

        with col4:
            st.metric(label='Married',value=df_selection[df_selection['ever_married']=='Yes'].value_counts().sum())

        b1, b2  = st.columns(2)
        with b1:
            df_stroke=df_selection.groupby('stroke')['id'].count().reset_index(name='count')
            fig88 = px.pie(df_stroke, values='count',names='stroke', height = 350, width = 400,title='Stroke Count')
            fig88=go.Figure(fig88)

            b1.plotly_chart(fig88)
            
            

        with b2:
            df_gender = df_selection.groupby('gender')['id'].count().reset_index(name='count')
            fig18 = px.pie(df_gender, values='count',names='gender', height = 350, width = 400, title='Gender count')
            fig18=go.Figure(fig18)

            b2.plotly_chart(fig18)

            

        
        



        c1, c2, c3 =st.columns(3)
        with c1:
            fig00= px.bar(df_selection, x='gender',y='stroke', height=400, width=400)
            fig00= go.Figure(fig00)
        
            c1.plotly_chart(fig00)

        with c2:
            fig01= px.bar(df_selection, x='gender',y='heart_disease', height=400, width=400)
            fig01= go.Figure(fig01)
        
            c2.plotly_chart(fig01)

        with c3:
            fig06 = px.bar(df_selection, x='smoking_status',y='stroke', color='gender',barmode='group', height=400, width=400)
            fig06 = go.Figure(fig06)

            c3.plotly_chart(fig06)

       


        
    



    if selected == "Dataset specific":
        met1, met2, met3, met4 = st.columns(4)
        st.markdown("""
        <style>
    div[data-testid="metric-container"] {
    background-color: rgba(95, 204, 218, 0.8);
    border: 1px solid rgba(95, 204, 218, 0.8);
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
    color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red;
}
</style>
"""
, unsafe_allow_html=True)


        with met1:
            st.metric(label='Strokes Patients below 18', value=len(df[(df['stroke']==1) & (df['age']<18)]))

        with met2:
            st.metric(label='Strokes Patients ages (18-30)', value=len(df[(df['stroke']==1) & (df['age']>18) & (df['age']<30)]))

        with met3:
            st.metric(label='Strokes Patients ages (30-60)', value=len(df[(df['stroke']==1) & (df['age']>30) & (df['age']<60)]))

        with met4:
            st.metric(label='Strokes Patients Above 60', value=len(df[(df['stroke']==1) & (df['age']>60)]))

        
        con1, con2 = st.columns(2)
        with con1:
            fig09 = px.sunburst(df, path=['gender','Residence_type','smoking_status'], values='stroke', color='gender', height=400, width=600)
            fig09=go.Figure(fig09)
            st.plotly_chart(fig09)


        with con2:
            fig099 = px.sunburst(df, path=['gender','ever_married','work_type'], values='stroke', color='gender',height=400, width=600)
            fig099=go.Figure(fig099)

            st.plotly_chart(fig099)

        m1, m2 = st.columns(2)
        with m1:
            df_smoking1 = df[df['stroke']==1].groupby(['smoking_status']).size().reset_index(name="counts of stroke")
            fig45 = px.violin(df_smoking1,x='smoking_status', y='counts of stroke')
            fig45 = go.Figure(fig45)
            st.plotly_chart(fig45)
        with m2:
            df_working = df[df['stroke']==1].groupby(['work_type']).size().reset_index(name="counts of stroke")
            fig46 = px.violin(df_working,x='work_type', y='counts of stroke')
            fig46 = go.Figure(fig46)
            st.plotly_chart(fig46)
        g1, g2 = st.columns(2)
        with g1:
            df_aging = df[df['stroke']==1].groupby(['age']).size().reset_index(name="counts of stroke")
            fig645 = px.scatter(df_aging, x='age', y='counts of stroke')
            fig645 = go.Figure(fig645)
            fig645.update_traces(marker=dict(color='red'))
            st.plotly_chart(fig645)

        with g2:
            fig74 = px.violin(df,x='work_type', y='bmi', height=400, width=600)
            fig74 = go.Figure(fig74,layout_yaxis_range =[5,50])
            fig74.update_traces(marker=dict(color='red'))
            st.plotly_chart(fig74)

            


    if selected == 'General 2':
        kol1, kol2 =st.columns(2)
        with kol1:
            html_string = '<iframe src="https://ourworldindata.org/grapher/annual-number-of-deaths-by-cause?time=latest" loading="lazy" style="width: 100%; height: 500px; border: 0px none;"></iframe>'
            st.markdown(html_string, unsafe_allow_html=True)

        with kol2:
            html_string2 = '<iframe src="https://ourworldindata.org/grapher/total-number-of-deaths-by-cause?stackMode=relative&country=~OWID_WRL" loading="lazy" style="width: 100%; height: 500px; border: 0px none;"></iframe>'
            st.markdown(html_string2, unsafe_allow_html= True)

    
    if selected == 'General':
        
        html_string3 = '<iframe src="https://ourworldindata.org/grapher/stroke-death-rates?country=MAR~NGA~LBR" loading="lazy" style="width: 100%; height: 600px; border: 0px none;"></iframe>'
        st.markdown(html_string3, unsafe_allow_html= True)
