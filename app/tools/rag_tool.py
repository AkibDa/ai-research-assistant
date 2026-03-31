# app/tools/rag_tool.py

from langchain.tools import tool
from app.services.vector_store import retrieve_similar_docs


@tool
def retrieve_user_docs(query: str) -> str:
    """
    Use this tool when the user asks questions about uploaded files,
    research notes, personal documents, or previously provided context.
    """
    docs = retrieve_similar_docs(query, k=3)

    if not docs:
        return "No relevant uploaded documents found."

    return "\n".join([doc.page_content for doc in docs])