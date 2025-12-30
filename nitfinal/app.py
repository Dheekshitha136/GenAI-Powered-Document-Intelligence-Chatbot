import gradio as gr
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from modules.pdf_loader import load_pdf
from modules.embeddings import get_embeddings
from modules.vector_store import create_vector_store
from modules.llm import load_llm
from modules.rag_chain import build_rag_chain
from modules.voice import speak
load_dotenv()
qa_chain=None

def process_pdf(pdf_file):
    global qa_chain
    text=load_pdf(pdf_file.name)
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunks=splitter.split_text(text)
    embeddings=get_embeddings()
    vectordb=create_vector_store(chunks,embeddings)
    llm=load_llm()
    qa_chain=build_rag_chain(llm,vectordb)
    return "PDF processed successfully. Ask your questions!"
def chat(query,history,voice_enabled):
    if qa_chain is None:
        history.append((query,"Please upload a PDF first."))
        return history
    response=qa_chain.invoke({"query": query})["result"]
    speak(response,enable_voice=voice_enabled)
    history.append((query,response))
    return history
with gr.Blocks(title="SmartPDF Chatbot") as demo:
    gr.Markdown("SmartPDF-Cross-Platform Voice-Enabled RAG Chatbot")
    pdf=gr.File(label="Upload PDF",file_types=[".pdf"])
    status=gr.Textbox(label="Status",interactive=False)
    pdf.upload(process_pdf, pdf, status)
    chatbot=gr.Chatbot(height=350)
    query=gr.Textbox(label="Ask a question")
    voice_toggle=gr.Checkbox(label="Enable Voice Output (Optional)", value=False)
    query.submit(chat,[query, chatbot, voice_toggle],chatbot)
demo.launch()
