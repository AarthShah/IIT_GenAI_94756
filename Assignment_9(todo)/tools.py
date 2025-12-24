from langchain.tools import tool
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
import time
@tool
def sql_executor(query):
    '''
    this is a sql query_executor tool where the input is a SQL query with file name as data and outputs a resulting string 
    this can be used when the user ask question about a uploaded csv file 
    input:This only takes plain str sql query and any  other text can cause error so give just query and file name must be data eg Select * from data like this 
    output:this returns the string of result
    note: this only need SQl query nothing else and it dont need file it takes it automaticly just name the file data 
    
    '''
    # df=get_dataframe()
    if query:
        reuslt=ps.sqldf(query,{"data":df}) # type: ignore 
        return reuslt
    else:
        return  "Error : Fail to execut the Query"
    
# @tool
def  web_search(title,word=None):
    '''
    this fuction is used to get the information about sunbeam from the subeam Website this uses simler words to get the the information from the words 

    input: this takes in 2 inputs one is title and other is word
      title: this is a string which takes title of the website this titles are fixed which are 
      [about_cdac , about_sunbeam ,placement,PG Certificate Programme in Advanced Computing  as (PGCP-AC),Post Graduate Certificate Programme in Mobile Computing as (PGCP-MC),Post Graduate Certificate Programme in Embedded Systems Design as (PGCP-ESD),Post Graduate Certificate Programme in Big Data Analytics  as (PGCP-BDA),Post Graduate Certificate Programme in IT Infrastructure, Systems and Security as (PGCP-ITISS),admission:procedure,rules,faqs,registration&onlineadmission,testimonials,infrastructure,contact_us]
      
    word: this is a optional parameter where if u want to find a specific word in the topics or filed . if not  found then gives the the whole page as result  
    
    output : this will give the reult of search query in string format and if it not finds any thing or any error occures it returns error 
    '''


    driver.get("https://www.sunbeaminfo.in")
    driver.implicitly_wait(15)
    wait=WebDriverWait(driver,15)
    if title=="aboutcdac":
        element = driver.find_element(By.LINK_TEXT, "ABOUT US")
        print(element)
        action=ActionChains(driver)
        action.move_to_element(element).perform()
        # dropdown=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"dropdown-menu")))
        # print(dropdown)
        element2= wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "BRANCH")))
        print(element2)
        element2.click()
    else :
        print("Fail")
    
    time.sleep(10)
    driver.quit()



if __name__=='__main__':
        driver = webdriver.Chrome()
        web_search("aboutcdac",word=None)
else:
        chromeotions=Options()
        chromeotions.add_argument("--headless")
        driver = webdriver.Chrome(options=chromeotions)
        web_search("aboutcdac",word=None)