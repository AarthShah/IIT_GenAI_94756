from langchain.chat_models import init_chat_model
from langchain.tools import tool
from dotenv import load_dotenv
from langchain.agents import create_agent
from toolss import sql_executor,web_search
import os 

load_dotenv()

@tool
def sql_executors(query):
        '''
    this is a sql query_executor tool where the input is a SQL query with file name as data and outputs a resulting string 
    this can be used when the user ask question about a uploaded csv file 
    input:This only takes plain str sql query and any  other text can cause error so give just query and file name must be data eg Select * from data like this 
    output:this returns the string of result
    note: this only need SQl query nothing else and it dont need file it takes it automaticly just name the file data 
    
    '''
        sql_executor(query)

@tool
def web_searchs():
      """
        This function extracts all textual information from the Sunbeam Internship webpage.

        Description:
        Loads the Sunbeam Internship page from the official website.
        Returns all readable information available on the internship page.

        Inputs:
        - None

        Behavior:
        - No searching, filtering, or keyword-based operations are performed.
        - Calling the function directly returns the complete content of the Sunbeam Internship page.

        Output:
        - Returns a list of text lines (list of strings).
        - Each list item represents information from the Sunbeam Internship webpage.
        - Returns an error if webpage loading fails.
    """
      web_search()
      

llm=init_chat_model(
    model="moonshotai/kimi-k2-instruct-0905",
    api_key= os.getenv('GROQ_API_key'),
    base_url="https://api.groq.com/openai/v1",
    model_provider='openai'
)

agent=create_agent(model=llm,tools=[web_searchs,sql_executors])

conversation=[]

while True:
    user_input=input("Enter Query :")
    conversation.append({"role":"user","content":user_input})
    response=agent.invoke({"messages":conversation})
    output=response["messages"][-1].content
    print(output)

