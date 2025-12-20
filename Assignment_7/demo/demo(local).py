from langchain_openai import ChatOpenAI

API_KEY ="Demo_key"

llm=ChatOpenAI(model="google/gemma-3n-e4b"
                , api_key=API_KEY,  # type: ignore
                base_url="http://127.0.0.1:1234/v1/") 

user_input = input("You: ")
# resilt = llm.invoke(user_input)
# print("AI: ", resilt.content)
result=llm.stream(user_input)
for chunk in result:
    print(chunk.content, end="")