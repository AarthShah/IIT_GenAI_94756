from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GROQ_API_key")
api_key1="Demo_KEY"

def groq_model(intput_text):
    llm = init_chat_model(
        model="moonshotai/kimi-k2-instruct-0905",
            model_provider="openai",
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )
    message =[
        SystemMessage(content="You are a helpful assistant that remembers the last few messages in the conversation.which are in dict format and ans the last user message only. based on past message."),
        HumanMessage(content=intput_text)
    ]
    response = llm.invoke(message)
    return response.content

def local_model(intput_text):    
    local_llm = init_chat_model(
        model="meta-llama-3.1-8b-instruct",
            model_provider="openai",
            api_key=api_key1,
            base_url="http://127.0.0.1:1234/v1")
    message =[
        SystemMessage(content="You are a helpful assistant that remembers the last mesages in the conversation and ans the last user message only. based on past message. and does not mention about past messages in your answer.only menition when needed."),
        HumanMessage(content=intput_text)
    ]
    response = local_llm.invoke(message)
    return response.content
  



if __name__ == "__main__":
    user_input = "hi"
    groq_response = groq_model(user_input)
    print("Groq Response:", groq_response)
    local_response = local_model(user_input)
    print("Local Response:", local_response)