# import streamlit as st 
import numpy as np
# from src.components.data_ingestion import DataIngestion
# import pandas as pd
# st.title('DEMO')
# file = st.file_uploader('Upload a file',['csv'])

# st.write(file)
# if file:
#     dataing = DataIngestion()
#     dataing.initialise_Ingestion(file)  --> get an additional parameter
#     st.write('Successful')
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr[0][1])