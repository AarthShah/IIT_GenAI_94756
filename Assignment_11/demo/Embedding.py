from langchain.embeddings import init_embeddings
import numpy as np
def consine_similarity(a, b):
    return np.dot(a,b)/(np.linalg.norm(a)* np.linalg.norm(b))

embedding_model=init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5@q8_0",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="demo",
    check_embedding_ctx_length=False
)

text=["Hello my Name is Aarth ",
       "what is You Name",
       "what is the user Name",
       "write a code in python and Name it openai",
       "what is This Age"]

result=embedding_model.embed_documents(text)

for i in result:
    print(i[:5])
    print("--"*20)

for i in range(1,5):
    print(f"1,{i}-->{consine_similarity(result[0],result[i])}")