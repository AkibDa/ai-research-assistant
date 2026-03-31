# app/services/llm_service.py

from app.services.agent_service import agent
from app.services.vector_store import retrieve_similar_docs
from app.utils.memory_store import get_user_messages, save_message
from app.utils.parser import normalize_llm_content


def get_user_context(query: str):
    docs = retrieve_similar_docs(query, k=3)
    return "\n".join([doc.page_content for doc in docs])


def get_response(query: str, user: str):
    memory = get_user_messages(user)
    doc_context = get_user_context(query)

    messages = []

    if doc_context:
        messages.append({
            "role": "system",
            "content": f"Use this retrieved document context:\n{doc_context}"
        })

    messages.extend(memory)
    messages.append({"role": "user", "content": query})

    state = {"messages": messages}

    response = agent.invoke(state)

    final_response = normalize_llm_content(
        response["messages"][-1].content
    )

    save_message(user, "user", query)
    save_message(user, "assistant", final_response)

    return final_response
