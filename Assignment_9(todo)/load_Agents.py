from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.agents import create_agent
import os 

load_dotenv()

llm=init_chat_model(
    model="moonshotai/kimi-k2-instruct-0905",
    api_key= os.getenv('GROQ_API_key'),
    base_url="https://api.groq.com/openai/v1",
    model_provider='openai'
)

agent=create_agent(model=llm)

conversation=[]

while True:
    user_input=input("Enter Query :")
    conversation.append({"role":"user","content":user_input})
    response=agent.invoke({"messages":conversation})
    output=response["messages"][-1].content
    print(output)

