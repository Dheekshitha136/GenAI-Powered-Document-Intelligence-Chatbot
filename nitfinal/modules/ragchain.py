from langchain.chains import RetrievalQA
def build_rag_chain(llm,vectordb):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=False
    )
