import streamlit as st
from load_model import groq_model, local_model
import pandasql as  ps
import pandas as pd

st.title("SQL Query Generator And Executor ")
st.write("This app generates and executes SQL queries based on user requests using Groq and Local models.")



def get_query_response(sql):
    try:
        df=st.session_state.file
        st.write("The SQL Query is "+sql)
        st.button("Execute Query")

        if sql:
            result=ps.sqldf(sql,{'data':df})
            st.write("Query Result:")
            st.write(result)
    except Exception as e:
        st.write("Error executing SQL query:", e)



if 'current_state'  not in  st.session_state:
    st.session_state.current_state="unuploaded"


if 'file' not in st.session_state:
    st.session_state.file=None

if st.session_state.current_state == "unuploaded":
        file=st.file_uploader("Upload your CSV file",type=["csv"])
        if file is not None:
            df=pd.read_csv(file)
            st.success("File uploaded  successfully!")
            st.session_state.file=df
        else:
            st.error("failed to upload file")

        if st.session_state:
            user_input=st.text_input("Enter The data u want to find .")
            user_input=user_input+str(st.session_state.file)
            st.button("Run")
            sql=groq_model(user_input)
