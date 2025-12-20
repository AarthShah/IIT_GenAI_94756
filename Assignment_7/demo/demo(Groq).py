from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GROQ_API_key")
llm = ChatGroq(model="moonshotai/kimi-k2-instruct-0905", api_key=api_key) # type: ignore

user_input = input("You: ")
result = llm.invoke(user_input)
print("AI: ", result.content)
result = llm.stream(user_input)
for chunk in result:
    print(chunk.content, end="")
    