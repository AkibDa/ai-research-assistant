from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from app.services.vector_store import vector_db

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo"
)

def get_response(query: str):
  if vector_db:
    docs = vector_db.similarity_search(query)
    context = " ".join([doc.page_content for doc in docs])

    prompt = f"Answer based on context: {context}\nQuestion: {query}"
    response = llm([HumanMessage(content=prompt)])
    return response.content

  return llm([HumanMessage(content=query)]).content