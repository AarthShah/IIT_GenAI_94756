import pandas as pd 
import pandasql as ps

filepath='Assignment03/demo/emp_hdr.csv'

try:
    df1=pd.read_csv(filepath)
    print(df1.head(5))
    try:
        query=input("Enter your SQL query: ")
        result=ps.sqldf(query, {'data':df1})
        print(locals())
        print(result)
    
    except Exception as e:
        print("Error executing SQL query:", e)

except Exception as e:
    print("Error reading the CSV file:", e)


