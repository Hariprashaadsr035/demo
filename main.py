import streamlit as st 
from src.components.data_ingestion import DataIngestion
import pandas as pd
st.title('DEMO')
file = st.file_uploader('Upload a file',['csv'])

st.write(file)
if file:
    dataing = DataIngestion()
    dataing.initialise_Ingestion(file)
    st.write('Successful')
