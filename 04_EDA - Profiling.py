import pandas as pd
import streamlit as st

import pandas_profiling

from pandas_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report


uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
if uploaded_data:
    df=pd.read_csv(uploaded_data)
    profile = ProfileReport(df,explorative= True)
    st_profile_report(profile)

