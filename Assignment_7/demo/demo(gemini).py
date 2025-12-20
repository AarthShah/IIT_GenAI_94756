from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_key")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)
user_input = input("You: ")
# result = llm.invoke(user_input)
# print("AI: ", result.content)

result = llm.stream(user_input)
for chunk in result:
    print(chunk.content, end="")