import streamlit as st
import pandas as pd
import numpy as np


st.table(data=pd.read_csv('accuracy_table.csv', index_col='Unnamed: 0'))

st.markdown("""
### Best Fit Model is Random Forest. 
### So, Random Forest algorithm was used to develop this model.            
""")