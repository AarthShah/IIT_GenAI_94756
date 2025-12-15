import streamlit as st
import time 

st.set_page_config(page_title="leo  Ai ", page_icon="https://cdn.dribbble.com/userupload/43003804/file/original-49a4fc8a0fb94f0a78389b25b8a2c4c1.png" )
st.title("leo Ai - Your Personal AI Chatbot 🤖")

def find_response(user_input):
    if user_input is None:
        return "hey ...!! How can I assist you today?"
    else:
        ans={"hi":"Hello! How can I assist you today?",
            "how are you":"I'm just a bunch of code, but thanks for asking! How can I help you today?",
            "what is your name":"I am leo Ai, your personal AI chatbot.", 
            "bye":"Goodbye! Have a great day!",
            "help":"Sure! I can help you with a variety of tasks. What do you need assistance with?",
            "thank you":"You're welcome! If you have any more questions, feel free to ask.",
            "default":"I'm sorry, I didn't understand that. Can you please rephrase?"
            }
        return ans.get(user_input, ans["default"])

def res(response):
     with st.spinner("leo Ai is typing..."):
        for i in response.split():
            yield i+" "
            time.sleep(0.25)


if "user_input" not in st.session_state:
    st.session_state.user_input = []
    st.write("Welcome to leo Ai, your personal AI chatbot designed to assist you with a variety of tasks. Whether you need help with answering questions, generating content, or just having a friendly chat, leo Ai is here to help!")

if "responses" not in st.session_state:
    st.session_state.responses = []



for i,j in zip(st.session_state.user_input, st.session_state.responses):

        if i != None:
            with st.chat_message("user"):
                st.write(i)
            with st.chat_message("assistant"):
                st.write(j)


input_= st.chat_input("Type your message here...")
if input_:
    st.session_state.user_input.append(input_)

    st.session_state.responses.append(find_response(input_))

    with st.chat_message("user"):
                    st.write(input_)
    with st.chat_message("assistant"):
       st.write_stream(res(st.session_state.responses[-1]))
