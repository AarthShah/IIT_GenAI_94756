import streamlit as st
from load_model import groq_model, local_model
from pandasql import sqldf
import pandas as pd

st.title("SQL Query Generator And Executor ")
st.write("This app generates and executes SQL queries based on user requests using Groq and Local models.")

def upload_file():
    file=st.file_uploader("Upload your CSV file",type=["csv"])
    if file is not None:
        df=pd.read_csv(file)
        st.session_state['dataframe']=df
        st.dataframe(df)
        st.success("File uploaded  successfully!")
    else:
        st.error("failed to upload file")

def get_query_response(model_func, user_input):
    sql_query = model_func(user_input)
    return sql_query
