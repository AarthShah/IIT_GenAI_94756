from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

llm=init_chat_model(
    model="meta-llama-3.1-8b-instruct",
    api_key="Demo_key",  # type: ignore
    base_url="http://127.0.0.1:1234/v1/",
    model_provider="openai"
)

agent=create_agent(model=llm, tools=[])

conversation=[]

while True:
    user_input=input("You: ")
    conversation.append({"role":"user","content":user_input})

    respone=agent.invoke({"messages":conversation})
    llm_output= respone["messages"][-1]
    print("AI: ", llm_output.content)

    print("\n \n all Conversation: ", respone["messages"])
    print("\n \n orignal response: ", respone)

    conversation= respone["messages"]
