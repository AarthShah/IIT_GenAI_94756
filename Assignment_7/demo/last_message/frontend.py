import streamlit as st
from load_model import groq_model, local_model

st.title("remember the last message with Groq and Local Models")

st.write("This app demonstrates the use of Groq and Local models to remember the last message.")

def give_chat_history():
    history=[]
    no_of_messages=st.session_state.no_of_messages
    user=st.session_state.user_history[-no_of_messages:]
    ai=st.session_state.response_history[-no_of_messages:]
    for i in range(len(user)):
        history.append(f"User :{user[i]}")
        if i < len(ai): 
            history.append(f"AI :{ai[i]}")
    return history

def display_chat():
    user=st.session_state.user_history
    ai=st.session_state.response_history
    for i in range(len(user)):
        st.chat_message("user").write(user[i])
        if i < len(ai): 
            st.chat_message("AI").write(ai[i])

if 'user_history' not in st.session_state:
    st.session_state.user_history = []
if 'response_history' not in st.session_state:
    st.session_state.response_history = []

if 'curent_model' not in st.session_state:
    st.session_state.current_model = 'local'
if'no_of_messages' not in st.session_state:
    st.session_state.no_of_messages=5

with st.sidebar:
    st.title("Select Model")
    model_choice = st.radio("Choose a model:", ('Groq Model', 'Local Model'))
    if model_choice == 'Groq Model':
        st.session_state.current_model = 'groq'
    else:
        st.session_state.current_model = 'local'
    last_message=st.slider("Select number of last messages to remember:",1,10,5)
    st.session_state.no_of_messages=last_message
    

user_intput = st.chat_input("You: ")
if user_intput:
    st.session_state.user_history.append(f"User :{user_intput}")

    if st.session_state.current_model == 'groq':
        # print(st.session_state.chat_history)
        message=give_chat_history()
        model_response = groq_model(str(message))
    else:
        message=give_chat_history()
        model_response = local_model(str(message))
        
    st.session_state.response_history.append(f"AI :{model_response}")
    display_chat()

