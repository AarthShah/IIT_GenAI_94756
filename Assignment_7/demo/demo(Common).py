from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_key")

llm = init_chat_model(
     model="moonshotai/kimi-k2-instruct-0905",
     model_provider="openai",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
 )

user_input = input("You: ")
result = llm.invoke(user_input)
print("AI: ", result.content)