import streamlit as st
from chroma import *
from embedding import *
from LLM import call_model


st.title("Welcome to RAG Based Resume Anyalzer ...")

query=st.chat_input("Enter the Qurey...")
if query:
    st.chat_message("user").write(query)
    result=read_query(query)
    if result:
            with st.status("Reading dounments" , expanded= True) as status :
                if result["documents"] != None and result["metadatas"] != None:
                    for i ,j in zip(result['documents'],result["metadatas"]):
                            st.chat_message('ai').write(f"document-->,{i[:100]}")
                            st.chat_message('ai').write(f"metadata-->,{j[:50]}")
                            st.chat_message('ai').write("-_"*20)
                    result=call_model(query=query,data=result["documents"],metadata=result["metadatas"])
                else:
                    result=call_model(query=query,data="no data related to this Query ",metadata="None")        
            status.update(label="Analysis Completed",state="complete" ,expanded=False)
            st.chat_message('ai').write(result)