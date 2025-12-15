import streamlit as st
import pandas as pd
import pandasql as ps

def upload_csv():
        try :
            st.title("Pandas Dataframe SQL Query Executor...")
            file = st.file_uploader("Upload your CSV file",type=['csv'])
            if file:
             df=pd.read_csv(file)
             st.write("First 5 rows of the uploaded CSV file:")
             st.write(df.head())
             return df
        except Exception as e:
            st.write("Error uploading the CSV file:", e)
        

def sql_query_execution():
    try:
        df=st.session_state.df
        query=st.text_area("Enter Your SQL Query Here :")
        st.button("Execute Query")

        if query:
            result=ps.sqldf(query,{'data':df})
            st.write("Query Result:")
            st.write(result)
    except Exception as e:
        st.write("Error executing SQL query:", e)



def change_state(page_name):
    st.session_state.page=page_name

if 'page' not in st.session_state:
    st.session_state.page='upload'

if 'df' not in st.session_state:
    st.session_state.df=None






if st.session_state.page=='upload':
    df=upload_csv()
    if df is not None:
        st.session_state.df=df
        st.button("Proceed to SQL Query Execution",on_click=change_state, args=("query",))

elif st.session_state.page=='query':
    sql_query_execution()


   

