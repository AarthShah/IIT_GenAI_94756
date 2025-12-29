import selenium as se
import pandasql as ps
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from langchain_community.document_loaders import WebBaseLoader
import time

def sql_executor(query):

    # df=get_dataframe()
    if query:
        reuslt=ps.sqldf(query,{"data":df}) # type: ignore 
        return reuslt
    else:
        return  "Error : Fail to execut the Query"
    

def  web_search( ):
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

    loader = WebBaseLoader("https://www.sunbeaminfo.in/internship.php")
    doc=loader.load()
    text=''
    try :
        for i in doc:
            text+=str(i)

        lines = text.splitlines()
        clean_lines = [line.strip() for line in lines if line.strip()]

        # print(clean_lines)
        return clean_lines
    except Exception:
         return "Error while  sending  data "
    


if __name__=='__main__':
        driver = webdriver.Chrome()
        web_search()
else:
        chromeotions=Options()
        chromeotions.add_argument("--headless")
        driver = webdriver.Chrome(options=chromeotions)
        web_search()