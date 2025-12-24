from langchain.embeddings import init_embeddings
from langchain_community.document_loaders import PyPDFLoader

def get_data(data,meta,embedding):
    return data,meta,embedding
embedding_model=init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5@q8_0",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="demo",
    check_embedding_ctx_length=False
)

def load_pdf(path):
    loader=PyPDFLoader(path)
    doc=loader.load()
    content=""
    for i in doc:
        content+=i.page_content
    metadata={
        "source":path,
         "page_count":len(doc)
    }
    return content,metadata


path="C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-002.pdf"

pdf_data,pdf_metadata=load_pdf(path)

result=embedding_model.embed_documents([pdf_data])

print("content",pdf_data)
print("metadat",pdf_metadata)

for embedding in result:
    print(embedding[:4])

get_data(pdf_data,pdf_metadata,result)