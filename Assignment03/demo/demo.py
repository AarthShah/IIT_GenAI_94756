import streamlit as st 

def change_state():
     st.session_state.current_page='counter'


if 'current_page'  not in st.session_state:
    st.session_state.current_page='login'
if 'counter' not in st.session_state:
    st.session_state.counter=0
if 'name' not in st.session_state:
    st.session_state.name=""



if st.session_state.current_page=='login':
     st.title("Welcome Counter App...^_^")
     st.session_state.name=st.text_input("Enter Your Name")
     if st.session_state.name !="":
        st.session_state.current_page='title'

if st.session_state.current_page=='title':
        st.title("Welcome Counter App...^_^")
        st.write(f"Hello,{st.session_state.name}..!!")
        st.button("Welcome",on_click=change_state)
       

elif st.session_state.current_page=='counter':
    st.title("Welcome to Counter App...^_^")

    def increment_counter():
        st.session_state.counter += 1
    def reset_counter():
        st.session_state.counter = 0
    def decrement_counter():
        st.session_state.counter -= 1
    
    st.button("Increment", on_click=increment_counter)
    st.button("Decrement", on_click=decrement_counter)
    st.button("Reset", on_click=reset_counter)

    st.write(f"Counter Value: {st.session_state.counter}")




