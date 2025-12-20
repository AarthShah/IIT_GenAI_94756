from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_key")
local_api_key="Demo_KEY"
def groq_model(intput_text):
    llm = init_chat_model(
        model="moonshotai/kimi-k2-instruct-0905",
            model_provider="openai",
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )
    message =[
        SystemMessage(content="You are a professional SQL Query Executor Expert. You will get a request from user to do some operation on a SQL database. You need to generate only SQL query as per the user request and nothing else. Do not add any explanation or additional text. Make sure the SQL query is syntactically correct and can be executed without errors. instruction :- the table name is data and dont use any other table name in your query."),
        HumanMessage(content=intput_text)
    ]
    response = llm.invoke(message)
    return response.content

def local_model(intput_text):    
    local_llm = init_chat_model(
        model="meta-llama-3.1-8b-instruct",
            model_provider="openai",
            api_key=local_api_key,
            base_url="http://127.0.0.1:1234/v1")
    message =[
        SystemMessage(content="You are a professional SQL Query Executor Expert. You will get a request from user to do some operation on a SQL database. You need to generate only SQL query as per the user request and nothing else. Do not add any explanation or additional text. Make sure the SQL query is syntactically correct and can be executed without errors. instruction :- the table name is data and dont use any other table name in your query."),
        HumanMessage(content=intput_text)
    ]
    response = local_llm.invoke(message)
    return response.content

if __name__ == "__main__":
    user_input = "Write a SQL query to fetch all records from the employees table where the salary is greater than 50000."
    groq_response = groq_model(user_input)
    print("Groq Response:", groq_response)
    local_response = local_model(user_input)
    print("Local Response:", local_response)