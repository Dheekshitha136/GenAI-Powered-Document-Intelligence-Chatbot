from langchain_community.vectorstores import Chroma
def create_vector_store(chunks,embeddings):
    return Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )
