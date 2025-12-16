import requests as req
try:
    url ="https://raw.githubusercontent.com/Ovi/DummyJSON/master/database/users.json"

    response=req.get(url)

    result=response.json()

    print("Data fetched successfully........^-^")
    print("Writing data to users.json file........^-^")

    with open("C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment2\\Q3\\users.json","w") as f:
        f.write(response.text)

except :
    print("Error occurred plz try again later........^_^")