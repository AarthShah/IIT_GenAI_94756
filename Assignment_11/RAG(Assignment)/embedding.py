from langchain.embeddings import init_embeddings
from langchain_community.document_loaders import PyPDFLoader
#from langchain_text_splitters import NLTKTextSplitter
from chroma import add_data,update_data,get_data_for_Embed_query

embed_model=init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5@q8_0",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="demo",
    check_embedding_ctx_length=False
)

def add_pdf(path):
    name,id=get_name(path)
    loder=PyPDFLoader(path)
    doc=loder.load()
    content=""
    for i in doc:
        content+=i.page_content
    
    metadatas={
    "source":path,
    "File_name":name,
    "Pages":len(doc)

    }

    embed_data=embed_model.embed_documents([content])

    add_data(data=content,metadata=metadatas,embed=embed_data,id=id)


def update_pdf(id,path):
    name,id=get_name(path)
    loder=PyPDFLoader(path)
    doc=loder.load()
    content=""
    for i in doc:
        content+=i.page_content
    
    metadatas={
    "source":path,
    "File_name":name,
    "Pages":len(doc)

    }

    embed_data=embed_model.embed_documents([content])

    update_data(data=content,metadata=metadatas,embed=embed_data,id=id)




def get_name(path):
    last=path.split("\\")[-1]
    id=last.split(".pdf")[-2]
    # print(last)
    return last,id



def read_query(query):
    Equery=embed_model.embed_documents([query])
    get_data_for_Embed_query(Equery)


if "__name__"=="__name__":
    # add_pdf( r"C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-004.pdf")
    # add_pdf( r"C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-005.pdf")
    # add_pdf( r"C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-006.pdf")
    # add_pdf( r"C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-007.pdf")
    # add_pdf( r"C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-008.pdf")
    # add_pdf( r"C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-009.pdf")
    # add_pdf( r"C:\\Users\\Aarth Shah\\OneDrive\\Desktop\\Sunbeam\\IIT_GenAI_94756\\Assignment_11\\resume\\resume-010.pdf")
    read_query("find the reusmes of Data Data Analyst")

