import streamlit as st
import pandas as pd

def load_data(uploaded_file):
    df=pd.read_csv(uploaded_file)
    return df

def display_data(df):
    st.dataframe(df)

def check_password(username, password):
    try:
        pass_df=pd.read_csv("users.csv")
        print(pass_df.head())
        st.success("User data loaded successfully.")
    except Exception as e:
        st.error("Error Checking user data.")
        return


st.title("CSV File Uploader and Viewer")

if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False
if 'login_status' not in st.session_state:
    st.session_state.login_status = False
if 'loged_user' not in st.session_state:
    st.session_state.loged_user = ""
if 'current_page' not in st.session_state:
    st.session_state.current_page = "login"

if st.session_state.current_page == "login":
    st.header("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        check_password(username, password)


