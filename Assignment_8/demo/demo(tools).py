from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

model =init_chat_model(
    model="google/gemma-3n-e4b",
    api_key="Demo_key",  # type: ignore
    base_url="http://127.0.0.1:1234/v1/",
    model_provider="openai"
)
@tool
def calculator_tool(expression):
    """A simple caluculator tool to evaluate mathematical expresstions
    
    instractions: it can only perfrom basic mathematical operations like addition, subtraction, multiplication, division only nothing else
       
    Aguments: its take a string exprestion as input like "2*3+5"
        
    Returns: the result of the evaluated expression in  string format.

    exception : if it false to give a result as error 
    """
    try:
        reslut = eval(expression)
        return str(reslut)
    except Exception as e:
        return ("Error")
    
@tool
def weather_tool(city):
    """
    This is A wearther Tool which will give u weather info about a particular city
    and give the response in json format

     eg : city is pune then it will return weather info about pune city

     Aguments: city name in string format

     Returns:wearther info in json format
     
     error if it failed to give weather info it will return error message containing error
    
     exception: it only gives the weather info of current day not past or future days

       """
    API_key = os.getenv("OpenWeather_API_key")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
 
    try:
        response=requests.get(url)
        response=response.json()
        return json.dumps(response)
    except Exception as e:
        return ("Error: failed to get weather info")


    

agents=create_agent(model=model,
              tools=[calculator_tool, weather_tool],
              system_prompt="You are a helpful AI assistant that can use tools to answer user queries. which include a calculator tool to evaluate mathematical expressions and a weather tool to get current weather information for a given city. and solve comlex problems by breaking them down into simpler sub-problems that can be solved using these tools. and if the probles are  to complex and tools can not solve then you convert the exprassion into simple expreastion that the tools can solve  and then do it u can use toolls as many times as needed to get the final answer."
              )

conversation=[]

while True:
    user_input=input("You:...")
    conversation.append({"role":"user","content":user_input})

    response=agents.invoke({"messages":conversation})
    llm_output=response["messages"][-1]
    print("AI :",llm_output.content)
    # print("\n \n all Conversation: ", response["messages"])
    # print("\n \n orignal response: ", response)
    conversation=response["messages"]