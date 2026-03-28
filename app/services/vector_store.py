from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

vector_db = None

def store_document(text: str):
    global vector_db

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_text(text.decode("utf-8"))

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

    vector_db = FAISS.from_texts(docs, embeddings)