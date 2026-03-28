from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from app.services.vector_store import vector_db

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def get_response(query: str):
  if vector_db:
    docs = vector_db.similarity_search(query)
    context = " ".join([doc.page_content for doc in docs])

    prompt = f"Answer based on context: {context}\nQuestion: {query}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

  return llm.invoke([HumanMessage(content=query)]).content