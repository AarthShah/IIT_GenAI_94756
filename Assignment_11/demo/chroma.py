import chromadb
from demo3 import pdf_data,pdf_metadata,result

db=chromadb.PersistentClient(path="./Resume_base")
collection=db.get_or_create_collection("resume")

try:
 collection.add(ids=["01"],embeddings=result,metadatas=pdf_metadata,documents=pdf_data) #type:ignore
 

 print("count :-->",collection.count())

except Exception :
    print("error to send data :")


