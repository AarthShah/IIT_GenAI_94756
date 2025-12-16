import streamlit as st 
import time
import os
import requests
import json
import dotenv


def login_page():
     st.session_state.current_state = "login"

def create_account_page():
     st.session_state.current_state = "create_account"

def create_welcome_page():
     st.session_state.current_state = "welcome_page"

def home_page():
     st.session_state.current_state = "home_page"

def logout():
     st.session_state.current_state = "login"
     st.session_state.login_status = False
     st.session_state.logined_username = None

def steam_words(title):
     
     for char in title:
          yield char + "" 
          time.sleep(0.1) 


st.set_page_config(page_title="login page", page_icon=":guardsman:")


if "username" not in st.session_state:
    st.session_state.username = []
    st.session_state.username.append("admin")
    st.session_state.username.append("A")
if "password" not in st.session_state:
    st.session_state.password = []
    st.session_state.password.append("admin123")
    st.session_state.password.append("A")
if "current_state" not in st.session_state:
    st.session_state.current_state = "login"
if "logined_username" not in st.session_state:
    st.session_state.logined_username = None
if "login_status" not in st.session_state:
    st.session_state.login_status = False

if st.session_state.current_state == "login":
    st.title("Login Page")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        create_account = st.form_submit_button("Create New Account", on_click=create_account_page)

        if submitted:
            status= False
            for i,j in zip(st.session_state.username, st.session_state.password):
                if username == i and password==j:
                    status= True
                    st.success("Login successful!")
                    st.session_state.logined_username = username
                    st.session_state.login_status = True
                    st.session_state.current_state = "welcome_page"
                    st.rerun()
                    break
                
            if not status:
                    st.error("Invalid username or password.")
    



if st.session_state.current_state == "create_account":
    st.write("Create a New Account")
    with st.form("create_account_form"):
        new_username=  st.text_input("New Username", key="new_username")
        new_password = st.text_input("New Password", type="password", key="new_password")
        create_button=st.form_submit_button("Create Account", on_click=create_account_page)
    

    if create_button:
            st.session_state.username.append(new_username)
            st.session_state.password.append(new_password)
            st.success("Account created successfully! You can now log in.")
            st.button("Go to Login Page", on_click=login_page)

if st.session_state.current_state == "welcome_page":
   title=f"Welcome {st.session_state.logined_username}..^-^ \n \n Loading your home page..."
   st.write_stream(steam_words(title))
   time.sleep(1)
   home_page()

if st.session_state.current_state == "home_page":
     st.title(f"Weather forecast page")
     city=st.text_input("Search city")
     search=st.button("Search")
     
     if search:
            API_KEY = os.getenv("OpenWeather_API_key") 
            dotenv.load_dotenv()
            st.write_stream(steam_words("Fetching weather data..."))
            url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

            response=requests.get(url)
            data=response.json()
            #print(data)
            if data.get("cod") != 200:
                 st.error("City not found. Please check the city name and try again.")
            else:
                city,description,humidity,temp=st.columns(4)

                with city:
                     st.subheader("City")
                     st.write(f"{data['name']}")
                with description:
                     st.subheader("Description")
                     st.write(f"{data['weather'][0]['description']}")
                with humidity:
                     st.subheader("Humidity")
                     st.write(f"{data['main']['humidity']}%")
                with temp:
                     st.subheader("Temperature")
                     st.write(f"{data['main']['temp']} K")
     st.button("Logout", on_click=logout)