from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

vector_db = None

def store_document(text: str):
    global vector_db

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_text(text.decode("utf-8"))

    embeddings = OpenAIEmbeddings()

    vector_db = FAISS.from_texts(docs, embeddings)